import concurrent.futures

def multiply(a, b):
    value = a * b
    print(f"{a} * {b} = {value}")

with concurrent.futures.ProcessPoolExecutor() as executor:
    for i in range(5):
        executor.submit(multiply, a=i, b=i)
