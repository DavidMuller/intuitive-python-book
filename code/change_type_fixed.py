from typing import Optional

def foo(value: int):
    output: Optional[str]
    if value > 1:
        output = "big"
    else:
        output = None

    print(output)
