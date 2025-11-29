# 🤖Anime News Tracker Discord Bot🤖
A Python bot that scrapes Anime News Network for keywords and posts real-time alerts to Discord via Webhooks. Tracks specific announcements from the Anime News Network (ANN) website. It automates the process of finding relevant news—such as sequel announcements, film releases, or manga updates. It delivers real-time, clean alerts directly to a designated Discord channel via a Webhook.

⚡Features:

🕸️Targeted Scraping: Uses BeautifulSoup to precisely extract headlines and links from the ANN news page structure.

🔍Keyword Filtering: Only posts articles that match defined keywords (e.g., "Season 2," "Sequel," "Film"), minimizing noise.

🔔Real-time Alerts: Leverages Discord Webhooks for instant, formatted notifications.

🔗Clean Output: Automatically resolves relative links to full, clickable URLs.

Here's what alerts look like in a Discord channel when the bot finds relevant articles:

![Discord Bot Alert Screenshot](./assets/AnimeNewsBot.png)

Tech Stack: 

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="40"/>
  <img src="https://cdn.prod.website-files.com/6257adef93867e50d84d30e2/66e3d80db9971f10a9757c99_Symbol.svg" width="40"/>
</p>

Follow these steps to set up and run your bot locally:

1. 📋Prerequisites: Make sure Python 3.x is installed and that you have a Discord server where you can create a Webhook.

2. ⬇️Installation: Clone this repository and install the necessary dependencies using the requirements.txt file:

      ```bash
      git clone animenewsbot
      cd animenewsbot
      pip install -r requirements.txt

3. 🔑Configuration: Get your Discord webhook. In Discord, navigate to your desired Channel Settings → Integrations → Webhooks → Copy the Webhook URL.

4. Open the anime_news_bot.py file and replace the placeholder with your actual URL:
     ```bash
     WEBHOOK_URL = ""

6. Modify the KEYWORDS list to include announcements you are most interested in.

7. ▶️Execution: Run the script from your terminal:
     ```bash
     python anime_news_bot.py
