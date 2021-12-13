# Gradient Descent, Single Variable
# Followed tutorial by codebasics
# YouTube: https://youtu.be/vsWrXfO3wWw

import numpy as np

def gradient_descent(x, y):
	m_current = b_current = 0
	iterations = 10000
	n = len(x)
	# Play with learning rate to see what fits best
	learning_rate = 0.08

	for i in range(iterations):
		y_predicted = m_current * x + b_current
		cost = (1/n) * sum([value**2 for value in y - y_predicted])
		md = -(2/n) * sum(x*(y - y_predicted))
		bd = -(2/n) * sum(y - y_predicted)
		m_current = m_current - learning_rate * md
		b_current = b_current - learning_rate * bd
		print("m {}, b {}, cost {}, iteration {}".format(m_current, b_current, cost, i))

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

gradient_descent(x, y) 

# output is 
# m = 2.000000000000002, 
# b = 2.999999999999995
# cost 1.0255191767873153e-29