from data.const import start_url_jp

import requests
from bs4 import BeautifulSoup


def fetch_page(url):
    response = requests.get(url)

    if response.status_code == 200:
        page_contents = BeautifulSoup(response.content, "html.parser")
        return page_contents
    else:
        print(f"Failed to retrive the page. Status code : {response.status_code}")
        return None


def get_title(soup):
    title = soup.find("h1", {"id": "firstHeading"}).get_text()
    print(title)
    return title


def get_article(soup):
    pass
