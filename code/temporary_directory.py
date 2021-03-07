import os
from tempfile import TemporaryDirectory

with TemporaryDirectory() as tmp_d_path:
    print(tmp_d_path, os.path.isdir(tmp_d_path))

    example_txt_path = os.path.join(tmp_d_path, "example.txt")
    with open(example_txt_path, mode="w") as f:
        f.write("example contents")
    print(example_txt_path, os.path.exists(example_txt_path))

print(tmp_d_path, os.path.isdir(tmp_d_path))
print(example_txt_path, os.path.exists(example_txt_path))
