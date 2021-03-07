import pickle

class Foo:
    def __init__(self):
        self.a = 1

foo_dumped = pickle.dumps(Foo())

class Foo:
    def __init__(self):
        self.a = 1
        self.b = 2

foo_loaded = pickle.loads(foo_dumped)
print(foo_loaded.b)
