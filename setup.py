"""Setup script for Orion Voice Assistant"""
import os
import sys

def create_env_file():
    """Create a .env file if it doesn't exist"""
    if os.path.exists(".env"):
        print("✅ .env file already exists")
        return
    
    if not os.path.exists(".env.example"):
        print("❌ .env.example not found")
        return
    
    # Copy .env.example to .env
    with open(".env.example", "r") as example:
        with open(".env", "w") as env:
            env.write(example.read())
    
    print("✅ Created .env file from .env.example")
    print("⚠️  Please edit .env and add your API keys")

def create_directories():
    """Create necessary directories"""
    directories = ["logs", "cache"]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✅ Created {directory} directory")
        else:
            print(f"✅ {directory} directory already exists")

def check_dependencies():
    """Check if all required packages are installed"""
    print("\n📦 Checking dependencies...")
    
    required_packages = [
        "speech_recognition",
        "gtts",
        "pygame",
        "wikipedia",
        "google.generativeai",
        "dotenv"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package if package != "dotenv" else "dotenv")
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - NOT INSTALLED")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️  Missing packages: {', '.join(missing_packages)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("\n✅ All dependencies are installed!")
    return True

def main():
    """Run setup"""
    print("="*50)
    print("🚀 Orion Voice Assistant Setup")
    print("="*50)
    print()
    
    # Create directories
    print("📁 Creating directories...")
    create_directories()
    print()
    
    # Create .env file
    print("🔐 Setting up environment variables...")
    create_env_file()
    print()
    
    # Check dependencies
    all_installed = check_dependencies()
    
    print()
    print("="*50)
    if all_installed:
        print("✅ Setup complete! Run 'python main.py' to start Orion")
    else:
        print("⚠️  Setup incomplete. Install missing dependencies first.")
    print("="*50)

if __name__ == "__main__":
    main()
