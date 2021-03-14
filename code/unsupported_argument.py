object_info = {
    "123": {"description": "example object"},
    "456": {"description": "another example object"},
}

def print_object_info(object_id: str):
    info = object_info.get(object_id, default=f"{object_id} not found")
    print(info)

print_object_info(this_is_not_an_argument="oops")
