import concurrent.futures

def get_elements():
    return ["a", "b", "c"]

with concurrent.futures.ThreadPoolExecutor() as executor:
    final_output = []
    future_1 = executor.submit(get_elements)
    future_2 = executor.submit(get_elements)

    for future in concurrent.futures.as_completed([future_1, future_2]):
        final_output += future.result()
    print(final_output)
