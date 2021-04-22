import pyecharts.options as opts
from pyecharts.charts import Line
import pandas as pd
import numpy as np
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
from pyecharts.charts import Bar



Epoch_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,
58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105]
Epoch_list = np.linspace(0,99,100)
df_train = pd.read_csv("E:\\处理数据及问题\\热源梯度_温度\\热源训练集精度.csv")
x1 = df_train.values.tolist()
df_test = pd.read_csv("E:\\处理数据及问题\\热源梯度_温度\\热源测试集精度.csv")
x2 = df_test.values.tolist()


def line_chart() -> Line:
    c = (
        Line()
        .set_global_opts(
            title_opts=opts.TitleOpts(title="nn train and test scores",pos_left = '40%', pos_top = None ),
            tooltip_opts=opts.TooltipOpts(is_show=False),
            
            xaxis_opts=opts.AxisOpts(
                type_="value",
                interval=5,
                name='Epoch',
                axistick_opts=opts.AxisTickOpts(is_show=True,is_inside= True),
                name_location='end',
            ),
            
            yaxis_opts=opts.AxisOpts(
                type_="value",
                max_ = 1,
                min_ = -1,
                axistick_opts=opts.AxisTickOpts(is_show=True,is_inside= True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                name='R2',
                name_location='end',
            ),
            legend_opts=opts.LegendOpts(pos_right= '5%',pos_top='3%',orient = 'vertical',item_height = 10)

        )
        .add_xaxis(xaxis_data=Epoch_list)
        .add_yaxis(
            series_name="train score",
            y_axis=x1,
            symbol="emptyCircle",
            is_symbol_show=True,
            label_opts=opts.LabelOpts(is_show=False),
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),

                ]
            )
        )
        .add_yaxis(
            series_name="test score",
            y_axis=x2,
            symbol="emptyCircle",
            is_symbol_show=True,
            label_opts=opts.LabelOpts(is_show=False),
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                ]
            )
        )
    )
    return c
make_snapshot(snapshot, line_chart().render(), "E:\\处理数据及问题\\热源梯度_温度\\热源训练精度.png")





# df_total = pd.read_csv("E:\\处理数据及问题\\末端梯度\\末端梯度汇总.csv")
# column_list = df_total._stat_axis.values.tolist()
# y1 = df_total.iloc[:,[70]].values.tolist()
# y2 = df_total.iloc[:,[71]].values.tolist()
# y3 = df_total.iloc[:,[72]].values.tolist()
# y4 = df_total.iloc[:,[73]].values.tolist()
# y5 = df_total.iloc[:,[74]].values.tolist()
# y6 = df_total.iloc[:,[75]].values.tolist()
# y7 = df_total.iloc[:,[76]].values.tolist()
# y8 = df_total.iloc[:,[77]].values.tolist()
# y9 = df_total.iloc[:,[78]].values.tolist()
# y10 = df_total.iloc[:,[79]].values.tolist()
# y11 = df_total.iloc[:,[80]].values.tolist()
# y12 = df_total.iloc[:,[81]].values.tolist()
# y13 = df_total.iloc[:,[82]].values.tolist()
# y14 = df_total.iloc[:,[83]].values.tolist()
# y15 = df_total.iloc[:,[84]].values.tolist()



# def line_chart() -> Line:
#     c = (
#         Line(init_opts=opts.InitOpts(width = '1600px',height="800px"))
#         .set_global_opts(
#             title_opts=opts.TitleOpts(title="神经网络末端梯度结果_8",pos_left = '45%', pos_top = None ),
#             tooltip_opts=opts.TooltipOpts(is_show=False),
            
#             xaxis_opts=opts.AxisOpts(
#                 type_="value",
#                 interval=5,
#                 name='Epoch',
#                 axistick_opts=opts.AxisTickOpts(is_show=True,is_inside= True),
#                 name_location='end',
#             ),
            
#             yaxis_opts=opts.AxisOpts(
#                 max_ = 10,
#                 interval = 1,
#                 type_="value",
#                 axistick_opts=opts.AxisTickOpts(is_show=True,is_inside= True),
#                 splitline_opts=opts.SplitLineOpts(is_show=True),
#                 name='grad',
#                 name_location='end',
#             ),
#             legend_opts=opts.LegendOpts(pos_left= '5%',pos_bottom='0%',orient = 'horizontal')

#         )
#         .add_xaxis(xaxis_data=column_list)
#         .add_yaxis(
#             series_name="冷源机组送风压力3",
#             y_axis=y1,
#             symbol="emptyCircle",
#             is_symbol_show=True,
#             label_opts=opts.LabelOpts(is_show=False),

#         )
#         .add_yaxis(
#             series_name="冷源机组回风温度3",
#             y_axis=y2,
#             symbol="emptyCircle",
#             is_symbol_show=True,
#             label_opts=opts.LabelOpts(is_show=False),

#         )
#         .add_yaxis(
#             series_name="冷源机组CO2浓度3",
#             y_axis=y3,
#             symbol="emptyCircle",
#             is_symbol_show=True,
#             label_opts=opts.LabelOpts(is_show=False),

#         )
#         .add_yaxis(
#             series_name="冷源机组冷热水阀开度3",
#             y_axis=y4,
#             symbol="emptyCircle",
#             is_symbol_show=True,
#             label_opts=opts.LabelOpts(is_show=False),

