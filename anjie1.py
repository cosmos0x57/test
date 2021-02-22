import pandas as pd
import numpy as np
import os 
from os import walk
from openpyxl import load_workbook
from time import time


# start_time = time()
# file1=pd.read_excel('C:\\Users\\dell\\Desktop\\安捷物联图纸与数据\\安捷暖通 -2号管理机\\安捷暖通-5m-2020-1221-1227-2.xlsx', sheet_name="mySheet")
# # row1=file1.loc[[0],:]
# # a1=row1.to_numpy()
# end_time = time()
# print(end_time-start_time)
# print(file1.columns.values)

# np.save('file1.npy',file1)
# 
# from glob import glob
# for _file in glob('xls2npy/*'):

#     start_time = time()
#     file1 = np.load(_file,allow_pickle=True)
#     end_time = time()
#     print(end_time-start_time)
#     print(file1[0])
# 

# file1 = np.load("E:\\tmp\\xls1npy\\安捷暖通-5m-2020-1221-1227-1.npy",allow_pickle=True)
# file2 = np.load("E:\\tmp\\xls1npy\\安捷暖通-5m-2020-1228-0103-1.npy",allow_pickle=True)

# for i in range(len(file1[0])):
#     if not file1[0][i] == file2[0][i]:
#         print('not same: ',file1[0][i],file2[0][i],i)
#     else:
#         print('all is same')

# from glob import glob
# list3=[]
# for _file in glob('xls1npy/*'):
#     list3.append(np.load(_file,allow_pickle=True)[0])
# print(list3)

# 计算复杂度 nlogn
# for i in range(len(list3)-1): # 从i到N
#     for j in range(i+1,len(list3)-1): # 从i+1到N
#         print(i,j)
#         if not (list3[i] == list3[j]).all():
#             print('not the same:',i,j)

# 一个简单粗暴的方法：两层循环一模一样
# 计算复杂度 n^2
# for i in range(len(list3)): # 从i到N
#     for j in range(len(list3)):
#         print(i,j)
#         if not (list3[i] == list3[j]).all():
#             print('not the same:',i,j)

    
# from glob import glob
# for _file in glob('xls1npy/*'):
#     file1 = np.load(_file,allow_pickle=True)
#     print('file1=')
#     print(file1)
#     print(_file)
#     if _file=="xls1npy\\安捷暖通-5m-2020-1123-1129-1.npy":
#         np.save(('E:\\tmp\\安捷暖通-5m-1号合并.npy'),file1)
#     else:
#         file2=np.load('E:\\tmp\\安捷暖通-5m-1号合并.npy',allow_pickle=True)
#         print('file2=')
#         print(file2)
#         file3=np.delete(file1,0,axis=0)
#         print('file3=')
#         print(file3)
#         file4 = np.vstack((file2,file3))
#         np.save('E:\\tmp\\安捷暖通-5m-1号合并.npy',file4)
#         print(file4)


# 
# for dirpath, dirnames, filenames in walk("C:\\Users\\dell\\Desktop\\安捷物联图纸与数据\\安捷暖通 -1号管理机"):

#     files = os.listdir(dirpath)
#     print(files)
#     print(dirpath)
#     print(dirnames)
#     print(filenames)
#     list1=[]



# for i in files:
#     fp=os.path.join(dirpath,i)
#     df=pd.read_excel(fp)
#     row1=df.columns
#     print(row1)
#     list1.append(row1)
# print(list1)
# 

# #for i in range(len(list1)-1):
#     #print(list1[i]==list1[i+1])


# 
# file1=pd.read_excel('C:\\Users\\dell\\Desktop\\安捷物联图纸与数据\\安捷暖通 -2号管理机\\安捷暖通-5m-2020-1123-1129-2.xlsx', sheet_name="mySheet")
# nunique = file1.apply(pd.Series.nunique)
# cols_to_drop = nunique[nunique == 1].index
# file2=file1.drop(cols_to_drop, axis=1)
# file2.to_excel("C:\\Users\\dell\\Desktop\\安捷物联图纸与数据\\安捷暖通 -2号管理机\\安捷暖通-5m-2020-1123-1129-2(fuben).xlsx", sheet_name="Sheet1")

# from collections import Counterq
file2=np.load('安捷暖通-5m-2号合并.npy',allow_pickle=True)
# file3=file2[:,877] # 第877列
# print(file3)
# tmp = np.unique(file3[1:]) # 看来混合类型的array不支持unique，把第一个元素（列名）跳过
# print(len(tmp))
print(np.shape(file2))
idx_to_del = []
for i in range(len(file2[0])):
    col=file2[:,i]
    # print(col)
    col_data=np.unique(col[1:])
    # print(col_data)
    if len(col_data)==1:
        # print('column',i,'data:',col_data)
        idx_to_del.append(i)

file2 = np.delete(file2,idx_to_del,axis=1)
print(np.shape(file2))
np.save("E:\\tmp\\安捷暖通-5m-2号剔除.npy",file2)
np.savetxt("E:\\tmp\\安捷暖通-5m-2号剔除.csv",file2,delimiter=",",fmt="%s")


