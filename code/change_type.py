def print_details(level: int):
    user_object = {
        "id": "2",
        "name": "David",
        "favorite_color": "blue",
    }
    if level <= 1:
        keys = ["id", "name"]  # <label id="code.change_type.list"/>
    else:
        keys = ("id", "name", "favorite_color")  # <label id="code.change_type.tuple"/>

    print(" ".join(user_object[k] for k in keys))
