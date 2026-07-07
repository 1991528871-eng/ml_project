import os
import sys

import pickle
from janome.tokenizer import Tokenizer

def load1(dictionary_path):
    dic = {}
    with open(dictionary_path, "r", encoding = "utf-8") as f:
        lines = f.read()
        for l in lines.split("\n"):
            entry = l.split("\t")
            if len(entry) < 2:  # 空行をパス
                continue
            key = entry[0]
            value = 0 if entry[1] == "e" else (1 if entry[1] == "p" else -1)
            dic[key] = [[[], value]]  # dictionary2 と同じ形にする
    return dic

def load2(dictionary_path):
    dic = {}
    t = Tokenizer()
    with open(dictionary_path, "r", encoding = "utf-8") as f:
        lines = f.read()
        for l in lines.split("\n"):
            entry = l.split("\t")
            if len(entry) < 2:  # 空行をパス
                continue
            entry[1] = entry[1].replace(" ", "")
            entry[1] = [ token.base_form for token in t.tokenize(entry[1]) ]
            # 活用に影響されないように，すべて原形に直す
            key = entry[1][0]
            value = -1 if entry[0].split("（")[0] == "ネガ" else 1
            if not(key in dic):
                dic[key] = []
            dic[key].append([ entry[1][1:], value ])
            # 1つ目の単語を key にして，
            # その後続く単語列とその極性を配列にして value として登録する
    return dic

dictionary_path = input("Enter the path for the first dictionary: ")
loaded_dictionary_path = input("Enter the path to save the loaded dictionary: ")
with open(loaded_dictionary_path, "wb") as f:
    pickle.dump(load1(dictionary_path), f)

dictionary_path = input("Enter the path for the second dictionary: ")
loaded_dictionary_path = input("Enter the path to save the loaded dictionary: ")
with open(loaded_dictionary_path, "wb") as f:
    pickle.dump(load2(dictionary_path), f)
