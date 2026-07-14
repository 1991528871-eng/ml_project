# 園田夏菜・J4260438  運用フェーズ
# models/best_model.pkl を読み込み，
# 前処理された data/data_preprocessed.pkl を用いて識別を行うように．
import os
import pickle
import src.my_library.load_input_data as input_loader

project_root_path = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(project_root_path, "models", "best_model.pkl")
preprocessed_data_path = os.path.join(project_root_path, "data", "data_processed.pkl")
data_path = os.path.join(project_root_path, "data", "data.txt")

with open(model_path, "rb") as f:
    predictor = pickle.load(f)
with open(preprocessed_data_path, "rb") as f:
    preprocessed_data, _ = pickle.load(f)

print(preprocessed_data[1:10])  # 前処理したデータを一部表示
sentence_array = input_loader.load_raw(data_path)
predictions = predictor.predict(preprocessed_data)

for i in range(len(predictions)):
    print(sentence_array[i], predictions[i])

file_path = ../data/consequence
with open(file_path, "w") as f:
    string = ""
    for i in range(len(predictions)):
        string = string + str(sentence_array[i]) + str(predicions[i]) + "\n"
    #stirng = string + str(sentence_array)
    #pickle.dump(, f)
    print(string, file = f)



# def dump(self, file_path):
#         with open(file_path, "wb") as f:
#             pickle.dump((self.X, self.Y), f)