import os
import time

# Secure parameters system variables fetch
db_user = os.environ.get('DB_USER', 'guest_user')
env_mode = os.environ.get('ENV_MODE', 'development')

print("🚀 Backend Application Monitoring Service Live!")
print(f"🌍 Mode: {env_mode} | Active Admin Role: {db_user}")

# Infinite loop backend container live run
while True:
    time.sleep(3600)
