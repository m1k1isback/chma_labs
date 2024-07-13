import matplotlib.pyplot as plt

plt.plot([0.5, 1, 1.5, 2, 2.5], [3.3, 5.9, 7, 6.3, 3.2], 'go--')
plt.bar([0.5, 1, 1.5, 2, 2.5], [2, 3.9, 4.5, 3.7, 1.2], width=0.3, color='red')
plt.xlabel('d', fontsize=24)
plt.ylabel('S,R', fontsize=24)
plt.title('Dependencies S(d) and R(d)', fontsize=24)
plt.grid(True)
plt.show()