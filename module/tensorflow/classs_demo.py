#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2019/9/18 11:12
# Author : LiuShiHua
# Desc :
from __future__ import absolute_import, division, print_function, unicode_literals

# 导入TensorFlow和tf.keras
import tensorflow as tf
from tensorflow import keras

# 导入辅助库
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
train_images.shape
print(len(train_labels))
test_images.shape
print(len(test_images))
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()
train_images = train_images / 255.0
test_images = test_images / 255.0
plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()
# 设置神经网络层
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])
# 编译模型
model.compile(optimizer='adam',  # 优化器
              loss='sparse_categorical_crossentropy',  # 损失函数
              metrics=['accuracy'])  # 评价方式 （衡量指标）
# 训练模型
"""
将训练数据提供给模型 - 在本案例中，他们是train_images和train_labels数组。
模型学习如何将图像与其标签关联
我们使用模型对测试集进行预测, 在本案例中为test_images数组。我们验证预测结果是否匹配test_labels数组中保存的标签。
通过调用model.fit方法来训练模型 — 模型对训练数据进行"拟合"。
"""
model.fit(train_images, train_labels, epochs=5)
# 评估准确率
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)
# 进行预测
predictions = model.predict(test_images)
predictions[0]
# 置信度最高的图片
np.argmax(predictions[0])
# 列出标签
test_labels[0]
