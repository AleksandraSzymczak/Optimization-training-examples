import xpress as xp
from math import pi as PI

h = xp.var(vartype=xp.continuous, name='h')
d = xp.var(vartype=xp.continuous, name='d')

p = xp.problem()

p.addVariable(h)
p.addVariable(d)

p.addConstraint(d == 1)

p.setObjective((PI * h * d**2) / 4 - (PI * h**3) / 16, sense=xp.maximize)

p.optimize()

print("Optimal height (h):", p.getSolution()[0])
print("Optimal diameter (r):", (p.getSolution()[1]/2) - (p.getSolution()[0]/4))
print("Optimal volume:", (p.getSolution()[2]))

#***Visualisation part***
# import numpy as np
# import matplotlib.pyplot as plt

# h = p.getSolution()[0]
# r = (p.getSolution()[1]/2) - (p.getSolution()[0]/4)
# v = p.getSolution()[2]

# def func(h):
#     #we assume d is constant and d=1 but i could be any positive value
#     return (np.pi * h) / 4 - (np.pi * h**3) / 16

# h_values = np.linspace(-1, 3, 400)

# y = func(h_values)

# # Plot the function
# plt.figure(figsize=(8, 6))
# plt.plot(h_values, y, label=r'$f(h) = \frac{\pi h}{4} - \frac{\pi h^3}{16}$')
# plt.axhline(0, color='black', linewidth=0.5)
# plt.axvline(0, color='black', linewidth=0.5)
# plt.title('Plot of the function $f(h)$')
# plt.xlabel('h')
# plt.ylabel('f(h)')
# plt.legend()
# plt.grid(True)
# plt.scatter(h, v, color='red', label='Point')

# z = np.linspace(0, h, 100)
# theta = np.linspace(0, 2 * np.pi, 100)
# theta_grid, z_grid = np.meshgrid(theta, z)
# x_grid = r * np.cos(theta_grid)
# y_grid = r * np.sin(theta_grid)

# # Plotting the cylinder
# fig = plt.figure(figsize=(8, 6))
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(x_grid, y_grid, z_grid, color='b', alpha=0.6)

# # Set labels and title
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.set_title('Barrel with maximum volume for d = 1')

# ax.set_box_aspect([1, 1, 1])

# plt.show()