import numpy as np
import pandas as pd
import os
# out_dir = 'xls2npy'

# for root,parent,files in os.walk('C:\\Users\\dell\\Desktop\\安捷物联图纸与数据\\安捷暖通 -1号管理机\\'):
#     for _file in files:
#         if not _file.endswith('.xlsx'):
#             print('Wrong format!')
#         else:
#             print('processing file ',_file)
#             df = pd.read_excel(os.path.join(root,_file)) 
#             complete_data = np.vstack(([df.columns.values],df.values))
#             np.save(os.path.join(out_dir,_file.strip('.xlsx')+'.npy'),complete_data)
            

df = df.loc[:, ~df.columns.str.contains('Unnamed')]


# '''
# debug
# '''
# file1=pd.read_excel('C:\\Users\\dell\\Desktop\\安捷物联图纸与数据\\安捷暖通 -2号管理机\\安捷暖通-5m-2020-1221-1227-2.xlsx', sheet_name="mySheet")
# print(np.shape(file1.columns.values),np.shape(file1.values))
# print(np.shape(np.vstack(([file1.columns.values],file1.values))))

# (1142,) -> (1,1142) + (2016,1142) -> (2017,1142)
# a = [1,2,3] -> (3,)
# [a] == [[1,2,3]] -> (1,3)

#git status
#git add .
#git commit -m "update"
#git push

