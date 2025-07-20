#!/usr/bin/env python3
"""
StockLift Comprehensive Compatibility Checker

This script verifies that all dependencies are compatible and working together.
"""

import sys
import importlib
import subprocess
from pathlib import Path

def check_python_version():
    """Check Python version compatibility"""
    print("🐍 Checking Python version...")
    version = sys.version_info
    print(f"   Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major == 3 and version.minor == 11:
        print("   ✅ Python 3.11 is compatible")
        return True
    else:
        print(f"   ⚠️  Python {version.major}.{version.minor} may have compatibility issues")
        return False

def check_package_imports():
    """Check if all required packages can be imported"""
    print("\n📦 Checking package imports...")
    
    packages = [
        # Core web framework
        ('flask', 'Flask'),
        ('werkzeug', 'Werkzeug'),
        ('jinja2', 'Jinja2'),
        
        # Data processing
        ('numpy', 'NumPy'),
        ('pandas', 'Pandas'),
        ('sklearn', 'Scikit-learn'),
        ('xgboost', 'XGBoost'),
        ('mlxtend', 'MLxtend'),
        
        # Deep learning
        ('tensorflow', 'TensorFlow'),
        ('keras', 'Keras'),
        
        # HTTP and API
        ('requests', 'Requests'),
        ('urllib3', 'urllib3'),
        
        # Date and time
        ('dateutil', 'python-dateutil'),
        ('pytz', 'pytz'),
        
        # Geospatial
        ('geopy', 'Geopy'),
        
        # Visualization
        ('plotly', 'Plotly'),
        ('dash', 'Dash'),
        
        # Image processing
        ('PIL', 'Pillow'),
        ('cv2', 'OpenCV'),
        
        # AI services
        ('google.generativeai', 'Google Generative AI'),
        
        # Environment
        ('dotenv', 'python-dotenv'),
        
        # Production
        ('gunicorn', 'Gunicorn'),
    ]
    
    failed_imports = []
    
    for module_name, display_name in packages:
        try:
            importlib.import_module(module_name)
            print(f"   ✅ {display_name}")
        except ImportError as e:
            print(f"   ❌ {display_name}: {e}")
            failed_imports.append(display_name)
    
    return len(failed_imports) == 0

def check_tensorflow_compatibility():
    """Check TensorFlow specific compatibility"""
    print("\n🧠 Checking TensorFlow compatibility...")
    
    try:
        import tensorflow as tf
        print(f"   ✅ TensorFlow version: {tf.__version__}")
        
        # Check if it's CPU version
        if 'cpu' in tf.__version__.lower() or 'cpu' in tf.__file__.lower():
            print("   ✅ TensorFlow CPU version detected")
        else:
            print("   ⚠️  Full TensorFlow detected (may cause issues on Render)")
        
        # Test basic functionality
        test_tensor = tf.constant([1, 2, 3])
        result = tf.reduce_sum(test_tensor)
        print(f"   ✅ TensorFlow basic operations work: {result.numpy()}")
        
        return True
    except Exception as e:
        print(f"   ❌ TensorFlow error: {e}")
        return False

def check_flask_app():
    """Check if Flask app can be imported"""
    print("\n🌐 Checking Flask application...")
    
    try:
        # Add current directory to path
        sys.path.insert(0, str(Path.cwd()))
        
        # Try to import the app
        from app import app
        print("   ✅ Flask app imported successfully")
        
        # Check if app has required attributes
        if hasattr(app, 'config'):
            print("   ✅ App configuration available")
        else:
            print("   ⚠️  App configuration not found")
        
        return True
    except Exception as e:
        print(f"   ❌ Flask app error: {e}")
        return False

def check_directories():
    """Check if required directories exist"""
    print("\n📁 Checking directories...")
    
    required_dirs = [
        'static',
        'templates', 
        'models',
        'uploads',
        'processed',
        'exports',
        'static/backgrounds',
        'static/css',
        'static/js',
        'static/img'
    ]
    
    missing_dirs = []
    
    for dir_path in required_dirs:
        if Path(dir_path).exists():
            print(f"   ✅ {dir_path}")
        else:
            print(f"   ❌ {dir_path} (missing)")
            missing_dirs.append(dir_path)
    
    return len(missing_dirs) == 0

def check_model_files():
    """Check if ML model files exist"""
    print("\n🤖 Checking ML model files...")
    
    model_files = [
        'models/bundle_model.pkl',
        'models/discount_model.pkl', 
        'models/xgboost_health_model.pkl',
        'u2net/u2netp.pth'
    ]
    
    missing_models = []
    
    for model_file in model_files:
        if Path(model_file).exists():
            print(f"   ✅ {model_file}")
        else:
            print(f"   ⚠️  {model_file} (missing - will be created at runtime)")
            missing_models.append(model_file)
    
    return True  # Models can be created at runtime

def check_render_compatibility():
    """Check Render-specific compatibility"""
    print("\n☁️  Checking Render compatibility...")
    
    # Check if we're in a Render-like environment
    render_env = any([
        'RENDER' in os.environ,
        'PORT' in os.environ,
        Path('/opt/render').exists()
    ])
    
    if render_env:
        print("   ✅ Render environment detected")
    else:
        print("   ℹ️  Local environment (Render-specific checks skipped)")
    
    # Check memory usage of key packages
    try:
        import psutil
        memory = psutil.virtual_memory()
        print(f"   ℹ️  Available memory: {memory.available / (1024**3):.1f} GB")
        
        if memory.available < 1 * (1024**3):  # Less than 1GB
            print("   ⚠️  Low memory environment detected")
        else:
            print("   ✅ Sufficient memory available")
    except ImportError:
        print("   ℹ️  psutil not available for memory check")
    
    return True

def main():
    """Run all compatibility checks"""
    print("🔍 StockLift Comprehensive Compatibility Check")
    print("=" * 50)
    
    checks = [
        ("Python Version", check_python_version),
        ("Package Imports", check_package_imports),
        ("TensorFlow", check_tensorflow_compatibility),
        ("Flask App", check_flask_app),
        ("Directories", check_directories),
        ("Model Files", check_model_files),
        ("Render Compatibility", check_render_compatibility),
    ]
    
    results = []
    
    for check_name, check_func in checks:
        try:
            result = check_func()
            results.append((check_name, result))
        except Exception as e:
            print(f"   ❌ {check_name} check failed: {e}")
            results.append((check_name, False))
    
    print("\n" + "=" * 50)
    print("📊 Compatibility Summary:")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for check_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"   {status} {check_name}")
    
    print(f"\n🎯 Overall: {passed}/{total} checks passed")
    
    if passed == total:
        print("🎉 All compatibility checks passed! Ready for deployment.")
        return True
    else:
        print("⚠️  Some compatibility issues found. Please review above.")
        return False

if __name__ == "__main__":
    import os
    success = main()
    sys.exit(0 if success else 1) 