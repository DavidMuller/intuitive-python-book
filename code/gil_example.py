import time

def do_work():
    countdown = 75000
    while countdown > 0:
        countdown -= 1

def run_comparision():
    start_serial = time.time()
    for _ in range(1000):
        do_work()
    elapsed_serial = time.time() - start_serial
    print(f"Serial execution took {elapsed_serial} seconds")

if __name__ == "__main__":
    run_comparision()
