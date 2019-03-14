import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn import svm
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np
def LinearPridict():    #使用户型，次级区域，面积对整租价格进行线性回归预测
      house = pd.read_csv('./DATA/58E.csv', encoding='gbk')
      district = pd.get_dummies(house['CiJiQuYu'], prefix='CiJiQuYu')
      huxing=pd.get_dummies(house['Huxing'], prefix='Huxing')
      data = pd.concat([house, district,huxing], axis=1)
      area=house['MianJi']
      data.drop(['DanJia','MianJi','CiJiQuYu','LeiXing','Huxing','ZhuangXiu','FangXiang','GaoDi','LouCeng','XiaoQuName','QuYuName','XiangXiDiZhi','XiangQing','LiangDian','MiaoShu','link','YuanYue','PayWay'], axis=1, inplace=True)
      data['MianJi']=area
      print(data.head())
      x = data.as_matrix()[:, 1:]
      y = data.as_matrix()[:, 0].reshape(-1, 1)

      # 数据分割，随机采样25%作为测试样本，其余作为训练样本
      x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=40, test_size=0.25)

      # 数据标准化处理
      ss_x = StandardScaler()
      ss_y = StandardScaler()
      x_train = ss_x.fit_transform(x_train)
      x_test = ss_x.transform(x_test)
      y_train = ss_y.fit_transform(y_train)
      y_test = ss_y.transform(y_test)

      lr = LinearRegression()     #初始化
      lr.fit(x_train, y_train)    #训练数据
      lr_y_predict = lr.predict(x_test)

      print("LinearRegression模型的均方误差为：",
            mean_squared_error(ss_y.inverse_transform(y_test), ss_y.inverse_transform(lr_y_predict)))
      print("LinearRegression模型的R方得分为：", r2_score(y_test, lr_y_predict))
      plt.scatter(ss_y.inverse_transform(y_test), ss_y.inverse_transform(lr_y_predict))
      x = np.linspace(0, 300000, 10000)
      plt.plot(x, x, color='red', linestyle='--', linewidth=2.5)
      plt.xlim(0, 300000)
      plt.ylim(0, 300000)
      plt.title('线性回归模型的预测效果')
      plt.xlabel('真实值')
      plt.ylabel('预测值')
      plt.show()
#LinearPridict()

def svrpredict():
      house = pd.read_csv('./DATA/58E.csv', encoding='gbk')
      district = pd.get_dummies(house['CiJiQuYu'], prefix='CiJiQuYu')
      zhuangxiu=pd.get_dummies(house['ZhuangXiu'], prefix='ZhuangXiu')
      huxing=pd.get_dummies(house['Huxing'], prefix='Huxing')
      fangxiang=pd.get_dummies(house['FangXiang'], prefix='FangXiang')
      data = pd.concat([house, district,huxing,zhuangxiu,fangxiang], axis=1)
      area=house['MianJi']
      data.drop(['DanJia','MianJi','CiJiQuYu','LeiXing','Huxing','ZhuangXiu','FangXiang','GaoDi','LouCeng','XiaoQuName','QuYuName','XiangXiDiZhi','XiangQing','LiangDian','MiaoShu','link','YuanYue','PayWay'], axis=1, inplace=True)
      data['MianJi']=area
      print(data.head())
      x = data.as_matrix()[:, 1:]
      y = data.as_matrix()[:, 0].reshape(-1, 1)

      # 数据分割，随机采样25%作为测试样本，其余作为训练样本
      x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=40, test_size=0.25)

      # 数据标准化处理
      ss_x = StandardScaler()
      ss_y = StandardScaler()
      x_train = ss_x.fit_transform(x_train)
      x_test = ss_x.transform(x_test)
      y_train = ss_y.fit_transform(y_train)
      y_test = ss_y.transform(y_test)
      svmpr=svm.SVR()
      svmpr.fit(x_train, y_train)
      svmpr_y_pridict=svmpr.predict(x_test)
      print("SVR模型的均方误差为：",
                  mean_squared_error(ss_y.inverse_transform(y_test), ss_y.inverse_transform(svmpr_y_pridict)))
      print("SVR模型的R方得分为：", r2_score(y_test, svmpr_y_pridict))
      plt.scatter(ss_y.inverse_transform(y_test), ss_y.inverse_transform(svmpr_y_pridict))

#svrpredict()