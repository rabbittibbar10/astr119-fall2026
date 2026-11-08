import numpy as np
import matplotlib.pyplot as plt

# Generates some random data
xdata1 = range(100)
ydata1 = 100 * np.random.rand(len(xdata1))
ydata2 = 100 * np.random.rand(len(xdata1))

# Your plot here!
plt.figure(facecolor="lime")
plt.scatter(xdata1, ydata1, color="yellow", marker="*", s=225)
plt.scatter(xdata1, ydata2, color="brown", marker="v", s=144)
plt.gca().set_facecolor("magenta")
plt.grid(color="white", linewidth=3)
plt.title('some data', color="red", fontsize=25)
plt.xlabel('x axis', color="cyan")
plt.ylabel('Y AXIS', color="orange", fontsize=20)
plt.legend(['Dataset 1', 'Dataset 2'], loc="center")
plt.savefig("ugly_figure.png")




# # One example:
# plt.figure()
# plt.plot(xdata1, ydata1, marker="*")
# plt.plot(xdata1, ydata2, marker="*")
# plt.title('Some Data')
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.legend(['Dataset 1', 'Dataset 2'])
# plt.savefig("test_figure_1.png")


# # Another way to do this:
# fig, ax = plt.subplots(1)
# ax.plot(xdata1, ydata1, marker="o")
# ax.plot(xdata1, ydata2, marker="o")
# ax.set_title('Some Data')
# ax.set_xlabel('x axis')
# ax.set_ylabel('y axis')
# ax.legend(['Dataset 1', 'Dataset 2'])
# plt.savefig("test_figure_2.png")