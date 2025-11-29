import requests
from bs4 import BeautifulSoup
import time

# Discord webhook URL for sending messages to the channel
WEBHOOK_URL = "" 
# Base URL for anime news
ANIME_NEWS_URL = "https://www.animenewsnetwork.com/news/"
# Keywords to filter relevant anime news articles
KEYWORDS = ["season 2", "sequel", "manga", "film", "announcement"] 

def send_discord_message(content):
    # Sends a message to Discord via webhook
    data = {"content": content}
    headers = {'User-Agent': 'AnimeNewsScraperBot/1.0'}
    try:
        response = requests.post(WEBHOOK_URL, json=data, headers=headers)
        response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to Discord: {e}")

def check_anime_news():
    # Scrapes anime news from Anime News Network and sends alerts for matching keywords
    BASE_URL = "https://www.animenewsnetwork.com"
    try:
        response = requests.get(BASE_URL + "/news/")
        response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        print(f"Error accessing URL: {e}")
        return
    soup = BeautifulSoup(response.text, "html.parser")
    news_items = soup.find_all('h3')
    for h3_tag in news_items:
        link_tag = h3_tag.find('a')
        if link_tag and link_tag.get("href"):
            text = link_tag.get_text(strip=True)
            relative_link = link_tag.get("href")
            full_link = BASE_URL + relative_link
            if any(keyword.lower() in text.lower() for keyword in KEYWORDS):
                message = f"🚨 **NEWS ALERT!** \n{text}\n🔗 {full_link}"
                send_discord_message(message)
                print(f"Sent: {text}")

if __name__ == "__main__":
    print("Anime News Bot is running...")
    check_anime_news()