import pickle
from sklearn.linear_model import LogisticRegression

class Trainer:
    def __init__(self):
        self.model = None

    def load_data(self, file_path):
        #データの読み込み
        with open(file_path, 'rb') as f:
            X, y = pickle.load(f)
        return X, y

    def dump_model(self, file_path):
        #学習したモデルを保存
        with open(file_path, 'wb') as f:
            pickle.dump(self.model, f)

    def train_LogisticRegression(self, c_value, X, y):
        #ロジスティック回帰
        # max_iterは学習が収束しない警告を防ぐために少し大きめに設定
        self.model = LogisticRegression(C=c_value, max_iter=1000)
        self.model.fit(X, y)
