import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm 
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import datetime as dt
import matplotlib as mpl

# df1 = pd.read_excel('E:\\处理数据及问题\\安捷暖通-5m-1号剔除-3.xlsx',sheet_name="安捷暖通-5m-1号剔除-1")
# df2 = df1.loc[:,['日期','气象站环温','气象站环湿','气象站总辐射1']]
# print(df2)
# df2.to_excel('安捷暖通-5m-室外气象.xlsx', sheet_name='Sheet1')

# df1 = pd.read_excel('E:\\处理数据及问题\\安捷暖通-5m-室内温度-2.xlsx', sheet_name='Sheet6')
# x_data = df1.iloc[:,0]
# y_data1 = df1.iloc[:,1]
# y_data2 = df1.iloc[:,2]
# y_data3 = df1.iloc[:,3]
# y_data4 = df1.iloc[:,4]
# y_data5 = df1.iloc[:,5]



# print(x_data[0],type(x_data[0]))


# fig = plt.figure()
# plt.rcParams["font.family"]="SimHei"
# mpl.rcParams['axes.unicode_minus']=False
# ax1 = fig.add_subplot(111)
# date2_1 = dt.minute(2020,11,23,0,0)
# date2_2 = dt.datetime(2021,1,10,23,55)
# delta2 = dt.timedelta(minutes=5)
# dates2 = mpl.dates.drange(date2_1, date2_2, delta2)
# date2_1 = dt.datetime(2020,11,23,0,0)
# date2_2 = dt.datetime(2021,1,10,23,55)
# delta2 = dt.timedelta(minutes=5)
# dates2 = mpl.dates.drange(date2_1, date2_2, delta2)[:-1] # 14111

# ax1.plot_date(x_data, y_data1, label="一层温度",linestyle='-',markersize=0.05)
# ax1.plot_date(x_data, y_data2, label="二层温度",linestyle='-',markersize=0.05)
# ax1.plot_date(x_data, y_data3, label="三层温度",linestyle='-',markersize=0.05)
# ax1.plot_date(x_data, y_data4, label="四层温度",linestyle='-',markersize=0.05)
# # ax1.plot_date(x_data, y_data5, label="六层温度",linestyle='-',markersize=0.05)
# # dateFmt = mpl.dates.DateFormatter('%Y-%m-%d')
# # ax1.xaxis.set_major_formatter(dateFmt)

# daysLoc = mpl.dates.DayLocator(interval=1)
# hoursLoc = mpl.dates.HourLocator(interval=1)
# ax1.xaxis.set_major_locator(daysLoc)
# ax1.xaxis.set_minor_locator(hoursLoc)
# ax1.yaxis.set_major_locator(MultipleLocator(2))
# plt.xlim(x_data.values[0], x_data.values[-1])
# plt.ylim(8,32)
# fig.autofmt_xdate()



# ax1.set_xlabel("日期")#添加x轴坐标标签，后面看来没必要会删除它，这里只是为了演示一下。
# ax1.set_ylabel("温度/℃")#添加y轴标签，设置字体大小为16，这里也可以设字体样式与颜色

# ax1.set_title("室内温度")#标题（表头）
# ax1.legend(loc='upper right')

# plt.savefig("E:\\处理数据及问题\\作图\\室内温度-2.png")
# plt.show()


# # from matplotlib.dates import date2num, num2date
# # dates2 = mpl.dates.drange(dt.datetime(2020,11,23,0,0), dt.datetime(2021,1,10,23,55), dt.timedelta(minutes=5))
# # print(len(dates2),num2date(dates2[0]),num2date(dates2[-1]))


fig = plt.figure()
plt.rcParams["font.family"]="SimHei"
ax1 = fig.add_subplot(111)

df1 = pd.read_excel('E:\\处理数据及问题\\安捷暖通-5m-能耗-2.xlsx', sheet_name='Sheet2')
x_data = df1.iloc[:,0]
y_data1 = df1.iloc[:,1]
y_data2 = df1.iloc[:,2]
y_data3 = df1.iloc[:,3]

