import tensorflow as tf;

v=tf.constant([1.0,2.0,3.0])
with tf.Session() as sess:
    print(sess.run(tf.log(v)))