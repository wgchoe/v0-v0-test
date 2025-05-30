# review_wiki_doc.py
# This script uses Selenium to open a specific URL in the Chrome browser for review.

# Before running this script, you need to:
# 1. Install Selenium:
#    Open your terminal or command prompt and run: pip install selenium
#
# 2. Install ChromeDriver:
#    - Download the ChromeDriver version that matches your Chrome browser version.
#      Find it at: https://chromedriver.chromium.org/downloads
#    - Ensure ChromeDriver is in your system's PATH, or provide the explicit path to it in the script.
#
# 3. Update the placeholder URL:
#    - Replace 'YOUR_DOCUMENT_URL_HERE' with the actual URL of the document you want to review.

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By # Though not used for navigation, good to have for future interaction
from selenium.webdriver.chrome.options import Options as ChromeOptions

# Placeholder URL - replace with the actual URL of the document
DOCUMENT_URL = "YOUR_DOCUMENT_URL_HERE"
# Example: DOCUMENT_URL = "https://internal.wiki.example.com/Task_mining_recording_data_collection_guide_v3.0"

# Optional: Path to your ChromeDriver executable
# If ChromeDriver is not in your PATH, uncomment and set the path below.
# CHROME_DRIVER_PATH = "C:/path/to/your/chromedriver.exe" # Example for Windows
# CHROME_DRIVER_PATH = "/usr/local/bin/chromedriver"      # Example for macOS/Linux

def review_document(url):
    """
    Opens the specified URL in Chrome for a brief review period.
    """
    webdriver_service = None
    driver = None  # Initialize driver to None for cleanup in finally block

    try:
        print(f"Attempting to open URL: {url}")

        # --- Initialize Chrome WebDriver ---
        chrome_options = ChromeOptions()
        # chrome_options.add_argument("--headless") # Uncomment if you don't want the browser UI
        # chrome_options.add_argument("--disable-gpu") # Recommended for headless mode

        # Check if CHROME_DRIVER_PATH is defined and use it
        try:
            # This global check is a bit indirect, but works for this script structure
            if 'CHROME_DRIVER_PATH' in globals() and CHROME_DRIVER_PATH:
                webdriver_service = ChromeService(executable_path=CHROME_DRIVER_PATH)
                print(f"Using ChromeDriver from specified path: {CHROME_DRIVER_PATH}")
            else:
                # If CHROME_DRIVER_PATH is not set, Selenium will try to find ChromeDriver in PATH
                webdriver_service = ChromeService()
                print("Using ChromeDriver from system PATH.")
            driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
        except Exception as e:
            print(f"Error initializing ChromeDriver: {e}")
            print("Please ensure ChromeDriver is installed and its path is correctly configured.")
            print("You can download it from: https://chromedriver.chromium.org/downloads")
            print("If it's not in PATH, set the CHROME_DRIVER_PATH variable in this script.")
            return

        # Open the URL
        driver.get(url)
        print(f"Successfully opened URL. The document will be displayed for 10 seconds.")

        # Wait for the user to "review" the document
        time.sleep(10)

        print("Review time finished.")

    except Exception as e:
        print(f"An error occurred during browser automation: {e}")
        if "YOUR_DOCUMENT_URL_HERE" in url:
            print("Remember to replace 'YOUR_DOCUMENT_URL_HERE' with the actual document URL.")

    finally:
        if driver:
            print("Closing the browser...")
            driver.quit()
            print("Browser closed.")

if __name__ == "__main__":
    if DOCUMENT_URL == "YOUR_DOCUMENT_URL_HERE":
        print("--------------------------------------------------------------------")
        print("SCRIPT NOT RUN: Please update the DOCUMENT_URL variable in the script")
        print("with the actual URL of the 'Task mining recording data collection guide v3.0'")
        print("or any other document you wish to review.")
        print("--------------------------------------------------------------------")
    else:
        print("--------------------------------------------------------------------")
        print("Starting the document review script...")
        print("Ensure you have Selenium and ChromeDriver installed.")
        print("--------------------------------------------------------------------")
        review_document(DOCUMENT_URL)
