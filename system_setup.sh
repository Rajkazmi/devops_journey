#!/bin/bash

echo "=========================================="
echo "STARTING AUTOMATED SYSTEM UPDATE & BACKUP"
echo "=========================================="

echo "Step 1: Updating system repository..."
sudo apt update -y

echo "Step 2: Creating a secure backup directory..."
mkdir -p ~/devops_backup

echo "Step 3: Checking system uptme..."
uptime

echo "=========================================="
echo " SYSTEM SETUP COMPLETED SUCCESSSFULLY"
echo "=========================================="
