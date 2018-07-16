# Gravity on mars


import math
import matplotlib.pyplot as plt
import random

g = 3.711
noiselevel = 0.5

height = list(range(50))
time = [math.sqrt(2*i/g) + random.uniform(-noiselevel, noiselevel) for i in height]
fit = [math.sqrt(2*i/g) for i in height]

heighttransformed = [math.sqrt(h) for h in height]
fittransformed = [math.sqrt(2/g)*h for h in heighttransformed]


plt.plot(height, time, '.')
	# plt.plot(height, fit)
plt.xlabel('y [m]')
plt.ylabel('t [s]')
plt.savefig('gravity.png')
plt.show()


plt.plot(heighttransformed, time, '.')
plt.plot(heighttransformed, fittransformed)
plt.xlabel('z')
plt.ylabel('t [s]')
plt.text(1, 5, 't = 0.73 z + 0.023')
plt.savefig('gravitytransformed.png')
plt.show()
