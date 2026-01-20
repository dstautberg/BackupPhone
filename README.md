# Pixel 6a Backup Tool

A Python script to backup your Pixel 6a phone to a directory using ADB (Android Debug Bridge) and BetterADBSync.

## Overview

This tool automates the process of backing up your Pixel 6a's internal storage to destination path. It uses ADB to communicate with your phone and BetterADBSync to efficiently synchronize files while excluding hidden system files.

## Prerequisites

- **Python 3.6+** installed on your system
- **ADB (Android Debug Bridge)** installed and added to your system PATH
- **BetterADBSync** Python package
- **USB Debugging** enabled on your Pixel 6a

### Installing Dependencies

1. Install ADB:
   - **Windows**: Download [Android SDK Platform Tools](https://developer.android.com/studio/releases/platform-tools) and add to PATH
   - **macOS**: `brew install android-platform-tools`
   - **Linux**: `sudo apt-get install adb` (Ubuntu/Debian)

2. Install BetterADBSync:
   ```
   pip install BetterADBSync
   ```

## Setup

1. **Enable USB Debugging** on your Pixel 6a:
- Go to Settings > About phone
- Tap "Build number" 7 times to enable Developer options
- Go to Settings > System > Developer options
- Enable "USB debugging"

2. **Configure the backup destination**:
- Edit `backup_phone.py` and update the `destination` variable to match your destination path:
     ```python
     destination = "/d/downloads/Backup-Pixel6a"  # Update this path as needed
     ```

3. **Connect your phone**:
   - Connect your Pixel 6a via USB
   - Accept the USB debugging authorization prompt on your phone

## Usage

Run the backup script:

```
python backup_phone.py
```

The script will:
1. Check if your Pixel 6a is connected via ADB
2. Sync all files from `/sdcard/` to your specified folder
3. Exclude hidden system files (files starting with `.`)
4. Display real-time progress
5. Report completion status

### Canceling a Backup

Press `Ctrl+C` to cancel the backup operation at any time.

## Configuration

You can modify the following settings in `backup_phone.py`:

- **`source`**: The path on your phone to backup (default: `//sdcard/`)
- **`destination`**: The local path where backups are saved (default: `/d/downloads/Backup-Pixel6a`)
- **`--exclude` pattern**: Modify the exclusion pattern to skip different file types

## Troubleshooting

### "No Pixel detected" Error
- Ensure USB debugging is enabled on your phone
- Check that your phone is connected via USB
- Run `adb devices` to verify the device is recognized
- Try restarting ADB: `adb kill-server` then `adb start-server`

### "Command not found: adb"
- ADB is not installed or not in your system PATH
- Install Android SDK Platform Tools and add to PATH

### BetterADBSync Import Error
- Run `pip install BetterADBSync` to install the required package

### Permission Denied
- Ensure you have write permissions to the destination folder
- On Android, some system folders may be inaccessible even with USB debugging

## Notes

- The script uses `//sdcard/` path format for MinGW/Git Bash compatibility on Windows
- Hidden files and folders (starting with `.`) are excluded by default to avoid backing up system files
- The backup is incremental - BetterADBSync only transfers new or modified files

## License

This is a personal backup tool. Feel free to modify and use as needed.

