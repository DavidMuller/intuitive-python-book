files = [
    ("Jack", "hill.txt"),
    ("Jill", "water.txt"),
    ("Jack", "crown.txt"),
]

owner_to_files = {}
for owner, file_name in files:
    if owner not in owner_to_files:
        owner_to_files[owner] = []
    owner_to_files[owner].append(file_name)

print(owner_to_files)
