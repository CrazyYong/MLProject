import tensorflow as tf
'''
tf.zeros
产生全0的数组
'''
a=tf.zeros([2,3],dtype=tf.int32)
print(a)

'''
tf.ones
产生全1的数组
'''
a=tf.ones([2,3],dtype=tf.int32)
print(a)

'''
tf.fill
产生一个全部给定数字的数组
'''
a=tf.fill([2,3],9)
print(a)

'''
tf.constant
产生一个给定值的常量
'''
a=tf.constant([1,2,3])
print(a)


with tf.Session() as sess:
    print(sess.run(a))