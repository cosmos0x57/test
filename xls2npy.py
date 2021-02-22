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
#

# not same:  新风A3_1直膨表冷器后风温度 六层机房新风周四时段3时间设置反馈 826 
# not same:  新风A3_1预冷后_直膨前风温度 六层机房新风周四时段4时间设置反馈 827
# not same:  新风A3_1预冷表冷器前风温度 六层机房新风周五时段开关时间设置反馈 828
# not same:  新风A4_1直膨表冷器后风温度 六层机房新风周五时段1时间设置反馈 829
# not same:  新风A4_1预冷后_直膨前风温度 六层机房新风周五时段2时间设置反馈 830
# not same:  新风A4_1预冷表冷器前风温度 一层2号室内湿度 831
# not same:  新风A5_1直膨表冷器后风温度 六层机房新风周五时段3时间设置反馈 832
# not same:  新风A5_1预冷后_直膨前风温度 六层机房新风周五时段4时间设置反馈 833
# not same:  六层机房新风周四时段3时间设置反馈 六层机房新风周六时段开关时间设置反馈 834
# not same:  新风A5_1预冷表冷器前风温度 六层机房新风周六时段1时间设置反馈 835
# not same:  新风A3_1机外余压 六层机房新风周六时段2时间设置反馈 836
# not same:  新风A4_1机外余压 六层机房新风周六时段3时间设置反馈 837
# not same:  新风A5_1机外余压 六层机房新风周六时段4时间设置反馈 838
# not same:  新风A3_1送风风速 六层机房新风周日时段开关时间设置反馈 839
# not same:  新风A4_1送风风速 六层机房新风周日时段1时间设置反馈 840
# not same:  新风A5_1送风风速 六层机房新风周日时段2时间设置反馈 841
# not same:  新风机组3_1总冷量 Unnamed: 842 842
# not same:  新风机组3_1预冷表冷器显冷 Unnamed: 843 843
# not same:  新风机组3_1深冷表冷器显冷 Unnamed: 844 844
# not same:  六层机房新风周四时段4时间设置反馈 Unnamed: 845 845
# not same:  新风机组3_1总显冷 Unnamed: 846 846
# not same:  新风机组3_1总潜冷 Unnamed: 847 847
# not same:  新风机组3_1总冷量累计量 Unnamed: 848 848
# not same:  新风机组3_1预冷表冷器显冷累计量 Unnamed: 849 849
# not same:  新风机组3_1深冷表冷器显冷累计量 Unnamed: 850 850
# not same:  新风机组3_1总显冷累计量 Unnamed: 851 851
# not same:  新风机组3_1总潜冷累计量 Unnamed: 852 852
# not same:  新风机组4_1总冷量 Unnamed: 853 853
# not same:  新风机组4_1预冷表冷器显冷 Unnamed: 854 854
# not same:  新风机组4_1深冷表冷器显冷 Unnamed: 855 855
# not same:  六层机房新风周五时段开关时间设置反馈 Unnamed: 856 856
# not same:  新风机组4_1总显冷 Unnamed: 857 857
# not same:  新风机组4_1总潜冷 Unnamed: 858 858
# not same:  新风机组4_1总冷量累计量 Unnamed: 859 859
# not same:  新风机组4_1预冷表冷器显冷累计量 Unnamed: 860 860
# not same:  新风机组4_1深冷表冷器显冷累计量 Unnamed: 861 861
# not same:  新风机组4_1总显冷累计量 Unnamed: 862 862
# not same:  新风机组4_1总潜冷累计量 Unnamed: 863 863
# not same:  新风机组5_1总冷量 Unnamed: 864 864
# not same:  新风机组5_1预冷表冷器显冷 Unnamed: 865 865
# not same:  新风机组5_1深冷表冷器显冷 Unnamed: 866 866
# not same:  六层机房新风周五时段1时间设置反馈 Unnamed: 867 867
# not same:  新风机组5_1总显冷 Unnamed: 868 868
# not same:  新风机组5_1总潜冷 Unnamed: 869 869
# not same:  新风机组5_1总冷量累计量 Unnamed: 870 870
# not same:  新风机组5_1预冷表冷器显冷累计量 Unnamed: 871 871
# not same:  新风机组5_1深冷表冷器显冷累计量 Unnamed: 872 872
# not same:  新风机组5_1总显冷累计量 Unnamed: 873 873
# not same:  新风机组5_1总潜冷累计量 Unnamed: 874 874
# not same:  新风机组3_1回风焓值焓 Unnamed: 875 875
# not same:  新风机组3_1出风焓值 Unnamed: 876 876
# not same:  新风机组4_1回风焓值焓 Unnamed: 877 877
# not same:  六层机房新风周五时段2时间设置反馈 Unnamed: 878 878
# not same:  新风机组4_1出风焓值 Unnamed: 879 879
# not same:  新风机组5_1回风焓值焓 Unnamed: 880 880
# not same:  新风机组5_1出风焓值 Unnamed: 881 881
# not same:  新风机组3_1瞬时风量 Unnamed: 882 882
# not same:  新风机组4_1瞬时风量 Unnamed: 883 883
# not same:  新风机组5_1瞬时风量 Unnamed: 884 884
# not same:  新风机组3_1风量累计量 Unnamed: 885 885
# not same:  新风机组4_1风量累计量 Unnamed: 886 886
# not same:  新风机组5_1风量累计量 Unnamed: 887 887
# not same:  一层2号室内湿度 Unnamed: 888 888
# not same:  六层机房新风周五时段3时间设置反馈 Unnamed: 889 889
# not same:  六层机房新风周五时段4时间设置反馈 Unnamed: 890 890
# not same:  六层机房新风周六时段开关时间设置反馈 Unnamed: 891 891
# not same:  六层机房新风周六时段1时间设置反馈 Unnamed: 892 892
# not same:  六层机房新风周六时段2时间设置反馈 Unnamed: 893 893
# not same:  六层机房新风周六时段3时间设置反馈 Unnamed: 894 894
# not same:  六层机房新风周六时段4时间设置反馈 Unnamed: 895 895
# not same:  六层机房新风周日时段开关时间设置反馈 Unnamed: 896 896
# not same:  六层机房新风周日时段1时间设置反馈 Unnamed: 897 897
# not same:  六层机房新风周日时段2时间设置反馈 Unnamed: 898 898