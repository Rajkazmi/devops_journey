import os
import shutil
from datetime import datetime

def create_backup():
    source_dir = "/home/admin_raj/devops_learning/my_project"
    backup_dir = "/home/admin_raj/devops_backup"

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        print(f"📁 Created backup directory at: {backup_dir}")

    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = f"project_backup_{current_time}"
    full_backup_path = os.path.join(backup_dir, backup_filename)

    try:
        print("⚡ Compressing files...")
        shutil.make_archive(full_backup_path, 'zip', source_dir)
        print(f"🎉 SUCCESS: Backup created at {full_backup_path}.zip")
    except Exception as e:
        print(f"🚨 ERROR: Backup failed! Reason: {e}")

create_backup()
