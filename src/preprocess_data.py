import os
import sys
import pickle
import time

# project_root_path = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(project_root_path)

import my_library.load_input_data as input_loader
from my_library.data_preprocessor import DataPreprocessor

data_path = input("Enter the path for the data file: ")
dictionary_path = input("Enter the path for the dictionary file(.pkl): ")
preprocessed_data_path = input("Enter the path to save the preprocessed data(.pkl): ")

labeled = input("Enter if the data is labeled (Y/N): ")

start_time = time.perf_counter()

with open(dictionary_path, "rb") as f:
    dictionary = pickle.load(f)

if labeled == "Y":
    sentence_arrays = input_loader.load(data_path)
    data_preprocessor = DataPreprocessor(sentence_arrays, dictionary)
    data_preprocessor.preprocess_data_and_label()
else:
    sentence_arrays = input_loader.load_raw(data_path)
    data_preprocessor = DataPreprocessor(sentence_arrays, dictionary)
    data_preprocessor.preprocess_data() 

data_preprocessor.dump(preprocessed_data_path)

end_time = time.perf_counter()
print("処理時間: ", "{:.2f}".format((end_time - start_time)/60))