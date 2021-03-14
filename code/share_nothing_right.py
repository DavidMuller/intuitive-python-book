from concurrent.futures import as_completed, ThreadPoolExecutor

def get_elements():
    return ["a", "b", "c"]

if __name__ == "__main__":
    with ThreadPoolExecutor() as executor:
        final_output = []
        future_1 = executor.submit(get_elements)
        future_2 = executor.submit(get_elements)

        for future in as_completed([future_1, future_2]):
            final_output += future.result()
        print(final_output)
