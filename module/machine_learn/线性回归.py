#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/12/21 15:58
# Author : LiuShiHua
# Desc :

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# 生成1000个线性点
# 线性回归模型 y =W8x +b
num_points = 1000
vector_set = []
for i in range(num_points):
    x1 = np.random.normal(0.0, 0.55)
    y1 = x1 * 0.1 + 0.3 + np.random.normal(0.0, 0.3)
    vector_set.append(([x1, y1]))

x_data = [v[0] for v in vector_set]
y_data = [v[1] for v in vector_set]

plt.scatter(x_data, y_data, c='r')
plt.show()

# 生成一维的W矩阵，取值是[-1,1]之间的随机数
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0), name='W')
# 生成一维的b矩阵，取值是0
b = tf.Variable(tf.zeros([1]), name='B')
# 经过计算得出预估值y
y = W * x_data + b

# 以预估值y和实际值y_data之间的均方误差作为损失
loss = tf.reduce_mean(tf.square(y - y_data), name='loss')
# 采用梯度下降法来优化参数
optimizer = tf.train.GradientDescentOptimizer(0.5)
# 训练的过程就是最小化这个误差值
train = optimizer.minimize(loss, name='train')
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

print('W =', sess.run(W), "b =", sess.run(b), 'loss =', sess.run(loss))
for step in range(20):
    sess.run(train)
    print('W =', sess.run(W), "b =", sess.run(b), 'loss =', sess.run(loss))

plt.scatter(x_data,y_data,c='r')
plt.plot(x_data,sess.run(W)*x_data+sess.run(b))
plt.show()