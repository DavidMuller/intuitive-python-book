import os
from tempfile import NamedTemporaryFile

with NamedTemporaryFile() as tmp_f:
    print(tmp_f.name, os.path.exists(tmp_f.name))

print(tmp_f.name, os.path.exists(tmp_f.name))
