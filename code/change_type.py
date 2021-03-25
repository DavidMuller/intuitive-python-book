def print_details(level: int):
    user_object = {
        "id": "2",
        "name": "David",
        "favorite_color": "blue",
    }
    if level <= 1:
        keys = ["id", "name"]
    else:
        keys = ("id", "name", "favorite_color")

    print(" ".join(user_object[k] for k in keys))
