import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import time
from requests.exceptions import RequestException

sections = {
    "https://www.regione.puglia.it/web/ricerca-e-relazioni-internazionali/agenda-eventi": "[Evento]",
    "https://www.regione.puglia.it/web/ricerca-e-relazioni-internazionali/elenco-notizie": "[Notizia]",
    "https://www.regione.puglia.it/web/ricerca-e-relazioni-internazionali/elenco-bandi": "[Bando]"
}

def fetch_with_retry(url, retries=3, delay=5):
    for attempt in range(retries):
        try:
            print(f"Tentativo {attempt+1} per URL: {url}")
            return requests.get(url, timeout=10)
        except RequestException as e:
            print(f"Errore: {e}")
            time.sleep(delay)
    raise Exception(f"Impossibile connettersi a {url} dopo {retries} tentativi.")

def extract_items(url, label):
    items = []
    resp = fetch_with_retry(url)
    soup = BeautifulSoup(resp.content, "html.parser")
    articles = soup.select("div.card-agenda-one")[:5]
    for a in articles:
        title_tag = a.select_one("a")
        title = a.select('p.title-text')[0].contents[0]
        link = a.select('a.card-agenda-image')[0]['href']
        date = a.select('div.date')[0].get_text(strip=True)
        items.append({
            "title": f"{label} {title}",
            "link": link,
            "date": date,
        })
    return items

all_items = []
for url, label in sections.items():
    all_items.extend(extract_items(url, label))

all_items = sorted(all_items, key=lambda x: x["date"])

rss = ET.Element("rss", version="2.0")
channel = ET.SubElement(rss, "channel")
ET.SubElement(channel, "title").text = "Regione Puglia - Feed Unificato"
ET.SubElement(channel, "link").text = "https://www.regione.puglia.it/"
ET.SubElement(channel, "description").text = "Notizie, Eventi e Bandi dalla Regione Puglia"

for item in all_items:
    i = ET.SubElement(channel, "item")
    ET.SubElement(i, "title").text = item["title"]
    ET.SubElement(i, "link").text = item["link"]
    ET.SubElement(i, "pubDate").text = item["date"]

tree = ET.ElementTree(rss)
tree.write("feed.xml", encoding="utf-8", xml_declaration=True)
