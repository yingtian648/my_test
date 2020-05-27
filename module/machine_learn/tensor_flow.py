#!/user/bin/python3
# -*- codeing:utf-8 -*-
# Time : 2018/12/12 16:02
# Author : LiuShiHua
# Desc :
from tensorflow import Session, device, constant, matmul
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 日志等级 忽略warning


def test_first():
    '''构建一个只有两个constant做输入, 然后进行矩阵乘的简单图:'''

    # 如果不使用with session()语句, 需要手动执行session.close().
    # with device设备指定了执行计算的设备:
    #  "/cpu:0": 机器的 CPU.
    #  "/gpu:0": 机器的第一个 GPU, 如果有的话.
    #  "/gpu:1": 机器的第二个 GPU, 以此类推.

    with Session() as sess:  # 创建执行图的上下文
        with device('/cpu:0'):  # 指定运算设备
            mat1 = constant([[3, 3]])  # 创建源节点
            mat2 = constant([[2], [2]])
            product = matmul(mat1, mat2)  # 指定节点的前置节点, 创建图
            result = sess.run(product)  # 执行计算
            print(result)


if __name__ == "__main__":
    test_first()
