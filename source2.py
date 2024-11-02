import matplotlib.pyplot as plt
import numpy as np

c = np.linspace(0, 10, 1000)
w = np.linspace(0, 10, 1000)

# plot
fig, ax = plt.subplots()

plt.grid(True)
plt.xticks(np.arange(0, 11, 1))
plt.yticks(np.arange(0, 11, 1))

# draw constraints
plt.plot(c, 7.0 - c, color='b', label='c + w <= 7')  # constraint 3
plt.plot(c, 4.0 / 0.7 - (0.75 / 0.7) * c, color='r', label='0.75c + 0.7w >= 4')  # constraint 2
plt.plot(c, 0.65 / 0.15 - (0.1 / 0.15) * c, color='g', label='0.1c + 0.15w >= 0.65')  # constraint 1

plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel('Amount of c')
plt.ylabel('Amount of w')

# fill in the feasible region
plt.fill_between(c, np.maximum(0.65 / 0.15 - (0.1 / 0.15) * c, 4.0 / 0.7 - (0.75 / 0.7) * c), 7.0 - c, color='yellow', alpha=0.75)
plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)

# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.show()
