import numpy as np
import pandas as pd
import torch

df = pd.read_excel("E:\\处理数据及问题\\安捷暖通-5m-模型训练-1.xlsx")
np.save('E:\\处理数据及问题\\安捷暖通-5m-模型训练-1.npy',df)
# class NeuralNet(nn.module):
#     def __init__(self,)