#!/usr/bin/env python3
"""
ADGM Corporate Agent - Main Entry Point
Run this script to launch the ADGM Corporate Agent application
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def main():
    """Main entry point for the ADGM Corporate Agent"""
    try:
        from adgm_corporate_agent import main as app_main
        print("🚀 Starting ADGM Corporate Agent - Professional Edition...")
        print("📱 The app will open in your browser at http://127.0.0.1:7862")
        app_main()
    except ImportError as e:
        print(f"❌ Error importing ADGM Corporate Agent: {e}")
        print("💡 Make sure you're running from the project root directory")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
