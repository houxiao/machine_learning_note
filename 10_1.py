
import numpy as np
import matplotlib.pyplot as plt

data = np.array([
                [0.697,0.460,1],[0.774,0.376,1],[0.634,0.264,1],[0.608,0.318,1],[0.556,0.215,1],
                [0.403,0.237,1],[0.481,0.149,1],[0.437,0.211,1],[0.666,0.091,0],[0.243,0.267,0],
                [0.245,0.057,0],[0.343,0.099,0],[0.639,0.161,0],[0.657,0.198,0],[0.360,0.370,0],
                [0.593,0.042,0],[0.719,0.103,0]
                ])
a = np.arange(0, 1.01, 0.01)
b = np.arange(0, 0.61, 0.01)

def kNN(train, test, k):
    res = []
    for i in range(len(test)):
        dist = []
        for j in range(len(train)):
            dist.append([j, np.linalg.norm(test[i,:]-train[j,:-1])])
        min_id = sorted(dist, key=lambda x: x[1])[:k]
        rate = [train[i[0], -1] for i in min_id]
        if sum(rate) / k >= 0.5:
            res.append(1)
        else:
            res.append(0)
    return res

x, y = np.meshgrid(a, b)
k = 1
z = kNN(data, np.c_[x.ravel(), y.ravel()], k)
z = np.array(z).reshape(x.shape)
fig = plt.figure()
ax = plt.gca()
label_map = {1:'good', 0:'bad'}
ax.scatter(data[:,0], data[:,1], c=data[:,2], cmap=plt.cm.Dark2)
ax.set_xlim(0, 1)
ax.set_ylim(0, 0.6)
ax.set_ylabel('sugar')
ax.set_xlabel('density')
ax.set_title('decision boundary: %s-NN' % k)
plt.show()