from data.const import start_url_jp

import requests
from bs4 import BeautifulSoup

response = requests.get(start_url_jp)

if response.status_code == 200:
    page_content = response.content
else:
    print(f"Failed to retrive the page. Status code : {response.status_code}")
