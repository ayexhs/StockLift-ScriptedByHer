#!/usr/bin/env python3
"""
StockLift Render Deployment Helper Script

This script helps prepare your StockLift application for deployment on Render.com
"""

import os
import sys

def check_requirements():
    """Check if all required files exist"""
    required_files = [
        'app.py',
        'requirements.txt',
        'build.sh',
        'render.yaml'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    
    print("✅ All required files found")
    return True

def check_directories():
    """Check if required directories exist"""
    required_dirs = [
        'static',
        'templates',
        'models',
        'uploads',
        'processed',
        'exports'
    ]
    
    missing_dirs = []
    for dir_name in required_dirs:
        if not os.path.exists(dir_name):
            missing_dirs.append(dir_name)
    
    if missing_dirs:
        print("❌ Missing required directories:")
        for dir_name in missing_dirs:
            print(f"   - {dir_name}")
        return False
    
    print("✅ All required directories found")
    return True

def check_environment_variables():
    """Check if environment variables are set"""
    print("\n🔧 Environment Variables Check:")
    
    # Optional but recommended
    if os.environ.get('GOOGLE_API_KEY'):
        print("✅ GOOGLE_API_KEY is set")
    else:
        print("⚠️  GOOGLE_API_KEY not set (Photogenix AI features may not work)")
    
    # Required for production
    if os.environ.get('FLASK_ENV'):
        print("✅ FLASK_ENV is set")
    else:
        print("⚠️  FLASK_ENV not set (will use development mode)")

def main():
    print("🚀 StockLift Render Deployment Checker")
    print("=" * 40)
    
    # Check files
    print("\n📁 Checking required files...")
    files_ok = check_requirements()
    
    # Check directories
    print("\n📂 Checking required directories...")
    dirs_ok = check_directories()
    
    # Check environment
    check_environment_variables()
    
    print("\n" + "=" * 40)
    if files_ok and dirs_ok:
        print("✅ Your application is ready for Render deployment!")
        print("\n📋 Next steps:")
        print("1. Push your code to GitHub")
        print("2. Go to render.com and create a new Web Service")
        print("3. Connect your GitHub repository")
        print("4. Use the render.yaml configuration")
        print("5. Set your environment variables")
        print("6. Deploy!")
    else:
        print("❌ Please fix the issues above before deploying")
        sys.exit(1)

if __name__ == "__main__":
    main() 