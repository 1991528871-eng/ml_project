# 石谷良祐・J4261071  評価フェーズ
# models/models1/ & models/moedls2/ に入ったすべてのモデルの評価を行い，
# 最良と思われるモデルを models/best_model.pkl として出力するように．

import os
import sys
import pickle
import src.my_library.validator as validator

def find_best_model(models_paths, data_path):
    """
    Args:
        models_paths (list of str): モデルが格納されたディレクトリのパスのリスト（例: [models_1, models_2]）
        data_path (str): 前処理済み検証データのパス
    """
    v = validator.Validator()
    v.load_data(data_path)

    best_accuracy = 0
    best_model_file_path = None

    for models_path in models_paths:
        for model_file in os.listdir(models_path):
            model_file_path = os.path.join(models_path, model_file)
            v.load_model(model_file_path)
            accuracy, precision, recall = v.evaluate_model()
            print(f"Evaluating {model_file_path}:")
            print(f"Accuracy: {accuracy}")
            print(f"Precision: {precision}")
            print(f"Recall: {recall}")

            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_model_file_path = model_file_path

    if best_model_file_path is not None:
        best_model_file_path_dest = os.path.join(os.path.dirname(models_paths[0].rstrip(os.sep)), 'best_model.pkl')
        v.load_model(best_model_file_path)
        with open(best_model_dest, 'wb') as f:
            pickle.dump(v.model, f)
        print(f"The best model is saved as 'best_model.pkl' with accuracy: {best_accuracy}")


data_path = input("Enter the path for the preprocessed validation data:")
models_path_1 = input("Enter the path for the first models directory:")
models_path_2 = input("Enter the path for the second models directory:")
find_best_model([models_path_1, models_path_2], data_path)