from collections import defaultdict

files = [
    ("Jack", "hill.txt"),
    ("Jill", "water.txt"),
    ("Jack", "crown.txt"),
]

owner_to_files = defaultdict(list)
for owner, file_name in files:
    owner_to_files[owner].append(file_name)

print(owner_to_files)
