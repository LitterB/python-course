import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

#plt.scatter(x_values, y_values, s=10)
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#plt.show()
plt.savefig("cubes_plot.png", bbox_inches='tight')