labels=["末端","输配","热源"]
colors=["#8da0cb","#fc8d62","#66c2a5"]
plt.stackplot(x_data,y_data1,y_data2,y_data3,labels=labels,colors=colors)
plt.legend(loc="upper left")
ax1.set_title("空调系统功率")

daysLoc = mpl.dates.DayLocator(interval=7)
hoursLoc = mpl.dates.HourLocator(interval=24)
ax1.xaxis.set_major_locator(daysLoc)
ax1.xaxis.set_minor_locator(hoursLoc)
# ax1.yaxis.set_major_locator(MultipleLocator(100))
plt.xlim(x_data.values[0], x_data.values[-1])
# plt.ylim(300,2000)
fig.autofmt_xdate()

plt.savefig("E:\\处理数据及问题\\作图\\能耗.png")
plt.show()


# size = 0.25
# base = 50


# fig = plt.figure()
# plt.rcParams["font.family"]="SimHei"
# ax1 = fig.add_subplot(111)


# vals_outer = np.array([ 
#     [2134.4,0,0,0,0],
#     [7232.799,12386.499,97.8,1922.899,1601.299],
#     [67883.799,265.601,0, 0,0]
#     ])

# vals_inner = vals_outer.sum(axis=1)

# # 最内圈使用的数值为内圈各类数据加上base
# vals_first = vals_inner + base

# '''
# 第二圈使用的数值, 因为最内圈每个类别都加上了base, 所以为了确保第二圈的数值和内圈相匹配, 第二圈的各类别要按照各自所占的比例分配各类的总数值.
# '''
# vals_second = np.zeros((3, 5))
# for i in range(3):
#     s_a = vals_first[i]
#     s_b = vals_outer[i].sum()
#     # 如果第二圈某类总数值为0, 则分配base.
#     if s_b == 0.0:
#         vals_second[i][1] = base
#         continue
#     for j in range(5):
#         vals_second[i][j] = (vals_outer[i][j] / s_b) * s_a
# # 获取colormap tab20c和tab20b的颜色
# cmap_c = plt.get_cmap("tab20c")

# # 使用tab20c的全部颜色和tab20b中的 5至8 颜色
# cmap_1 = cmap_c(np.array([0,1,2,3,4,5.6,7,8,9,10,11,12,13,14]))
# cmap_2 = cmap_c(np.arange(20))
# # 内圈的颜色是每4个颜色中色彩最深的那个. vstack是将两类颜色叠加在一起
# inner_colors = cmap_2[::4]
# # 外圈的颜色是全部24种颜色
# outer_colors = cmap_2



# labels_first=["末端\n{}kW/h".format(vals_inner[0]), 
#         "输配\n{}kW/h".format(vals_inner[1]), 
#         "热源\n{}kW/h".format(vals_inner[2])
#         ]

# labels_seocnd=[
#     "新风\n2134.4kW/h",
#     "",
#     "",
#     "",
#     "",

#     "地源热泵空调侧水泵\n7232.799kW/h",
#     "地源热泵地源侧水泵\n12386.499kW/h",
#     "太阳能直供水泵\n97.8kW/h",
#     "空调蓄能水泵\n1922.899kW/h",
#     "放能水泵\n1601.299kW/h",

#     "地源热泵主机\n67883.799kW/h",
#     "太阳能设备\n265.601kW/h",
#     "",
#     "",
#     "",

# ]



# handles, labels =  ax1.pie(vals_first, radius=1-size-size, 
#                 labels=labels_first, 
#                 labeldistance=0.5,  rotatelabels=True, textprops={'fontsize': 5}, 
#                 colors=inner_colors, wedgeprops=dict(width=size, edgecolor='w'))

# ax1.pie(vals_second.flatten(),   radius=1-size, colors=outer_colors,
#     labels=labels_seocnd, 
#     labeldistance=0.7,  rotatelabels=True, textprops={'fontsize': 5}, 
#     wedgeprops=dict(width=size, edgecolor='w'))

# plt.title('供暖系统能耗占比', fontsize=10)
# plt.legend(handles=handles, labels=[
#         "末端", 
#         "输配", 
#         "热源", 
#         ],
#         loc = 1
#         )
# plt.savefig("E:\\处理数据及问题\\作图\\能耗分布.png")
# plt.show()
