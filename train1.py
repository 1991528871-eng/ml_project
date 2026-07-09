# 柚木翔太・J4260079  学習フェーズ 1
# 学習したモデルを models/models1/ に出力するように．
import os
import sys
import src.my_library.trainer1 as trainer
preprocessed_train_data_path=input("Enter the path for the preprocessed data:")
model_dump_path_base=input("Enter the path for the directory to save the models:")
t=trainer.Trainer()
X,y=t.load_data(preprocessed_train_data_path)
hyperparameters=[0.1,1,10,100,1000]
for h in hyperparameters:
    model_dump_path=os.path.join(model_dump_path_base,"SVM_"+str(h)+".pkl")
    print(model_dump_path)
    t.train_SVM(h,X,y)
    t.dump_model(model_dump_path)