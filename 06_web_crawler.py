# web_crawler.py
import requests
from bs4 import BeautifulSoup

def crawl_website(url):
    """Crawl a website and extract all links."""
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to access {url}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        
        print(f"Links found on {url}:")
        for link in links:
            href = link.get('href')
            if href:
                print(href)

    except requests.RequestException as e:
        print(f"Error: {e}")

def web_crawler():
    """Main function for web crawler."""
    print("Simple Web Crawler")
    while True:
        url = input("Enter website URL (e.g., https://example.com): ")
        if not url.startswith('http'):
            url = 'https://' + url

        crawl_website(url)

        again = input("Crawl another website? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    web_crawler()
