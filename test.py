

import tensorflow as tf

a = tf.Variable(tf.random_normal([5, 5], stddev=0.1,dtype="float32"),dtype=tf.float32)
print a 
b = tf.Print(a, [a], "a: ",summarize=6)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
# sess.run(a)
sess.run(b)

