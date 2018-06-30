1. 训练集中每个样本减去同一个样本（eg第一个样本）可以将y=wx+b中的b消除掉，使用减去后的新样本进行训练，不必考虑b
2. 思路： 对目标函数和最大似然函数分别求二阶导，看是否恒大于等于0
3.
```
# -*- coding: utf-8 -*-

import numpy as np
from sklearn.cross_validation import train_test_split

def sigmoid(z):
    return 1 / (1+np.exp(-z))

def logistic_regression(theta, x, y, iteration, alpha, lmbd):
    for i in range(iteration):
        theta = theta - alpha*(np.dot(x.transpose(), (sigmoid(np.dot(x, theta))-y)) + lmbd*theta)/y.shape[0]
        cost = -1/y.shape[0] * (np.dot(y.transpose(), np.log(sigmoid(np.dot(x, theta)))) + np.dot((1-y).transpose(), np.log(1-sigmoid(np.dot(x, theta))))) + lmbd/(2*y.shape[0])*np.dot(theta.transpose(), theta)
        print(f'Iteration: {i}, cost: {cost}')
    return theta

def predict(theta, test):
    pred = np.zeros([test.shape[0], 1])
    for idx, value in enumerate(np.dot(test, theta)):
        if sigmoid(value) >= 0.5:
            pred[idx] = 1
        else:
            pred[idx] = 0
    return pred

def main():
    density=np.array([0.697,0.774,0.634,0.608,0.556,0.430,0.481,0.437,0.666,0.243,0.245,0.343,0.639,0.657,0.360,0.593,0.719]).reshape(-1,1)
    sugar_rate=np.array([0.460,0.376,0.264,0.318,0.215,0.237,0.149,0.211,0.091,0.267,0.057,0.099,0.161,0.198,0.370,0.042,0.103]).reshape(-1,1)
    xtrain=np.hstack((density,sugar_rate))
    xtrain=np.hstack((np.ones([density.shape[0],1]),xtrain))
    ytrain=np.array([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0]).reshape(-1,1)
    xtrain,xtest,ytrain,ytest=train_test_split(xtrain,ytrain,test_size=0.25,random_state=33)

    theta_init=np.random.rand(3,1)
    theta=logistic_regression(theta_init, xtrain, ytrain,200, 0.5, 0.01)
    pred = predict(theta, xtest)
    print('predictions are',pred)
    print('ground truth is',ytest)
    print('theta is ',theta)
    print('the accuracy is',np.mean(pred==ytest))

if __name__ == '__main__':
    main()
```

6. 通过将数据映射，使其在更高一维上可分；使用基于核方法的KLDA
9.  对于OvR，MvM来说，由于对每个类进行了相同的处理，其拆解出的二分类任务中类别不平衡的影响会相互抵消，因此通常不需要专门处理。