#         )
#         .add_yaxis(
#             series_name="冷源机组制热阀投入开度3",
#             y_axis=y5,
#             symbol="emptyCircle",
#             is_symbol_show=True,
#             label_opts=opts.LabelOpts(is_show=False),

#         )
#         .add_yaxis(
#             series_name="新风机组供水温度",
#             y_axis=y6,
#             symbol="emptyCircle",
#             is_symbol_show=True,
#             label_opts=opts.LabelOpts(is_show=False),

#         )
#         .add_yaxis(
#             series_name="机组回水温度控制反馈",
#             y_axis=y7,
#             symbol="emptyCircle",
#             is_symbol_show=True,
#             label_opts=opts.LabelOpts(is_show=False),

#         )
#         .add_yaxis(
#             series_name="新风机组供水压力",
#             y_axis=y8,
#             symbol="emptyCircle",
#             is_symbol_show=True,
#             label_opts=opts.LabelOpts(is_show=False),

#         )
#         .add_yaxis(
#             series_name="新风机组回水温度",
#             y_axis=y9,
#             symbol="emptyCircle",
#             is_symbol_show=True,
#             label_opts=opts.LabelOpts(is_show=False),

#         )
#         .add_yaxis(
#             series_name="新风机组回水压力",
#             y_axis=y10,
#             symbol="emptyCircle",
#             is_symbol_show=True,
#             label_opts=opts.LabelOpts(is_show=False),

#         )
#         .add_yaxis(
#             series_name="一层温度3",
#             y_axis=y11,
#             symbol="emptyCircle",
#             is_symbol_show=True,
#             label_opts=opts.LabelOpts(is_show=False),

#         )
#         .add_yaxis(
#             series_name="二层温度4",
#             y_axis=y12,
#             symbol="emptyCircle",
#             is_symbol_show=True,
#             label_opts=opts.LabelOpts(is_show=False),

#         )
#         .add_yaxis(
#             series_name="三层温度2",
#             y_axis=y13,
#             symbol="emptyCircle",
#             is_symbol_show=True,
#             label_opts=opts.LabelOpts(is_show=False),

#         )
#         .add_yaxis(
#             series_name="五层温度3",
#             y_axis=y12,
#             symbol="emptyCircle",
#             is_symbol_show=True,
#             label_opts=opts.LabelOpts(is_show=False),

#         )
#         .add_yaxis(
#             series_name="六层温度3",
#             y_axis=y13,
#             symbol="emptyCircle",
#             is_symbol_show=True,
#             label_opts=opts.LabelOpts(is_show=False),

#         )
#     )
#     return c
# make_snapshot(snapshot, line_chart().render(), "E:\\处理数据及问题\\末端梯度\\末端参数梯度-8.png")







# colors = ["#5793f3", "#d14a61"]
# x_data = ["冷源机组送风压力3", "冷源机组回风温度3", "冷源机组CO2浓度3", "冷源机组冷热水阀开度3", "冷源机组制热阀投入开度3", 
# "新风机组供水温度", "机组回水温度控制反馈", "新风机组供水压力", "新风机组回水温度", "新风机组回水压力","一层温度3","二层温度4","三层温度2","五层温度3","六层温度3"]
# legend_list = ["Linear Model", "XGboost"]
# LM = [-0.000253,	0.221115,	-0.000069,	-0.005699,	-0.018611,	0.025629,	0.034428,	0.014341,	-0.001328,	-0.024608,	-0.003327,	0.121008,	0.799332, 0, 0,]
# xgboost = [12,30,43,8,0,7,0,0,9,1,28,12,4,4,21,]
# def bar_chart() -> Bar:

#     bar = (
#         Bar(init_opts=opts.InitOpts(width="1680px", height="800px"))
#         .add_xaxis(xaxis_data=x_data)
#         .add_yaxis(
#             series_name="Linear Model",
#             y_axis=LM,
#             yaxis_index=0,
#             color=colors[1],
#         )
#         .add_yaxis(
#             series_name="XGboost", y_axis=xgboost, yaxis_index=1, color=colors[0]
#         )
#         .extend_axis(
#             yaxis=opts.AxisOpts(
#                 name="xgboost",
#                 type_="value",
#                 min_=0,
#                 max_=100,
#                 position="right",
#                 axisline_opts=opts.AxisLineOpts(
#                     linestyle_opts=opts.LineStyleOpts(color=colors[1])
#                 ),
#             )
#         )
#         .set_global_opts(
#             yaxis_opts=opts.AxisOpts(
#                 type_="value",
#                 name="Linear Modle",
#                 min_=-1,
#                 max_=1,
#                 position="left",
#                 axisline_opts=opts.AxisLineOpts(
#                     linestyle_opts=opts.LineStyleOpts(color=colors[0])
#                 ),
#             ),
#             xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
#             title_opts=opts.TitleOpts(title="Linear Model和XGboost末端权重对比_8",pos_left = '45%', pos_top = None ),
#             # axisline_opts=opts.AxisLineOpts(is_on_zero=True),
#             tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
#             legend_opts=opts.LegendOpts(pos_right= '10%',pos_top='10%',orient = 'vertical')
#         )
#     )
#     return bar
# make_snapshot(snapshot, bar_chart().render(), "E:\\处理数据及问题\\末端梯度\\LM权重-8.png")