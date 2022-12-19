import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
def ana():
    data = pd.read_csv('2010-2011四家公司数据.csv', encoding='gbk')
    score = []
    for i in data['比分'].tolist():
        score.append(i.replace('月', '-').replace('日', ''))
    listScore = []
    for i in score:
        a = i.split('-', 1)[0]
        b = i.split('-', 1)[1]
        if a == b:
            listScore.append(0)
        elif a > b:
            listScore.append(1)
        elif a < b:
            listScore.append(-1)
    data['score'] = listScore
    data['score'].astype(int)
    homeRank = data['主场排名'].astype(str).tolist()
    awayRank = data['客场排名'].astype(str).tolist()
    rankHome = []
    rankAway = []
    for i in homeRank:
        rankHome.append(i.replace('英冠', ''))
    for i in awayRank:
        rankAway.append(i.replace('英冠', ''))
    data['主场排名'] = rankHome
    data['客场排名'] = rankAway
    data['rankD'] = data['主场排名'].astype(int) - data['客场排名'].astype(int)
    rankD = []
    for i in data['rankD'].tolist():
        if i < 0:
            i = -i
        rankD.append(i)
    data['rankD'] = rankD

    data = data[['主场排名', '客场排名', 'rankD', '初盘_胜率_主', '初盘_胜率_和', '初盘_胜率_客','score']].astype(float)
    sns.pairplot(data, vars=['初盘_胜率_主', '初盘_胜率_和', '初盘_胜率_客'],diag_kind= 'kde',hue ='score',kind= 'reg')
    x = data[['主场排名', '客场排名', 'rankD', '初盘_胜率_主', '初盘_胜率_和', '初盘_胜率_客']].values
    y = data['score'].values
    print(np.corrcoef(data,rowvar=False))
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    svm_model = SVC(kernel='rbf').fit(X_train,   y_train)
    pred1 = svm_model.predict(X_train)
    accuracy1 = accuracy_score(y_train, pred1)
    print('在训练集上的精确度: %.4f' % accuracy1)
    pred2 = svm_model.predict(X_test)
    accuracy2 = accuracy_score(y_test, pred2)
    print('在测试集上的精确度: %.4f' % accuracy2)


if __name__ == '__main__':
    # files = ['2010-2011四家公司数据.csv', '2011-2012四家公司数据.csv', '2012-2013四家公司数据.csv',
    #          '2013-2014四家公司数据.csv',
    #          '2014-2015四家公司数据.csv', '2015-2016四家公司数据.csv', '2016-2017四家公司数据.csv',
    #          '2018-2019四家公司数据.csv',
    #          '2019-2020四家公司数据.csv', '2020-2021四家公司数据.csv']
    # for i in files:
    print('-'*50)
    ana()
