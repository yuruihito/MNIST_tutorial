# 使い方
## ファイル構造
*のところが変更やCNNの学習に使える。
```
└──mnist_classification
    ├──MNIST：文字データ
    ├──utils - 可視化コード
    ├──workspace:　出力保存先
    │   ├──checkpoint　モデルパラメータ
    │   ├──eval 混同行列
    │   └──training_log: ロスと精度の推移
    ├──requierement.txt: 実行環境　余計なものがかなり含まれています. python == 3.12.3
    ├──*config.json: 引数
    ├──*eval.ipynb: テスト用コード
    ├──*model.py: CNN
    └──*train.ipynb: 学習用コード
```

##　環境構築
必要なモジュールのインストール
```
!pip install -r requirements.txt
```
pythonは3.12.3を使用しました。

## config　引数設定
適宜変更してください。変更しなくても実行可能
```
    "gpu_id": 0, #GPU使用
    "batch_size": 100,  #バッチサイズ
    "epoch_num" : 50,　#学習数
    "save_every_epoch_num": 10,　#保存頻度
    "model_state": "checkpoint"　#test時の使用モデルパラメータ名
```

## 学習
train.ipynbを実行
epoch毎のロスと精度の推移は
```
/workspace/training_log　
```
に書き出し

## テスト
eval.ipynbを実行
結果の可視化は
```
/workspace/eval
```
に書き出し
