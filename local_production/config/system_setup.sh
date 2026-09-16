#!/bin/bash

echo "🧹 --- SERVER AUTOMATIC MAINTENANCE STARTED ---"
echo "🕒 Current Time: $(date)"

# Unused docker containers, networks aur local cache ko safe clear karna
docker system prune -f

echo "🎉 --- MAINTENANCE COMPLETED SUCCESSFULLY ---"
