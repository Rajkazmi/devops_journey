import psutil
disk = psutil.disk_usage('/')
total_gb = round(disk.total / (1024**3), 2)
used_gb = round(disk.used / (1024**3), 2)
free_gb = round(disk.free / (1024**3), 2)

print("=== SERVER STORAGE REPORT ===")
print(f"Total Disk Space: {total_gb} GB")
print(f"Used Space: {used_gb} GB")
print(f"Free space Availble: {free_gb} GB")
print(f"Usage Percentage: {disk.percent}%")

if disk.percent > 80:
    print("🚨 ALERT: Disk usage is above 80%! Clean up space immediately.")
else:
    print("✅ SYSTEM STATUS: Storage is healthy.")
