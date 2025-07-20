#!/usr/bin/env bash
# exit on error
set -o errexit

echo "🚀 Starting StockLift build process..."

# Check Python version
echo "🐍 Python version:"
python --version

# Install requirements with --no-build-isolation to avoid setuptools issues
echo "📥 Installing Python dependencies..."
pip install --no-build-isolation -r requirements.txt

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p uploads
mkdir -p processed
mkdir -p exports
mkdir -p static/backgrounds

# Set permissions
echo "🔐 Setting permissions..."
chmod 755 uploads
chmod 755 processed
chmod 755 exports
chmod 755 static/backgrounds

# Verify installations
echo "✅ Verifying installations..."
python -c "import flask, pandas, numpy, sklearn, xgboost, tensorflow, cv2, PIL; print('All core packages imported successfully!')"

echo "🎉 Build completed successfully!" 