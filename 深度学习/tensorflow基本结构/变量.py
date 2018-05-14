import tensorflow as tf
import numpy as np

'''
tf.random_normal:
正态分布
主要参数：平均值、标准差、取值类型

tf.truncated_normal:
正态分布，但如果随机出来的值偏离平均值超过2个标准差，那么这个数将会被重新随机
主要参数:平均值、标准差、取值类型

tf.random_uniform:
平均分布
主要参数:最小、最大取值，取值类型

tf.random_gamma
Gamma分布
主要参数:形状参数alpha、尺度参数beta、取值类型
'''

w=tf.Variable(tf.random_normal([2,3],stddev=2,mean=0,seed=1))
print("初始值为正太分布的变量-",w)

b=tf.Variable(tf.zeros([3]))
print("初始值为0且长度为3的变量",b)



