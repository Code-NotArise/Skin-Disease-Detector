#!/usr/bin/env python3
"""
Setup script for Skin Disease Detector Django project.
This script helps with initial project setup and configuration.
"""

import os
import sys
import subprocess
import secrets

def run_command(command, description):
    """Run a shell command and handle errors."""
    print(f"🚀 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed with error:")
        print(f"Error: {e.stderr}")
        return False

def create_env_file():
    """Create .env file from .env.example with generated secret key."""
    if os.path.exists('.env'):
        print("ℹ️  .env file already exists. Skipping creation.")
        return True
        
    if not os.path.exists('.env.example'):
        print("❌ .env.example file not found. Please create it first.")
        return False
        
    # Generate a secure secret key
    secret_key = secrets.token_urlsafe(50)
    
    # Read the example file
    with open('.env.example', 'r') as example_file:
        env_content = example_file.read()
    
    # Replace placeholder with generated secret key
    env_content = env_content.replace('your-secure-secret-key-here', secret_key)
    
    # Write the new .env file
    with open('.env', 'w') as env_file:
        env_file.write(env_content)
    
    print("✅ .env file created with generated secret key")
    print("⚠️  Please edit .env file to add your database credentials and Roboflow API key")
    return True

def main():
    """Main setup function."""
    print("=" * 60)
    print("🩺 Skin Disease Detector - Setup Script")
    print("=" * 60)
    
    # Check if Python is available
    if not run_command("python --version", "Checking Python installation"):
        print("❌ Python is not installed or not in PATH")
        return False
    
    # Create virtual environment
    if not os.path.exists('venv'):
        if not run_command("python -m venv venv", "Creating virtual environment"):
            return False
    else:
        print("ℹ️  Virtual environment already exists. Skipping creation.")
    
    # Install dependencies
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        return False
    
    # Create .env file
    if not create_env_file():
        return False
    
    print("\n" + "=" * 60)
    print("✅ Setup completed successfully!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Edit the .env file with your database credentials")
    print("2. Edit the .env file with your Roboflow API key")
    print("3. Run migrations: python manage.py migrate")
    print("4. Create superuser: python manage.py createsuperuser (optional)")
    print("5. Start server: python manage.py runserver")
    print("\nFor detailed instructions, see README.md")
    
    return True

if __name__ == "__main__":
    if main():
        sys.exit(0)
    else:
        sys.exit(1)
