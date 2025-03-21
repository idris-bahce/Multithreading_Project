import threading
import requests
import time

urls = [
    'https://www.google.com',
    'https://www.github.com',
    'https://www.example.com',
    'https://www.invalidurlfoobar.com',
    'https://www.stackoverflow.com'
    ]

def check_url(url):
    try:
        response = requests.get(url, timeout=5)
        print(f"{url} - Status: {response.status_code}")
    except Exception as e:
        print(f"{url} - Error: {str(e)}")

def sequential_check():
    start = time.time()
    
    for url in urls:
        check_url(url)
    
    print(f"Sequencial time: {time.time() - start:.2f}s\n")

def threaded_check():
    start = time.time()
    threads = []

    for url in urls:
        thread = threading.Thread(target=check_url, args=(url, ))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"Threaded time: {time.time() - start:.2f}s")

print("Sequential Execution:")
sequential_check()

print("Threaded Execution:")
threaded_check()