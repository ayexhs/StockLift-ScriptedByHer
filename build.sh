#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Create necessary directories
mkdir -p uploads
mkdir -p processed
mkdir -p exports

# Set permissions
chmod 755 uploads
chmod 755 processed
chmod 755 exports 