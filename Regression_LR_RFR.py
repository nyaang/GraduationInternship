import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor,RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体

# 使用one-hot编码获取特征
def get_feature():
    df = pd.read_csv('./DATA/58w.csv',encoding='gbk')
    area = df['面积']
    huxing = df['户型']

    shi = []
    ting = []
    wei = []
    for hx in huxing:
        shi.append(int(hx.split('室')[0]))
        ting.append(int(hx.split('室')[1].split('厅')[0]))
        wei.append(int(hx.split('厅')[1].split('卫')[0]))

    # 装修
    decorate = pd.get_dummies(df['装修'], prefix='装修')
    data_dec= pd.concat([df, decorate], axis=1)

    # 朝向
    direction = pd.get_dummies(df['朝向'], prefix='朝向')
    data_dir = pd.concat([data_dec, direction], axis=1)

    # 高低
    high_low = pd.get_dummies(df['高低'], prefix='高低')
    data_hl = pd.concat([data_dir, high_low], axis=1)

    # 次级区域
    district = pd.get_dummies(df['次级区域'], prefix='高低')
    data_dis = pd.concat([data_hl, district], axis=1)

    # 押金
    deposit = pd.get_dummies(df['押金'], prefix='押金')
    data = pd.concat([data_dis, deposit], axis=1)
    data.drop(['面积','租赁方式','户型','装修','朝向','高低','楼层','小区名','区域','次级区域','详细地址','详情',
               '亮点','描述','URL','周期','押金'], axis=1, inplace=True)

    data['面积'] = area
    data['室'] = shi
    data['厅'] = ting
    data['卫'] = wei
    #显示所有列
    # pd.set_option('display.max_columns', None)
    # print(data.head())
    return  data

# 线性回归训练模型
def LR_train_model(data):
    x = data.as_matrix()[:,1:]
    y = data.as_matrix()[:,0].reshape(-1,1)

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=40, test_size=0.2)

    #数据标准化处理
    ss_x = StandardScaler()
    ss_y = StandardScaler()
    x_train = ss_x.fit_transform(x_train)
    x_test = ss_x.transform(x_test)
    y_train = ss_y.fit_transform(y_train)
    y_test = ss_y.transform(y_test)

    lr = LinearRegression()     #初始化
    lr.fit(x_train, y_train)    #训练数据
    lr_y_predict = lr.predict(x_test)  #回归预测
    return ss_y, y_test, lr_y_predict

# 随机森林训练模型
def RFR_train_model(data):
    x = data.as_matrix()[:, 1:]
    y = data.as_matrix()[:, 0].reshape(-1, 1)

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=40, test_size=0.2)

    # 数据标准化处理
    ss_x = StandardScaler()
    ss_y = StandardScaler()
    x_train = ss_x.fit_transform(x_train)
    x_test = ss_x.transform(x_test)
    y_train = ss_y.fit_transform(y_train)
    y_test = ss_y.transform(y_test)

    rfr = RandomForestRegressor()
    rfr.fit(x_train, y_train)
    rfr_y_predict = rfr.predict(x_test)
    return ss_y, y_test, rfr_y_predict

def output_LR_score(ss_y, y_test, lr_y_predict):
    print("LinearRegression模型的均方误差为：",
          mean_squared_error(ss_y.inverse_transform(y_test), ss_y.inverse_transform(lr_y_predict)))
    print("LinearRegression模型的R方得分为：", r2_score(y_test, lr_y_predict))
    return r2_score(y_test, lr_y_predict)

def output_RFR_score(ss_y, y_test, rfr_y_predict):
    print("随机森林模型的均方误差为：",
          mean_squared_error(ss_y.inverse_transform(y_test), ss_y.inverse_transform(rfr_y_predict)))
    print("随机森林模型的R方得分为：", r2_score(y_test, rfr_y_predict))
    return r2_score(y_test, rfr_y_predict)

#预测结果可视化
def visible_LR(ss_y, y_test, y_predict):
    plt.scatter(ss_y.inverse_transform(y_test), ss_y.inverse_transform(y_predict))
    x = np.linspace(0,50000,500)
    plt.plot(x,x,color='red',linestyle='--',linewidth=2.5)
    plt.xlim(0,50000)
    plt.ylim(0,50000)
    plt.title('线性回归模型的预测效果')
    plt.xlabel('真实值')
    plt.ylabel('预测值')
    # plt.savefig('LR_result.png')
    plt.show()

def visible_RFR(ss_y, y_test, y_predict):
    plt.scatter(ss_y.inverse_transform(y_test), ss_y.inverse_transform(y_predict))
    x = np.linspace(0, 50000, 500)
    plt.plot(x, x, color='red', linestyle='--', linewidth=2.5)
    plt.xlim(0, 50000)
    plt.ylim(0, 50000)
    plt.title('随机森林回归模型的预测效果')
    plt.xlabel('真实值')
    plt.ylabel('预测值')
    # plt.savefig('GBR_result.png')
    plt.show()

def LR_predict_price():
    data = get_feature()
    ss_y, y_test, lr_y_predict = LR_train_model(data)

    r2 =output_LR_score(ss_y, y_test, lr_y_predict)
    visible_LR(ss_y, y_test, lr_y_predict)
    return r2
def RFR_predict_price():
    data = get_feature()
    ss_y, y_test, rfr_y_predict = RFR_train_model(data)
    r2 =output_RFR_score(ss_y, y_test, rfr_y_predict)
    visible_RFR(ss_y, y_test, rfr_y_predict)
    return r2
#LR_predict_price()
#RFR_predict_price()