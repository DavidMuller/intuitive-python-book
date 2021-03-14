import pickle

class Snack:
    def __init__(self):
        self.cookie = "Oreo"

snack_dumped = pickle.dumps(Snack())

class Snack:
    def __init__(self):
        self.cookie = "Oreo"
        self.drink = "milk"

snack_loaded = pickle.loads(snack_dumped)
print(snack_loaded.drink)
