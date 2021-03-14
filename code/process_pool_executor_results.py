import concurrent.futures

def multiply(a, b):
    return a * b

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = []
        for i in range(5):
            future = executor.submit(multiply, a=i, b=i)
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            print(future.result())
