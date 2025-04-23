import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import cm

#define domain
Lx=1
Ly=1
nx=51
ny=51
x=np.linspace(0,Lx,nx)
dx=x[1]-x[0]
y=np.linspace(0,Ly,ny)
dy=y[1]-y[0]

xx,yy=np.meshgrid(x,y)

#set up
p=np.zeros([ny,nx])
S=np.zeros([ny,nx])


#tolerance
tol=1e-5
error=1e10
max_it=1000
it=0

while error>tol and it<max_it:
    p_k=p.copy()

    #dirichle boundary condition
    p[0,:]=0.0#bottom wall
    p[-1,:]=0.0 #top wall
    p[:,-1]=0.0 #right wall
    p[:,0]=0.0 #left wall
    p[10:-10,0]=1.0 #left wall

    #neuman boundary condition
    # p[0,:]=p[1,:] -alpha*dy#bottom wall
    # p[-1,:]=p[-2,:]+alpha*dy #top wall
    # p[:,-1]=p[:,-2] +alpha*dx #right wall
    # p[:,0]=0.0 #left wall
    # p[10:-10,0]=1.0 #left wall

    for i in range(1, nx-1):
        for j in range(1, ny-1):
            #jecob iterative method
            p[j, i] = 1.0 / 2.0 / (dx * dx + dy * dy) * (dx * dx * dy * dy * S[j, i] + dy * dy * (p_k[j, i+1] + p_k[j, i-1])+ dx * dx * (p_k[j+1, i] + p_k[j-1, i]))

    diff = p - p_k #difference between current and previous iteration
    error = np.linalg.norm(diff, 2) #l2 norm of the difference

    it+=1

if it==max_it:
    print("soluation did not converge in: ",it,"iterations")
    print("error=",error)
else:
    print("solution converged in: ",it,"iterations")


#plotting 
plt.contourf(xx,yy,p,levels=50,cmap="jet")
plt.colorbar(label='p')
plt.show()