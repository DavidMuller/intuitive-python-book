import pickle

l = ["a", "b", None, "c"]

dumped_l = pickle.dumps(l)
print(dumped_l)

loaded_l = pickle.loads(dumped_l)
print(loaded_l)
