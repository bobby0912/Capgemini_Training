import threading
import os
import requests

def fetch_url(sites,site, results):
    response = requests.get(sites[site])
    html_content = response.text  # Get the HTML content as a string
    results.append(f"Fetched {sites[site]}:\n{html_content}\n")
    with open(f"{site}.html", "w", encoding="utf-8", errors="replace") as file:
        file.write(html_content)

    # file=open(f"{site}.html",'w')
    # file.write(html_content)

sites = {
    "youtube":"https://www.youtube.com/",
    "example":"https://example.com",
    "python":"https://www.python.org",
    "github":"https://www.github.com"
}

threads = []
results = []

for site in sites.keys():
    thread = threading.Thread(target=fetch_url, args=(sites,site, results))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

# Display results in the console after all threads are done
# for result in results:
#     print(result)

print("All URLs fetched")
