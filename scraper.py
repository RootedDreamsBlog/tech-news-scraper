import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_tech_trends():
    url = "https://news.ycombinator.com/"

    # 1. Identify yourself (Good practice)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"
    }

    print(f"Fetching data from {url}...")
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"❌ Failed to reach site. Status: {response.status_code}")
        return

    # 2. Parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # 3. Target the story titles (found in <span> with class 'titleline')
    articles = soup.find_all('span', class_='titleline')

    scraped_data = []

    for article in articles:
        link_tag = article.find('a')
        title = link_tag.string
        link = link_tag.get('href')

        scraped_data.append({
            "title": title,
            "link": link,
            "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    # 4. Save to CSV
    filename = "tech_trends_2026.csv"
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "link", "scraped_at"])
        writer.writeheader()
        writer.writerows(scraped_data)

    print(f"Success! Saved {len(scraped_data)} trends to {filename}")

if __name__ == "__main__":
    scrape_tech_trends()