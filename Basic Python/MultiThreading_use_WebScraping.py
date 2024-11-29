import threading
import requests
from bs4 import BeautifulSoup


urls = [

    'https://vegamovies.ai/',
    'https://hdhub4u.joburg/category/hollywood-movies/'
]

def fetch_Data(url):
    response =requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"Length of The Web Page WOrds are {len(soup.text)} of {url}")

threads = []
for url in urls:
    thread = threading.Thread(target=fetch_Data,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All data Fetched")