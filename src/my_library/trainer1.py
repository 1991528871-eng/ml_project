import sklearn.svm as SVM
import pickle
class Trainer:
    def __init__(self):
        self.model=None #モデルを格納するインスタンス変数を初期化
    def load_data(self,file_path):
        with open(file_path,'rb')asf:
        X,y=pickle.load(f)
        return X,y
    def dump_model(self,file_path):
        with open(file_path,'wb')asf:
            pickle.dump(self.model,f)
    def train_SVM(self,hyperparameter,X,y):
        self.model=SVM.SVC(C=hyperparameter)
        self.model.fit(X,y)