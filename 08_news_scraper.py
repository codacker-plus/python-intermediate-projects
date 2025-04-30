# news_scraper.py
import requests
import csv
from bs4 import BeautifulSoup

def scrape_news(url):
    """Scrape news headlines from a website and save to CSV."""
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to access {url}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all('h2')  # Adjust based on website structure

        with open('news.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Headline'])

            for headline in headlines:
                text = headline.get_text().strip()
                if text:
                    writer.writerow([text])
                    print(text)

        print("News saved to news.csv")

    except requests.RequestException as e:
        print(f"Error: {e}")

def news_scraper():
    """Main function for news scraper."""
    print("News Scraper")
    while True:
        url = input("Enter news website URL (e.g., https://example.com): ")
        if not url.startswith('http'):
            url = 'https://' + url

        scrape_news(url)

        again = input("Scrape another website? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    news_scraper()
