import os
import subprocess
from io import BytesIO
from tempfile import TemporaryDirectory
from urllib import request
from zipfile import ZipFile


def download_code(target_dir):
    """
    Downloads the book's raw source code from pragprog.com
    and stores it in target_dir.
    """
    code_url = "https://media.pragprog.com/titles/dmpython/code/dmpython-code.zip"
    with request.urlopen(code_url, timeout=30) as f:
        downloaded_zip_bytes = BytesIO(f.read())
        downloaded_zip_bytes.seek(0)
    with ZipFile(downloaded_zip_bytes) as downloaded_zip_bytes:
        downloaded_zip_bytes.extractall(target_dir)


def check_code_synced(source_dir):
    """
    Compares the contents of source_dir with the downloaded
    contents from pragprog.com. Raises an Exception if the
    two directories are not equivalent.
    """
    with TemporaryDirectory() as downloaded_code:
        download_code(target_dir=downloaded_code)
        subprocess.run(
            ["diff", "--recursive", source_dir, os.path.join(downloaded_code, "code")],
            check=True,
        )


if __name__ == "__main__":
    source_dir = os.path.join(os.environ["GITHUB_WORKSPACE"], "code")
    check_code_synced(source_dir=source_dir)
