import os

db_pass = os.environ.get('DB_PASSWORD', 'NOT_FOUND')
api_key = os.environ.get('API_KEY', 'NOT_FOUND')
env = os.environ.get('ENVIRONMENT', 'development')

print("🚀 Secure Application Starting...")
print(f"🌍 Running in Configuration Mode: {env}")
print(f"🔑 Fetched DB Password securely: {db_pass}")
print(f"⚡ Fetched API Key securely: {api_key}")
