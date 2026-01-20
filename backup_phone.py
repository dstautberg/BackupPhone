import subprocess
import sys
import os

def run_backup():
    # 1. Configuration
    # Note: Using //sdcard/ for MinGW path compatibility
    source = "//sdcard/"
    destination = "/g/My Drive/Backup-Pixel6a"
    
    print(f"--- Starting Pixel 6a Backup to {destination} ---")

    # 2. Check if device is connected via ADB
    check_device = subprocess.run(["adb", "get-state"], capture_output=True, text=True)
    
    if "device" not in check_device.stdout:
        print("Error: No Pixel detected. Please connect your phone and enable USB debugging.")
        return

    # 3. Construct the BetterADBSync command
    # We use 'python -m BetterADBSync' to ensure it uses the installed module
    cmd = [
        "python", "-m", "BetterADBSync", 
        "pull", 
        "--exclude", "**/.*",  # Skip hidden system files
        source, 
        destination
    ]

    try:
        # 4. Execute the sync
        # bufsize=1 and universal_newlines=True allow us to see the output in real-time
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        
        for line in process.stdout:
            print(line, end="")
            
        process.wait()
        
        if process.returncode == 0:
            print("\n--- Backup Completed Successfully! ---")
        else:
            print(f"\n--- Backup failed with exit code {process.returncode} ---")

    except KeyboardInterrupt:
        print("\nBackup cancelled by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    run_backup()
