import subprocess

with open("example.txt", mode="w") as f:
    contents = "example\ntext\nfile"
    f.write(contents)

with open("example.txt", mode="r") as f:
    result = subprocess.run(
        ["grep", "l"], stdin=f, capture_output=True, check=True
    )

stdout_str = result.stdout.decode("utf-8").strip()
print(stdout_str)
