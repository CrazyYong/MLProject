import tensorflow as tf

'''
tf.greater的输入是两个张量，此函数会比较这两个输入张量中每一个元素的大小，并返回比较结果。当
tf.greater的输入张量维度不一样时，TensorFlow会进行类似Numpy广播操作的处理。

tf.where函数有三个参数。第一个为选择条件根据，当选择为True时，tf.where函数会选择第二个参数中的
值，否则使用第三个参数中的值。注意的是 tf.where函数判断和选择都是在元素级别进行的
'''
v1=tf.constant([1.0,2.0,3.0,4.0])
v2=tf.constant([4.0,3.0,2.0,1.0])

with tf.Session() as sess:
    print(sess.run(tf.greater(v1,v2)))
    '''
    结果：[False False  True  True]
    '''

    print(sess.run(tf.where(tf.greater(v1,v2),v1,v2)))
    '''
    结果:[4. 3. 3. 4.]
    '''