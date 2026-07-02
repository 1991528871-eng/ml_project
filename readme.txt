計算機プログラミング　グループワーク後半
group c

担当：
沈展帆・J4250336    前処理フェーズ
園田夏菜・J4260438  運用フェーズ
石谷良祐・J4261071  評価フェーズ
柚木翔太・J4260079  学習フェーズ 1 aaa
米澤大雅・J4250453  学習フェーズ 2

配布された template をほぼ丸ごとコピーして実行してみた
変更した箇所：
1.  バグが出たので，requirements.txt の内容を調整した
2.  時間かかりすぎたので，
    load_dictionary.py と count_statistics.py の内容を調整してみたが，変化なし
    train.txt と validation.txt を大幅削除
実行手順と結果：
1.  src/preprocess_data.py を実行
    dictionary file: data/dictionary1.txt
    # 前処理する際に，dictionary1.txt を参照する
    (既存のテキストファイル) -> (自動作成された新しいファイル)
    data.txt -> data_processed.pkl
    train.txt -> train_processed.pkl
    validation.txt -> validation_processed.pkl
2.  model/ を作成
    train.py を実行
    すると，models/ で複数の.kplファイルが作成された
3.  validate.py を実行
    すると，各モデルの精度・適合率・再現率は Terminal で出力され，
    models/ で best_model.pkl が作成された (RF_4.pkl)
4.  predict.py を実行
    Terminal で出力された．
