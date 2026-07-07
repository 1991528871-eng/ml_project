import os
import sys
import pickle
import numpy as np

import my_library.count_statistics as counter

class DataPreprocessor:
    def __init__(self, sentences, dictionary):
        self.sentences = sentences
        self.dic = dictionary
        self.X = None
        self.Y = None
    
    def preprocess_data(self):
        X_list = [ counter.count_and_vectorize(sen, self.dic) for sen in self.sentences ]
        self.X = np.array(X_list)
    
    def preprocess_data_and_label(self):
        X_list = [ counter.count_and_vectorize(sen[0], self.dic) for sen in self.sentences ]
        Y_list = [ -1 if sen[4] == "0" else 1 for sen in self.sentences ]
        self.X, self.Y = np.array(X_list), np.array(Y_list)
    
    def dump(self, file_path):
        with open(file_path, "wb") as f:
            pickle.dump((self.X, self.Y), f)
