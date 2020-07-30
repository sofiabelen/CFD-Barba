import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
from matplotlib import cm
import seaborn as sns

u = np.loadtxt('Data/u12')
v = np.loadtxt('Data/v12')
P = np.loadtxt('Data/p12')
param = np.loadtxt('Parameters/input12')
exp_count = int(np.loadtxt('Parameters/counter')) - 1

dx = param[0]
dt = param[1]
dy = dx
nx = int(2.0 / dx)
ny = int(2.0 / dy)

print("exp_count: ", exp_count);
print("dx: ", dx)
print("dy: ", dy)
print("dt: ", dt)
print("nx: ", nx)
print("ny: ", ny)

u = u.reshape(nx, ny)
v = v.reshape(nx, ny)
P = P.reshape(nx, ny)
u = np.transpose(u)
v = np.transpose(v)
P = np.transpose(P)

x = np.linspace(0, 2, nx)
y = np.linspace(0, 2, ny)
x, y = np.meshgrid(x, y)

sns.set(context='talk', style='dark')

fig, ax = plt.subplots(figsize=(11, 7), dpi=100);
pos = ax.contourf(x, y, P, alpha=0.5, cmap=cm.viridis)
fig.colorbar(pos, ax=ax,\
        label='Pressure')
ax.contour(x, y, P, cmap=cm.viridis)
ax.quiver(x[::2, ::2], y[::2, ::2], u[::2, ::2], v[::2, ::2],\
        label='Velocity')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Channel Flow with Navier-Stokes')
ax.legend(loc='lower left')

fig.savefig(f'Images/12-exp{exp_count}.svg')
fig.savefig(f'Images/12-exp{exp_count}.png')
