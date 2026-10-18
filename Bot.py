import os
from github import Github
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# ---------------------------------------------------------------------------
# 1. Configuration & Authentication
# ---------------------------------------------------------------------------
# GitHub Personal Access Token and Repository setup
GITHUB_TOKEN = "ghp_kMXNSAB5MgE51YIkxBIRbsAsOMUwSn1KVkry"
REPO_NAME = "davidsonofcristosyhwh-netizen/Firstab"

# Authenticate with the GitHub API
gh = Github(GITHUB_TOKEN)
repo = gh.get_repo(REPO_NAME)
print(f"Connected to repository: {repo.full_name}")

# ---------------------------------------------------------------------------
# 2. Selenium Headless Browser Configuration
# ---------------------------------------------------------------------------
# Configure Chrome options for running headlessly inside Codespaces
chrome_options = Options()
chrome_options.add_argument("--headless=new")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# ---------------------------------------------------------------------------
# 3. Web Scraping Execution
# ---------------------------------------------------------------------------
try:
    url = "https://example.com"
    print(f"Navigating to {url}...")
    driver.get(url)

    # Example task: Extract page title
    page_title = driver.title
    print(f"Page Title: {page_title}")

    # Add your specific web-scraping logic here

finally:
    driver.quit()
    print("Browser closed successfully.")
