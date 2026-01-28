import schedule
import time
from backup_phone import run_backup

def job():
    print("\n" + "="*60)
    print("Starting scheduled backup...")
    print("="*60 + "\n")
    run_backup()

# Schedule the backup to run daily at 11:00 PM
schedule.every().day.at("23:00").do(job)

print("Backup scheduler started. Waiting for scheduled time (11:00 PM)...")
print("Press Ctrl+C to stop the scheduler.\n")

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute