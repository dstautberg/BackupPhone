import subprocess
import sys
import os
import shutil
from dotenv import load_dotenv

def run_backup():
    # Load environment variables from .env file
    load_dotenv()
    
    # 1. Configuration
    # Use proper Windows path format
    # Can be overridden by BACKUP_DESTINATION in .env file
    destination = os.getenv("BACKUP_DESTINATION", "D:\\downloads\\Backup-Pixel6a")
    
    # Ensure the destination directory exists
    os.makedirs(destination, exist_ok=True)
    
    # Source uses Unix-style path for ADB compatibility
    source = "/sdcard/"
    
    print(f"--- Starting Pixel 6a Backup to {destination} ---")

    # 2. Check if ADB is available
    adb_path = shutil.which("adb")
    if not adb_path:
        print("Error: ADB not found in PATH.")
        print("Please install Android Platform Tools from:")
        print("https://developer.android.com/studio/releases/platform-tools")
        return
    
    print(f"Using ADB from: {adb_path}")

    # 3. Check if device is connected via ADB
    check_device = subprocess.run(["adb", "get-state"], capture_output=True, text=True)
    
    if "device" not in check_device.stdout:
        print("Error: No Pixel detected. Please connect your phone and enable USB debugging.")
        return

    # 4. List contents of /sdcard/
    print(f"\nListing contents of {source}...")
    list_result = subprocess.run(["adb", "shell", "ls", "/sdcard/"], capture_output=True, text=True)
    
    if list_result.returncode != 0:
        print(f"Error listing directory: {list_result.stderr}")
        return
    
    # Parse the directory listing
    entries = [entry.strip() for entry in list_result.stdout.strip().split('\n') if entry.strip()]
    
    if not entries:
        print("No entries found in /sdcard/")
        return
    
    print(f"Found {len(entries)} entries to backup:")
    for entry in entries:
        print(f"  - {entry}")
    
    print("\n--- Starting backup process ---\n")

    # 5. Loop through each entry and sync it
    success_count = 0
    failed_count = 0
    
    for entry in entries:
        # Skip hidden files/folders (starting with .)
        if entry.startswith('.'):
            print(f"Skipping hidden entry: {entry}")
            continue
        
        entry_source = f"/sdcard/{entry}"
        entry_dest = destination
        
        print(f"\n>>> Syncing: {entry}")
        
        # Construct the adbsync command for this entry
        cmd = [
            "adbsync",
            "--exclude", "**/.*",  # Skip hidden system files
            "pull",
            entry_source, 
            entry_dest
        ]
        
        try:
            # Execute the sync for this entry
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            
            for line in process.stdout:
                print(line, end="")
                
            process.wait()
            
            if process.returncode == 0:
                print(f"✓ Successfully synced: {entry}")
                success_count += 1
            else:
                print(f"✗ Failed to sync: {entry} (exit code {process.returncode})")
                failed_count += 1
                
        except KeyboardInterrupt:
            print("\n\nBackup cancelled by user.")
            print(f"\nSummary: {success_count} succeeded, {failed_count} failed, {len(entries) - success_count - failed_count} not processed")
            return
        except Exception as e:
            print(f"✗ Error syncing {entry}: {e}")
            failed_count += 1
    
    # 6. Print summary
    print("\n" + "="*60)
    print("--- Backup Completed ---")
    print(f"Total entries: {len(entries)}")
    print(f"Successfully synced: {success_count}")
    print(f"Failed: {failed_count}")
    print(f"Skipped (hidden): {len(entries) - success_count - failed_count}")
    print(f"\nBackup location: {destination}")
    print("="*60)

if __name__ == "__main__":
    run_backup()
