from concurrent.futures import ThreadPoolExecutor

def add_elements(a_list):
    a_list += ["a", "b", "c"]
    return a_list

if __name__ == "__main__":
    with ThreadPoolExecutor() as executor:
        # wrong: don't do the following
        shared_list = []
        executor.submit(add_elements, a_list=shared_list)
        executor.submit(add_elements, a_list=shared_list)
