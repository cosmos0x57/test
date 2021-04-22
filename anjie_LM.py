import numpy as np
import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import r2_score,mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn import svm
import xgboost as xgb
from xgboost import plot_importance
from matplotlib import pyplot as plt



narray =  np.load("E:\\处理数据及问题\\安捷暖通-5m-模型-末端.npy",allow_pickle=True)
train_x,test_x,train_y,test_y = train_test_split(narray[:,0:83],narray[:,83][:,np.newaxis],test_size=0.15,random_state=5)
# Linearmodel
Linear_model = LinearRegression()
LM = Linear_model.fit(train_x,train_y)
outputs_LM = LM.predict(test_x)
print('LM',r2_score(test_y,outputs_LM))
coefficients_LM = LM.coef_
np.savetxt('E:\\处理数据及问题\\末端梯度\\LM权重-3'+'.csv',coefficients_LM,fmt = '%f',delimiter =',')
print(LM.intercept_)
#XGBoost
params = {
    'booster': 'gbtree',
    'objective': 'reg:squarederror',
    'gamma': 0.1,
    'max_depth': 5,
    'lambda': 3,
    'subsample': 0.7,
    'colsample_bytree': 0.7,
    'min_child_weight': 3,
    'silent': 1,
    'eta': 0.1,
    'seed': 1000,
    'nthread': 4,
}
dtrain = xgb.DMatrix(train_x, train_y)
num_rounds = 100
plst = list(params.items())
XGB_model = xgb.train(plst, dtrain, num_rounds)

# 对测试集进行预测
dtest = xgb.DMatrix(test_x)
outputs_XGB = XGB_model.predict(dtest)
print('XGB',r2_score(test_y,outputs_XGB))
print(XGB_model.get_fscore())
# plot_importance(XGB_model)
# plt.rcParams['figure.autolayout'] = True
# plt.xlim(fontsize=5)
# plt.ylim(fontsize=5)
# plt.xlabel('xlabel',fontsize =5)
# plt.ylabel('ylabel',fontsize =5)
# plt.show()
