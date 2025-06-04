import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    texts = soup.find_all(['p', 'h1', 'h2', 'h3', 'li'])
    content = "\n".join([t.get_text(strip=True) for t in texts])
    return content

# Save scraped content to a file
if __name__ == "__main__":
    content = scrape_website("https://example.com")
    with open("site_content.txt", "w", encoding="utf-8") as f:
        f.write(content)
