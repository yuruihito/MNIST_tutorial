import torch            # 深層学習のモジュール（PyTorch）
import torch.nn as nn

class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1)#(チャンネル数, カーネル数)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        self.l1 = nn.Linear(7*7*32, 1024)
        self.l2 = nn.Linear(1024, 1024)
        self.l3 = nn.Linear(1024, 10)
        self.act = nn.ReLU()
        self.pool = nn.MaxPool2d(2, 2)

    def forward(self, x):                       # 入力画像サイズ: [batch, 1, 28, 28]
        h = self.pool(self.act(self.conv1(x)))  # 出力される特徴マップサイズ: [batch, 16, 14, 14]
        h = self.pool(self.act(self.conv2(h)))  # 出力される特徴マップサイズ: [batch, 32, 7, 7]
        # 特徴マップの配列サイズを [batch, channel, height, width] --> [batch, channel * height * width] に変更
        h = h.view(h.size()[0], -1)
        h = self.act(self.l1(h))
        h = self.act(self.l2(h))
        h = self.l3(h)
        return h