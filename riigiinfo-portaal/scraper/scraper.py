## Esimene must katse
import os
import requests
from bs4 import BeautifulSoup
import pdfplumber
import sqlite3
from urllib.parse import urlparse
import re
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# ======= Konfiguratsioon =======
OUTPUT_DIR = "scraped_docs"
DB_FILE = "documents.db"
FAISS_INDEX_FILE = "embeddings.index"
CHUNK_SIZE = 300  # sõnade arv chunkis
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"  # tasuta, lightweight

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ======= SQLite Setup =======
conn = sqlite3.connect(DB_FILE)
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    source_url TEXT,
    category TEXT,
    chunk_index INTEGER,
    content_text TEXT
)
''')
conn.commit()

# ======= Faiss Setup =======
embedding_dim = 384  # all-MiniLM-L6-v2 dimensioon
if os.path.exists(FAISS_INDEX_FILE):
    index = faiss.read_index(FAISS_INDEX_FILE)
else:
    index = faiss.IndexFlatL2(embedding_dim)
embeddings_list = []

# ======= Helper Functions =======
def clean_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    for tag in soup(["script", "style", "header", "footer", "nav", "aside"]):
        tag.decompose()
    text = soup.get_text(separator="\n")
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    clean_text = "\n".join(lines)
    clean_text = re.sub(r"\n{2,}", "\n\n", clean_text)
    return clean_text

def chunk_text(text, chunk_size=CHUNK_SIZE):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

def fetch_html(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return clean_html(response.text)

def fetch_pdf(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    with open("temp.pdf", "wb") as f:
        f.write(response.content)
    text = ""
    with pdfplumber.open("temp.pdf") as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    os.remove("temp.pdf")
    return text

def get_content_from_url(url):
    if url.lower().endswith(".pdf"):
        return fetch_pdf(url)
    else:
        return fetch_html(url)

def save_to_db(title, url, category, chunks):
    for idx, chunk in enumerate(chunks):
        c.execute('''
            INSERT INTO documents (title, source_url, category, chunk_index, content_text)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, url, category, idx, chunk))
        conn.commit()
        # Loome embeddingu
        embedding_vector = model.encode(chunk).astype(np.float32)
        embeddings_list.append(embedding_vector)

# ======= Main Scraper Function =======
model = SentenceTransformer(EMBEDDING_MODEL_NAME)

def scrape_and_store(url, category="general"):
    print(f"Scraping: {url}")
    text_content = get_content_from_url(url)
    chunks = chunk_text(text_content)
    # Loo title failinime põhjal
    parsed_url = urlparse(url)
    title = parsed_url.netloc.replace(".", "_") + parsed_url.path.replace("/", "_")
    title = title.strip("_") or "document"
    save_to_db(title, url, category, chunks)
    print(f"Saved {len(chunks)} chunks for {url}")

    # Salvesta Faiss indeks
    if embeddings_list:
        embeddings_array = np.vstack(embeddings_list)
        index.add(embeddings_array)
        faiss.write_index(index, FAISS_INDEX_FILE)
        print(f"Faiss index updated, total vectors: {index.ntotal}")

# ======= Näidis kasutus =======
if __name__ == "__main__":
    urls_to_scrape = [
        "https://www.riigiteataja.ee/akt/129032021003",  # HTML
        # "https://www.example.ee/sample.pdf",           # PDF näide
    ]
    for url in urls_to_scrape:
        scrape_and_store(url, category="legal")
