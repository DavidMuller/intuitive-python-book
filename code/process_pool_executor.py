import concurrent.futures

def multiply(a, b):
    value = a * b
    print(f"{a} * {b} = {value}")

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for i in range(5):
            executor.submit(multiply, a=i, b=i)
