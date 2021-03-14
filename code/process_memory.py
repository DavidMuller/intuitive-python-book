import concurrent.futures

a_list = []  # <label id="code.process_memory.a_list"/>


def append_to_a_list():  # <label id="code.process_memory.append_to_a_list-fcn"/>
    a_list.append(1)

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.submit(append_to_a_list)
        executor.submit(append_to_a_list)
        executor.submit(append_to_a_list)

    print(a_list)
