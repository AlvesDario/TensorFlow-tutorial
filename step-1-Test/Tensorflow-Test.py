import tensorflow as tf

with tf.compat.v1.Session() as sess:
    a = tf.constant(20)
    b = tf.constant(22)
    c = a + b
    print(f'a + b = {sess.run(c)}')
    sess.close()

