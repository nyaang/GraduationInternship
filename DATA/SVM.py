import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import mean_squared_error, r2_score
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体


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
# data['室'] = shi
# data['厅'] = ting
# data['卫'] = wei
#显示所有列
pd.set_option('display.max_columns', None)

print(data.head())

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

score = []
import numpy as np
for c in np.arange(0.1,100,0.5):
    s = svm.SVR(kernel='rbf',C=c)
    s.fit(x_train, y_train.ravel().astype('int'))
    s_y_predict = s.predict(x_test)
    score.append(r2_score(y_test, s_y_predict))

print(score)
from matplotlib import pyplot as plt
i = 0
c = 0
max_score = 0
C = np.arange(0.1,100,0.5)
while i<len(score):
    if max_score < score[i]:
        max_score = score[i]
        c = C[i]
    i += 1

print(c, max_score)
plt.plot(np.arange(0.1,100,0.5), score)
plt.vlines(c, 0, 1, 'red', label='最大值')
plt.title('支持向量机-线性核不同C值对结果的影响')
plt.xlabel('C')
plt.ylabel('R2-score')
plt.legend()
plt.savefig('SVM_linear.png')
plt.show()


# print("accuracy is:",s.score(x_test, y_test))
# print("LinearRegression模型的均方误差为：",
#       mean_squared_error(ss_y.inverse_transform(y_test), ss_y.inverse_transform(s_y_predict)))
# print("LinearRegression模型的R方得分为：", r2_score(y_test, s_y_predict))
