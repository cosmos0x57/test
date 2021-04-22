import numpy as np
import pandas as pd
import torch
from torch import nn
from torch.nn import init
import torch.utils.data as Data
import random
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import r2_score,mean_absolute_error




BATCH_SIZE = 256
EPOCH = 100
LR = 0.01
N_HIDDEN = 3
HIDDEN_SIZE = 128
ACTIVATION = torch.relu
B_INIT = -0.2

def minmax(mat):
    min_ = np.min(mat)
    max_ = np.max(mat)
    return (mat-min_)/(max_-min_)

narray =  np.load("E:\\处理数据及问题\\安捷暖通-5m-模型-末端.npy",allow_pickle=True)
X = narray[:,0:85]
Y = narray[:,85][:,np.newaxis]
# Y = minmax(Y)
train_x,test_x,train_y,test_y = train_test_split(X,Y,test_size=0.15,random_state=5)

train_x = torch.from_numpy(train_x).float()
train_y = torch.from_numpy(train_y).float()
test_x = torch.from_numpy(test_x).float() 
test_y = torch.from_numpy(test_y).float()
torch_train_dataset = Data.TensorDataset(train_x, train_y)
train_loader = Data.DataLoader(dataset = torch_train_dataset,batch_size = BATCH_SIZE,shuffle = True,num_workers = 2)
torch_test_dataset = Data.TensorDataset(test_x, test_y)
test_loader = Data.DataLoader(dataset = torch_test_dataset,batch_size = BATCH_SIZE,shuffle = True,num_workers = 2)

def mape(y_true, y_pred):
    return np.mean(np.abs((y_pred - y_true) / y_true)) * 100
 
def smape(y_true, y_pred):
    return 2.0 * np.mean(np.abs(y_pred - y_true) / (np.abs(y_pred) + np.abs(y_true))) * 100

class NeuralNet(nn.Module):
    def __init__(self,batch_normalization=False):
        super(NeuralNet,self).__init__()
        self.do_bn = batch_normalization
        self.fcs = []
        self.bns = []
        self.bn_input =nn.BatchNorm1d(85,momentum=0.5)
        for i in range(N_HIDDEN):
            inputsize = 85 if i == 0 else HIDDEN_SIZE
            fc = nn.Linear(inputsize,HIDDEN_SIZE)
            setattr(self,'fc%i'%i,fc)
            self._set_init(fc)
            self.fcs.append(fc)
            if self.do_bn:
                bn = nn.BatchNorm1d(HIDDEN_SIZE,momentum=0.5)
                setattr(self,'bn%i'%i,bn)
                self.bns.append(bn)
        self.predict = nn.Linear(HIDDEN_SIZE,1)
        self._set_init(self.predict)
    def _set_init(self,layer):
        init.normal_(layer.weight,mean=0.,std=.1)
        init.constant_(layer.bias,B_INIT)
    def forward(self,x):
        pre_activation = [x]
        if self.do_bn: x = self.bn_input(x)
        layer_input = [x]
        for i in range(N_HIDDEN): 
            x = self.fcs[i](x)
            pre_activation.append(x)
            if self.do_bn: x = self.bns[i](x)
            x = ACTIVATION(x)
            layer_input.append(x)
        out = self.predict(x)
        # out = ACTIVATION(out)
        return out

    def pre_grad(self,x):
        pre_activation = [x]
        if self.do_bn: x = self.bn_input(x)
        layer_input = [x]
        for i in range(N_HIDDEN): 
            x = self.fcs[i](x)
            pre_activation.append(x)
            if self.do_bn: x = self.bns[i](x)
            x = ACTIVATION(x)
            layer_input.append(x)
        out = self.predict(x)
        # out = ACTIVATION(out)
        return out

if __name__ == '__main__':
    neuralnet = NeuralNet(batch_normalization = True)
    opts = torch.optim.Adam(neuralnet.parameters(),lr = LR)
    loss_func = torch.nn.MSELoss() # 我改成了mse，因为bce要求神经网络的输出值域在(0,1)，一定要用bce的话，需要对y做归一化，以及神经网络最后一层需要激活函数relu使得y∈(0,1)
    # 现在依然没加，啊这，要加吗；要加的话，就得对label做归一化了，不然loss就算的不对那您觉得现在有必要加吗；没必要，如果后面要刷分的话，再加吧刷分？刷高神经网络的分数，比如mse.做完归一化，mse会明显变小，因为各个y的绝对值变小了
    #好的吧，那就先这样；ok

    total_grad = []
    train_r2 = []
    test_r2 = []
    for epoch in range(EPOCH):
        print('Epoch:',epoch)
        train_scores = []
        train_mses = []
        
        for step,(train_x,train_y) in enumerate(train_loader):
            train_x.requires_grad = True
            outputs_train = neuralnet(train_x)
            loss = loss_func(outputs_train,train_y)
            opts.zero_grad()
            loss.backward()
            opts.step()
            neuralnet.zero_grad()
            out = neuralnet.pre_grad(train_x)
            out.backward(torch.ones_like(out))
            if step == 0:
                train_grad = train_x.grad.numpy()
            else:
                train_grad = np.vstack((train_grad,train_x.grad))
            train_x.grad = None
            train_mses.append(np.sqrt(metrics.mean_squared_error(train_y.detach().numpy(), outputs_train.detach().numpy())))
            train_scores.append(r2_score(train_y.detach().numpy(),outputs_train.detach().numpy()))
        print('train:',np.mean(train_mses),np.mean(train_scores))
        mean_grad = np.mean(np.abs(train_grad),axis=0) # axis = 0
        total_grad.append(mean_grad)
        train_r2.append(np.mean(train_scores))
        

        # np.savetxt('E:\\处理数据及问题\\末端梯度'+'%d.csv'%epoch,mean_grad,fmt = '%f',delimiter =',')
        '''
        这里还没跑通，不知道什么bug，那好的吧，明天再说还有问题吗有
        传入ones_like后在这种情况下直接打印矩阵就可以了吗；是啊，ones_like(out)是个[1],啊，那梯度的结果我咋没看到，太多了我注释掉了嗷嗷，好的吧，OK，那train没问题了
        '''
        with torch.no_grad():
            test_mses = []
            test_scores = []
            for batch_x,batch_y in test_loader: # 遍历的是loader，由loader产生每个batch的(x,y)，不是全局的test_x,test_y
                # 局部变量会覆盖全局变量，如果全局变量后面还要用的话，就会乱掉；所以要养成良好的编程命名习惯，不要重名，不不不我现在是不明白原理，就是为什么上面就没问题，下面也没问题，bug估计也不是因为这个，只是我自己不喜欢这样
                outputs_test = neuralnet(batch_x)
                test_mses.append(np.sqrt(metrics.mean_squared_error(batch_y.detach().numpy(), outputs_test.detach().numpy())))
                test_scores.append(r2_score(batch_y.detach().numpy(),outputs_test.detach().numpy()))
            print('test:',np.mean(test_mses),np.mean(test_scores))
            test_r2.append(np.mean(test_scores))

    total_grad = np.array(total_grad)
    train_r2 = np.array(train_r2)
    test_r2 = np.array(test_r2)
    np.savetxt('E:\\处理数据及问题\\末端梯度\\末端梯度汇总'+'.csv',total_grad,fmt = '%f',delimiter =',')
    np.savetxt('E:\\处理数据及问题\\末端梯度\\末端训练集精度'+'.csv',train_r2,fmt = '%f',delimiter =',')
    np.savetxt('E:\\处理数据及问题\\末端梯度\\末端测试集精度'+'.csv',test_r2,fmt = '%f',delimiter =',')



