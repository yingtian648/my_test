#!/user/bin/py thon3
# -*- codeing:utf-8 -*-
# Time : 2019/2/26 14:33
# Author : LiuShiHua
# Desc :
import tensorflow as tf
import numpy as np

sess = tf.Session()


def test_first():
    x_data = np.array([[1.,2.,3.],[3.,2.,6.]])
    x = tf.convert_to_tensor(x_data,dtype=tf.float32)
    print(x)


if __name__ == "__main__":
    test_first()
