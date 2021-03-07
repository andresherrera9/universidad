# 2-D unsteady heat equation
# df/dt = alpha*d2f/dx2 + d2f/dy2 + S
# Forward Euler, central difference.
# Finite difference
# Points on boundaries, solve interior points.
# BC = 0; IC = 0

from numpy                import *
from matplotlib.pyplot    import *
from mpl_toolkits.mplot3d import *
from math                 import *
#from time                 import sleep

Ld       = 1.0                  # domain length
nTauRun  = 0.5                  # # of diffusion timescales to run
nxy      = 22                   # # of uniform grid points in x, y
alpha    = 10.0                 # thermal diffusivity
cfl      = 0.5                  # time step factor

tau  = Ld**2/alpha              # domain diffusion timescale
tend = nTauRun*tau              # run time
dxy  = Ld/(nxy-1)               # grid spacing
dt   = dxy**2/alpha/4*cfl       # time step size
nt   = ceil(tend/dt)            # number of time steps
dt   = tend/nt                  # clean it up
np   = ceil(1/cfl)*10           # how often to plot?

f = zeros((nt,nxy,nxy))         # initialize the solution
S = ones((nt,nxy,nxy))          # set the source term

X,Y = meshgrid(linspace(0,Ld,nxy),linspace(0,Ld,nxy))  # for plotting
i = arange(1,nxy-1)
j = i

for it in arange(1,nt):
    f[it][ix_(i,j)] = f[it-1][ix_(i,j)] \
                    + (alpha*dt/dxy**2)*(f[it-1][ix_(i-1,j)]-2*f[it-1][ix_(i,j)]+f[it-1][ix_(i+1,j)]) \
                    + (alpha*dt/dxy**2)*(f[it-1][ix_(i,j-1)]-2*f[it-1][ix_(i,j)]+f[it-1][ix_(i,j+1)]) \
                    + S[it-1][ix_(i,j)]

contourf(X,Y,f[it,:,:],20)
show()
