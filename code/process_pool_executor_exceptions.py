import concurrent.futures

def multiply(a, b):
    if a == 2:
        raise ValueError("Oops, a = 2")
    return a * b

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = []
        for i in range(5):
            future = executor.submit(multiply, a=i, b=i)
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            try:
                print(future.result())
            except ValueError:
                print("Caught a ValueError")
