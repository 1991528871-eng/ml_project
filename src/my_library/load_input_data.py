def load(data_path):
    with open(data_path, "r", encoding = "utf-8") as f:
        lines = f.read().strip().split("\n")
    res = [ line.split("\t") for line in lines ]
    return res[1:]

def load_raw(data_path):
    with open(data_path, "r", encoding = "utf-8") as f:
        lines = f.read().strip().split("\n")
    return lines
