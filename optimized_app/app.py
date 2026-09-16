import psutil
import sys

print("🚀 Highly Optimized Production Container Started!")
print(f"📦 Python Version Runtime: {sys.version}")

# Core hardware info metrics fetch karna
cpu_count = psutil.cpu_count()
print(f"⚡ System Core Count Detected: {cpu_count} CPUs")
