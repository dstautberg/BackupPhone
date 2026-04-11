# Pixel 6a Backup Tool

A Python script to backup your Pixel 6a phone to a local directory using ADB (Android Debug Bridge) and BetterADBSync.

Note: The backup_phone.py script has moved to my https://github.com/dstautberg/misc_tools repository. Any future changes will happen there.

## Overview

This tool automates the process of backing up your Pixel 6a's internal storage to a destination folder. It uses ADB to communicate with your phone and BetterADBSync to efficiently synchronize files while excluding hidden system files.

## Prerequisites

- **Python 3.6+** installed on your system
- **ADB (Android Debug Bridge)** installed and added to your system PATH
- **BetterADBSync** Python package (`adbsync` command)
- **python-dotenv** for configuration management
- **USB Debugging** enabled on your Pixel 6a

### Installing Dependencies

1. Install ADB:
   - **Windows**: Download [Android SDK Platform Tools](https://developer.android.com/studio/releases/platform-tools) and add to PATH
   - **macOS**: `brew install android-platform-tools`
   - **Linux**: `sudo apt-get install adb` (Ubuntu/Debian)

2. Install Python packages:
   ```
   pip install BetterADBSync python-dotenv
   ```

## Setup

1. **Enable USB Debugging** on your Pixel 6a:
- Go to Settings > About phone
- Tap "Build number" 7 times to enable Developer options
- Go to Settings > System > Developer options
- Enable "USB debugging"

2. **Configure the backup destination**:
- Copy `.env.example` to `.env`:
  ```
  cp .env.example .env
  ```
- Edit `.env` and set your backup destination:
  ```
  BACKUP_DESTINATION=D:\\downloads\\Backup-Pixel6a
  ```
- Use Windows path format with double backslashes (`\\`) or forward slashes (`/`)

3. **Connect your phone**:
   - Connect your Pixel 6a via USB
   - Accept the USB debugging authorization prompt on your phone

## Usage

Run the backup script:

```
python backup_phone.py
```

The script will:
1. Check if ADB is available and your Pixel 6a is connected
2. List all entries in `/sdcard/`
3. Sync each entry individually to your specified destination folder
4. Exclude hidden system files (files/folders starting with `.`)
5. Display real-time progress for each entry
6. Report a summary with success/failure counts

### Canceling a Backup

Press `Ctrl+C` to cancel the backup operation at any time. The script will display a summary of completed backups.

## Configuration

### Environment Variables (.env file)

- **`BACKUP_DESTINATION`**: The local path where backups are saved
  - Default: `D:\downloads\Backup-Pixel6a`
  - Example: `BACKUP_DESTINATION=D:\\MyBackups\\Phone` or `BACKUP_DESTINATION=D:/MyBackups/Phone`

### Script Settings

You can modify the following in `backup_phone.py`:

- **`source`**: The path on your phone to backup (default: `/sdcard/`)
- **`--exclude` pattern**: Modify the exclusion pattern to skip different file types (default: `**/.*`)

## Troubleshooting

### "No Pixel detected" Error
- Ensure USB debugging is enabled on your phone
- Check that your phone is connected via USB
- Run `adb devices` to verify the device is recognized
- Try restarting ADB: `adb kill-server` then `adb start-server`

### "Command not found: adb"
- ADB is not installed or not in your system PATH
- Install Android SDK Platform Tools and add to PATH

### BetterADBSync/adbsync Not Found
- Run `pip install BetterADBSync` to install the required package
- Verify installation: `adbsync --version`

### Files Not Appearing in Expected Location
- Check the script output for "Backup location:" to see where files were saved
- Ensure you're using proper Windows path format in `.env`: `D:\\path\\to\\folder` or `D:/path/to/folder`
- Verify the destination folder exists and you have write permissions

### Permission Denied
- Ensure you have write permissions to the destination folder
- On Android, some system folders may be inaccessible even with USB debugging

## Notes

- The script backs up each top-level entry in `/sdcard/` individually for better progress tracking
- Hidden files and folders (starting with `.`) are excluded by default to avoid backing up system files
- The backup is incremental - BetterADBSync only transfers new or modified files
- The `.env` file is gitignored to keep personal paths private

## License

This is a personal backup tool. Feel free to modify and use as needed.

