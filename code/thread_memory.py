import concurrent.futures

a_list = []


def append_to_a_list():
    a_list.append(1)

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # note this is race condition prone code suitable only
        # for illustrative purposes
        executor.submit(append_to_a_list)
        executor.submit(append_to_a_list)
        executor.submit(append_to_a_list)

    print(a_list)
