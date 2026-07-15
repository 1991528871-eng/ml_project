# 米澤大雅・J4250453  学習フェーズ 2
# 学習したモデルを models/models2/ に出力するように．
import os
import sys
import src.my_library.trainer2 as trainer

preprocessed_train_data_path = input("Enter the path for the preprocessed data: ")
model_dump_path_base = input("Enter the path for the directory to save the models: ")

t = trainer.Trainer()
X, y = t.load_data(preprocessed_train_data_path)

# ロジスティック回帰のハイパーパラメータの候補
hyperparameters = [0.01, 0.1, 1, 10, 100]

for h in hyperparameters:
    # 保存ファイル名をSVMと区別するために変更
    model_dump_path = os.path.join(model_dump_path_base, "LogReg_" + str(h) + ".pkl")
    print("Training:", model_dump_path)
    
    t.train_LogisticRegression(h, X, y)
    t.dump_model(model_dump_path)
