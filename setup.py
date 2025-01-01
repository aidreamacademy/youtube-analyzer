import os
import subprocess
import sys

def install_requirements():
    """Install required Python packages."""
    print("Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("All dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error installing dependencies. Please check your Python installation and try again.")
        sys.exit(1)

def setup_env():
    """Prompt user for API keys and save them to a .env file."""
    print("Welcome to YouTube Trend & Idea Analyzer Setup!")
    youtube_key = input("Enter your YouTube API key: ")
    anthropic_key = input("Enter your Anthropic API key: ")
    
    with open(".env", "w") as f:
        f.write(f"YOUTUBE_API_KEY={youtube_key}\n")
        f.write(f"ANTHROPIC_API_KEY={anthropic_key}\n")
    
    print("Setup complete! Your API keys have been saved to '.env'.")

def main():

    # Check if requirements.txt exists
    if not os.path.exists("requirements.txt"):
        print("Error: 'requirements.txt' not found. Make sure you're in the correct directory.")
        sys.exit(1)

    # Install dependencies
    install_requirements()
    
    # Set up environment variables
    if not os.path.exists(".env"):
        setup_env()
    else:
        print(".env file already exists. Skipping environment setup.")

if __name__ == "__main__":
    main()
