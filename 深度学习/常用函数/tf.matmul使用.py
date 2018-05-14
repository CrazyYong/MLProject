import tensorflow as tf

'''
矩阵乘法
'''
v1=tf.constant([[1.0,2.0],[3.0,4.0]])
v2=tf.constant([[5.0,6.0],[7.0,8.0]])
with tf.Session() as sess:
    print(sess.run(tf.matmul(v1,v2)))


'''
直接乘法，元素之间直接相乘
'''
with tf.Session() as sess:
    print(sess.run(v1*v2))