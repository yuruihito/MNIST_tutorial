# Usage
## ファイル構造
```
└──mnist_classification
    ├──MNIST：文字データ
    ├──utils - 可視化コード
    ├──workspace:　出力保存先
    │   ├──checkpoint　モデルパラメータ
    │   ├──eval 混同行列
    │   └──training_log: ロスと精度の推移
    ├──requierement.txt: 実行環境
    ├──pyproject.toml: 実行環境
    ├──*config.json: 引数
    ├──*eval.ipynb: テスト用コード
    ├──*model.py: CNN
    └──*train.ipynb: 学習用コード
```

## 環境構築
必要なモジュールのインストールをしてください。
```
pip install -r requirements.txt
```
poetryを使用している場合
```
poetry install
```

## config 引数設定
以下はデフォルト値です。適宜変更してください。
```
    "gpu_id": 0, #GPU使用
    "batch_size": 100,  #バッチサイズ
    "epoch_num" : 50, #学習数
    "save_every_epoch_num": 10, #保存頻度
    "model_state": "checkpoint" 
```

## 学習
train.ipynbを実行
epoch毎のロスと精度の推移は
```

/workspace/training_log
```
に書き出し

以下の学習logが書き出される
![loss_and_accuray](https://github.com/user-attachments/assets/051fd663-f039-4b86-9ab5-0ebb16ac3883)
## テスト
eval.ipynbを実行
結果の可視化は
```
/workspace/eval
```
に書き出し

以下のような混同行列が書き出される
![mnist_confusion_matrix](https://github.com/user-attachments/assets/fe0b14f0-c870-4ed3-b4e0-9d8bc822fe4d)


