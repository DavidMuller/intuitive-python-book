import concurrent.futures
import time
from urllib import request

def get_info():
    request.urlopen("https://example.com", timeout=30).read()

def run_comparison():
    start_serial = time.time()
    for _ in range(25):
        get_info()
    elapsed_serial = time.time() - start_serial
    print(f"Serial execution took {elapsed_serial} seconds")

    start_threaded = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for _ in range(25):
            executor.submit(get_info)
    elapsed_threaded = time.time() - start_threaded
    print(f"Threaded execution took {elapsed_threaded} seconds")

if __name__ == "__main__":
    run_comparison()
