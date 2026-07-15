計算機プログラミング　グループワーク後半
group c

担当：
沈展帆・J4250336  前処理フェーズ
園田夏菜・J4260438  運用フェーズ
石谷良祐・J4261071  評価フェーズ
柚木翔太・J4260079  学習フェーズ 1
米澤大雅・J4250453  学習フェーズ 2

ファイル構成：
ml_project/
|--- data/
|    |--- dictionary1.txt               # 辞書1の生データ
|    |--- dictionary1_loaded.pkl        # 辞書1（pythonのdictionary型）
|    |--- dictionary2.txt               # 辞書2の生データ
|    |--- dictionary2_loaded.pkl        # 辞書2（pythonのdictionary型）
|    |--- train.txt                     # 訓練用の生データ
|    |--- train_preprocessed.pkl        # ベクトル化済みの訓練データ（ラベル付き）
|    |--- validation.txt                # 検証用の生データ
|    |--- validation_preprocessed.pkl   # ベクトル化済みの検証データ（ラベル付き）
|    |--- data.txt                      # 予測用の生データ
|    |--- data_preprocessed.pkl         # ベクトル化済みの予測データ（ラベル無し）
|    |--- consequence.txt               # 予測した結果
|--- src/
|    |--- my_library/
|    |    |--- load_input_data.py       # データを読み込むモジュール
|    |    |--- count_statistics.py      # 単語の極性情報を計算するモジュール
|    |    |--- data_preprocessor.py     # データの前処理を行うクラス
|    |    |--- trainer1.py              # データの学習を行うクラス（柚木さん担当）
|    |    |--- validator.py             # データの評価を行うクラス
|    |--- load_dictionary.py            # 辞書を読み込むモジュール
|    |--- preprocess_data.py            # 前処理を行うモジュール
|--- models/
|    |--- models_1/                     # 学習したモデル（柚木さん担当）
|    |    |--- ???.pkl
|    |--- models_2/                     # 学習したモデル（米澤さん担当）
|    |    |--- ???.pkl
|    |--- best_model.pkl                # 最良のモデル（評価フェーズで作成）
|--- train1.py                          # 学習を行うモジュール（柚木さん担当）
|--- train2.py                          # 学習を行うモジュール（米澤さん担当）
|--- validate.py                        # 検証を行うモジュール
|--- predict.py                         # 予測を行うモジュール
|--- readme.txt                         # プロジェクトの説明（本ファイル）
|--- requirements.txt                   # 必要な外部ライブラリ
