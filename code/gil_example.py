# START_HIGHLIGHT
import concurrent.futures
# END_HIGHLIGHT
# START:serial
import time
# START:serial

def do_work():
    countdown = 75000
    while countdown > 0:
        countdown -= 1

start_serial = time.time()
for _ in range(1000):
    do_work()
elapsed_serial = time.time() - start_serial
print(f"Serial execution took {elapsed_serial} seconds")
# END:serial

# START_HIGHLIGHT
start_threaded = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    for _ in range(1000):
        executor.submit(do_work)
elapsed_threaded = time.time() - start_threaded
print(f"Threaded execution took {elapsed_threaded} seconds")
# END_HIGHLIGHT
