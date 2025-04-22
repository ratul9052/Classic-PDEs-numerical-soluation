import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# 1D wave equation
# u_tt = c^2 * u_xx domain (0,pi)
# u(x,0) = f(x)
# u_t(x,0) = g(x)
# u(0,t) = u(L,t) = 0

#physical domain
g=50
n=100
T=10
x=np.linspace(0,np.pi,g)
t=np.linspace(0,T,n)   
U=[]

#analytical soluation for c=1
def analytical_solution(x,t):
    u=np.sin(x)*(np.cos(t)+np.sin(t))
    return u


#neumerical soluation
u_0=np.sin(x)  #initial condition
dx=x[1]-x[0]
dt=0.01
T=10

print("cfl:", dt/dx)
n_sol=[]
a_sol=[]


n_sol.append(u_0)
a_sol.append(u_0)
a=0
while a<T:
    u_old=n_sol[-1]
    u_new=np.zeros_like(u_old)
    if len(n_sol)==1:
        u_new[1:-1]=u_old[1:-1] +dt*np.sin(x[1:-1]) + (((dt/dx)**2) * (u_old[2:] - 2*u_old[1:-1] + u_old[:-2]))/2
    
    else:
        u_pold=n_sol[-2]
        u_new[1:-1]=2*u_old[1:-1] - u_pold[1:-1] + (((dt/dx)**2) * (u_old[2:] - 2*u_old[1:-1] + u_old[:-2]))

    
    u_new[0]=0
    u_new[-1]=0
    n_sol.append(u_new)
    a_sol.append(analytical_solution(x,a))
    a+=dt





#PLOTING
ims = []
fig = plt.figure(figsize=[5,4], dpi=200)
plt.grid()
i = 0
for n in range(len(n_sol)):

    im1 = plt.plot(x,a_sol[n-1], 'x', color='b', markersize=2, animated=True)
    im2 = plt.plot(x,n_sol[n-1], '-', color='r', markersize=2, animated=True)
    #plt.ylim(-1.1, 1.1)
    ims.append(im2 + im1)


ani = animation.ArtistAnimation(fig, ims, interval=35, blit=True, repeat_delay=1000)
ani

#plt.plot(x,n_sol[3], '-o', color='r', markersize=2)

plt.show()




