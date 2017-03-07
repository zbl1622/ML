import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

d_x = np.random.rand(100)
d_y = 2 * d_x * d_x - 7 * d_x + 3
print(d_x)
print(d_y)

v_a = tf.Variable(tf.zeros([1]))
v_b = tf.Variable(tf.zeros([1]))
v_c = tf.Variable(tf.zeros([1]))
v_y = d_x * d_x * v_a + d_x * v_b + v_c

loss = tf.reduce_mean(tf.square(v_y - d_y))
optimizer = tf.train.GradientDescentOptimizer(0.1)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()
session = tf.Session()
session.run(init)

data_xi = []
data_xa = []
data_xb = []
data_xc = []
for i in range(1, 10000):
    session.run(train)
    if i % 100 == 0:
        data_xi.append(i)
        data_xa.append(session.run(v_a))
        data_xb.append(session.run(v_b))
        data_xc.append(session.run(v_c))
        print(session.run(v_a), session.run(v_b), session.run(v_c))

plt.plot(data_xi,data_xa)
plt.plot(data_xi,data_xb)
plt.plot(data_xi,data_xc)
plt.show()
# print(data)
