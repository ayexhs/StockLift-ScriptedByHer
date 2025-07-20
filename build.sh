#!/usr/bin/env bash
# exit on error
set -o errexit

echo "🚀 Starting StockLift build process..."

# Upgrade pip and setuptools first
echo "📦 Upgrading pip and setuptools..."
pip install --upgrade pip setuptools wheel

# Install requirements
echo "📥 Installing Python dependencies..."
pip install -r requirements.txt

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