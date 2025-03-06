import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Initialize Selenium WebDriver
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Automatically set up ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open Nitter search page
nitter_url = "https://nitter.net/search?q=AI&f=tweets"
driver.get(nitter_url)

# Wait for tweets to load
time.sleep(5)

# Scrape tweets
tweets = driver.find_elements(By.CSS_SELECTOR, "div.tweet-content")

tweet_data = []

for tweet in tweets:
    original_text = tweet.text.strip()
    if original_text:
        tweet_data.append({"text": original_text})

# Close the browser
driver.quit()

# Send scraped tweets to sentiment analysis API
api_url = "http://127.0.0.1:5000/analyze"
for tweet in tweet_data:
    response = requests.post(api_url, json=tweet)
    print(response.json())  # Print sentiment analysis results
