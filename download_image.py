import requests
from bs4 import BeautifulSoup
import json
import os
from urllib.parse import quote
from tqdm import tqdm

# Baca data dari movies.json
with open("movies.json", "r", encoding="utf-8") as f:
    movies = json.load(f)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def search_wikipedia_page(title):
    search_url = f"https://en.wikipedia.org/w/index.php?search={quote(title)}+film"
    resp = requests.get(search_url, headers=HEADERS)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "html.parser")
        result = soup.find("div", class_="mw-search-result-heading")
        if result:
            return "https://en.wikipedia.org" + result.find("a")["href"]
        else:
            # Kalau langsung redirect ke halaman film
            if soup.find("table", class_="infobox vevent"):
                return resp.url
    return None

def get_poster_url(wiki_url):
    resp = requests.get(wiki_url, headers=HEADERS)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "html.parser")
        infobox = soup.find("table", class_="infobox vevent")
        if infobox:
            img_tag = infobox.find("img")
            if img_tag:
                return "https:" + img_tag["src"]
    return None

def download_image(url, save_path):
    try:
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code == 200:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, "wb") as f:
                f.write(resp.content)
            return True
    except Exception as e:
        print(f"[❌] Error downloading {url}: {e}")
    return False

# Proses utama
for movie in tqdm(movies, desc="Processing Movies"):
    title = movie["name"]
    img_path = movie["imgPath"]

    wiki_url = search_wikipedia_page(title)
    if not wiki_url:
        print(f"[⚠️] Wikipedia page not found for: {title}")
        continue

    poster_url = get_poster_url(wiki_url)
    if not poster_url:
        print(f"[⚠️] Poster not found for: {title}")
        continue

    if download_image(poster_url, img_path):
        print(f"[✅] Downloaded: {img_path}")
    else:
        print(f"[❌] Failed to download image from: {poster_url}")
