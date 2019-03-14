import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False

house = pd.read_csv('./DATA/58E.csv', encoding='gbk')
price = house['DanJia']
max_price = price.max()
min_price = price.min()
mean_price = price.mean()
median_price = price.median()

def printprice():   #打印
    print("海淀区整租房最高价格：%.2f元/平方米*月" % max_price)
    print("海淀区整租房最低价格：%.2f元/平方米*月" % min_price)
    print("海淀区整租房平均价格：%.2f元/平方米*月" % mean_price)
    print("海淀区整租房中位数价格：%.2f元/平方米*月" % median_price)
def num_price():    #房价数量分布
    plt.xlim(0,700)
    plt.ylim(0,400)
    plt.title("海淀区整租房价格分析")
    plt.xlabel("海淀区整租房价格 (元/平方米*月)")
    plt.ylabel("整租房数量")
    plt.hist(price, bins=60)
    plt.vlines(mean_price, 0, 500, color='red', label='平均价格', linewidth=1.5, linestyle='--')
    plt.vlines(median_price, 0, 500, color='red',label='中位数价格', linewidth=1.5)
    plt.legend()
    plt.show()
def CiJiQuYu_price():   #海淀区内，次级区域与价格的关系
    mean_price_district = house.groupby('CiJiQuYu')['DanJia'].mean().sort_values(ascending=False)
    mean_price_district.plot(kind='bar',color='b')
    print(mean_price_district)
    plt.ylim(30,350,20)
    plt.title("海淀区各子地区整租房价格平均价格分析")
    plt.xlabel("海淀区行政区划")
    plt.ylabel("海淀区整租房价格 (元/平方米*月)")
    plt.show()
    '''箱形图
    house.boxplot(column='DanJia', by='CiJiQuYu', whis=1.5,)
    plt.title("海淀区各子地区整租房价格平均价格分析(箱形图)")
    plt.show()
    '''
def Mianji_price():     #海淀区内，面积与价格的关系
    x = house['MianJi']
    y = house['DanJia']
    plt.scatter(x,y,s=2.5)
    plt.title("房屋面积对整租房房价的影响")
    plt.show()
def Huxing_price(): #户型对单价的影响
    mean_price_Huxing = house.groupby('Huxing')['DanJia'].mean().sort_values(ascending=False)
    mean_price_Huxing.plot(kind='bar',color='b')
    print(mean_price_Huxing)
    plt.ylim(30,350,20)
    plt.title("海淀区各子地区整租房价格平均价格分析")
    plt.xlabel("户型")
    plt.ylabel("海淀区整租房价格 (元/平方米*月)")
    plt.show()
def ZhuangXiu_price():  #装修对单价的影响
    mean_price_ZhuangXiu = house.groupby('ZhuangXiu')['DanJia'].mean().sort_values(ascending=False)
    mean_price_ZhuangXiu.plot(kind='bar',color='b')
    print(mean_price_ZhuangXiu)
    plt.ylim(30,350,20)
    plt.title("海淀区各子地区整租房价格平均价格分析")
    plt.xlabel("装修")
    plt.ylabel("海淀区整租房价格 (元/平方米*月)")
    plt.show()
def ChaoXiang_price():  #朝向对单价的影响
    mean_price_FangXiang = house.groupby('FangXiang')['DanJia'].mean().sort_values(ascending=False)
    mean_price_FangXiang.plot(kind='bar',color='b')
    print(mean_price_FangXiang)
    plt.ylim(30,350,20)
    plt.title("海淀区各子地区整租房价格平均价格分析")
    plt.xlabel("朝向")
    plt.ylabel("海淀区整租房价格 (元/平方米*月)")
    plt.show()
def LouCeng_price():    #楼层对单价的影响
    mean_price_LouCeng = house.groupby('LouCeng')['DanJia'].mean().sort_values(ascending=False)
    mean_price_LouCeng.plot(kind='bar',color='b')
    print(mean_price_LouCeng)
    plt.ylim(30,350,20)
    plt.title("海淀区各子地区整租房价格平均价格分析")
    plt.xlabel("楼层")
    plt.ylabel("海淀区整租房价格 (元/平方米*月)")
    plt.show()
def PayWay_price(): #押金对单价影响
    mean_price_PayWay = house.groupby('PayWay')['DanJia'].mean().sort_values(ascending=False)
    mean_price_PayWay.plot(kind='bar',color='b')
    print(mean_price_PayWay)
    plt.ylim(30,350,20)
    plt.title("海淀区各子地区整租房价格平均价格分析")
    plt.xlabel("押金方式")
    plt.ylabel("海淀区整租房价格 (元/平方米*月)")
    plt.show()
#ZhuangXiu_price()