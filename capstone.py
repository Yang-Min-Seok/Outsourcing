# -*- coding: utf-8 -*-
"""Capstone.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NVbfpsb2T1GJRtLJMfiTLFNZrU4Q-rRI
"""
from torch import nn, cat
import torch.nn.functional as F
from torch.nn import Linear, ReLU
from torchvision import models


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        model_pt = models.vgg16(weights='DEFAULT')
        for p in model_pt.parameters():
            p.requires_grad = False
        self.l1 = Linear(98304, 1024)
        self.l2 = Linear(1024, 1)  # regression 이기 때문에 마지막 차원 1
        self.VGG16 = model_pt.features
        self.relu = ReLU(inplace=True)

    def forward(self, top, bot, shoes):
        top = self.VGG16(top)  # 256*256
        bot = self.VGG16(bot)  #
        shoes = self.VGG16(shoes)  #
        N,r,c = top.size()
        print(N)
        print(r)
        print(c)
        top = top.view(1, N*r*c)
        bot = bot.view(1, N*r*c)
        shoes = shoes.view(1, N*r*c)
        z = cat((top, bot, shoes), 1)
        z = self.l1(z)
        z = self.relu(z)
        z = self.l2(z)
        return z