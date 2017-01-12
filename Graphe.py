import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import os

os.chdir("../result/")


file = open("sigma.txt", "r")


time = []
sigma = []

for lines in file:
	a = lines.split("\t")
	time.append(float(a[0]))

	a.pop(0)
	sigma.append(a)


sigma = np.array(sigma).astype(float)
time = np.array(time)

l = len(sigma[0,])


# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure(0)
ax = plt.axes(xlim=(-20, l+20), ylim=(sigma.min(), sigma.max()))
line, = ax.plot([], [], lw=2)

time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)


# initialization function: plot the background of each frame
def init():
	line.set_data([], [])

	time_text.set_text('')

	return line,

# animation function.  This is called sequentially
def animate(i):
	x = range(l)
	y = sigma[i,]
	line.set_data(x, y)

	time_text.set_text('time = %.1f s' % time[i])

	return line, time_text

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(time), interval=20, blit=True)




file.close()



### pour le fichier gene

'''

file = open("gene.txt", "r")

time = [0]
gene = []

lines = file.readline()

for lines in file:
	a = lines.split("\t")
	time.append(float(a[0]))

	a.pop(0)
	gene.append(a)


gene = np.array(gene).astype(float)
time = np.array(time)

print time
print gene


fig = plt.figure(1)
plt.axes()

exit()
'''
plt.show()


