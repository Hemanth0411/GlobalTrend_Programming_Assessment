import requests
from requests.exceptions import HTTPError, Timeout, RequestException


def fetch_content(urls, max_retries=3):
  results = {}
  for url in urls:
    attempts = 0
    while attempts < max_retries:
      try:
        response = requests.get(url, timeout=6)
        response.raise_for_status()
        results[url] = response.content
        break
      except HTTPError as e:
        print(f"HTTP error while fetching {url}: {e}")
      except Timeout as e:
        print(f"Timeout error while fetching {url}: {e}")
      except RequestException as e:
        print(f"Request error while fetching {url}: {e}")
      attempts += 1
      print(f"Retrying.. ({attempts}/{max_retries})")

      if attempts == max_retries:
        print(f"Failed to fetch content from {url} after {max_retries} attempts")
        results[url] = None
  return results

urls_list = [
    "https://www.google.com",
    "https://www.example.com/this-page-does-not-exist",
    "https://xkcd.com/353/"
]

fetched_content = fetch_content(urls_list)
for link, data in fetched_content.items():
  if data:
    print(f"\nContent from {link}:\n{data[:100]}\n")
  else:
    print(f"No content fetched from {link}")
