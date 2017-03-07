import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

d_x = np.array([-2, -1, 0, 1, 2])
d_y = np.array([2, -1, 1, -1, 2])

v_a = tf.Variable(tf.zeros([1]))
v_b = tf.Variable(tf.zeros([1]))
v_c = tf.Variable(tf.zeros([1]))
v_d = tf.Variable(tf.zeros([1]))
v_e = tf.Variable(tf.zeros([1]))
v_y = v_a * d_x * d_x * d_x * d_x + v_b * d_x * d_x * d_x + v_c * d_x * d_x + v_d * d_x + v_e

loss = tf.reduce_mean(tf.square(v_y - d_y))
optimizer = tf.train.GradientDescentOptimizer(0.005)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()
session = tf.Session()
session.run(init)

data_xi = []
data_xa = []
data_xb = []
data_xc = []
data_xd = []
data_xe = []
for i in range(0, 10000):
    session.run(train)
    if i % 100 == 0:
        # data_xi.append(i)
        # data_xa.append(session.run(v_a))
        # data_xb.append(session.run(v_b))
        # data_xc.append(session.run(v_c))
        # data_xc.append(session.run(v_d))
        # data_xc.append(session.run(v_e))
        x = np.linspace(-2, 2, 400, endpoint=True)
        y = session.run(v_a) * x * x * x * x + session.run(v_b) * x * x * x + session.run(v_c) * x * x + session.run(v_d) * x + session.run(v_e)
        plt.plot(x, y)
        print(session.run(v_a), session.run(v_b), session.run(v_c), session.run(v_d), session.run(v_e))

# plt.plot(data_xi, data_xa)
# plt.plot(data_xi, data_xb)
# plt.plot(data_xi, data_xc)
# plt.plot(data_xi, data_xd)
# plt.plot(data_xi, data_xe)
plt.show()
# print(data)
