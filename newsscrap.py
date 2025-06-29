# Python program to scrape headlines from BBC and save to a text file
import requests
from bs4 import BeautifulSoup

# Target BBC URL
URL = "https://www.bbc.com/"

# Set headers to avoid blocks
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

try:
    # Make GET request
    response = requests.get(URL, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Store extracted headlines
        headlines = []

        # Look for all <h3> tags (BBC uses these for many headlines)
        for tag in soup.find_all('h3'):
            text = tag.get_text(strip=True)
            if text and text not in headlines:
                headlines.append(text)

        # Save to a .txt file
        with open("bbc_headlines.txt", "w", encoding="utf-8") as f:
            for i, line in enumerate(headlines, start=1):
                f.write(f"{i}. {line}\n")

        print("Headlines successfully saved to 'bbc_headlines.txt'.")

    else:
        print(f" Failed to fetch BBC page. Status code: {response.status_code}")

except Exception as e:
    print(f"Error: {e}")
