import pickle

with open("data/data_preprocessed.pkl", "rb") as f:
    pairs = pickle.load(f)

print(pairs)