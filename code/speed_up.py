import concurrent.futures
import time
from urllib import request

def get_info():  # <label id="code.speed_up.get_info"/>
    request.urlopen("https://example.com").read()

def run_comparison():
    start_serial = time.time()
    for _ in range(25):  # <label id="code.speed_up.serial_start"/>
        get_info()  # <label id="code.speed_up.serial_end"/>
    elapsed_serial = time.time() - start_serial
    print(f"Serial execution took {elapsed_serial} seconds")

    start_threaded = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:  # <label id="code.speed_up.threaded_start"/>
        for _ in range(25):
            executor.submit(get_info)  # <label id="code.speed_up.threaded_end"/>
    elapsed_threaded = time.time() - start_threaded
    print(f"Threaded execution took {elapsed_threaded} seconds")

if __name__ == "__main__":
    run_comparison()
