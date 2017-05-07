import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def fractal(points,n_max):
    if len(points)>=4**n_max+1:
        return
    for k in range(len(points)-1):
        i=4*k
        A=points[i]
        B=points[i+1]
        P=2*A/3+B/3
        Q=A/3+2*B/3
        M=np.array([0.5*(B[0]-A[0])+0.288675*(A[1]-B[1]),
                   0.5*(B[1]-A[1])+0.288675*(B[0]-A[0])])
        M=M+A
        points.insert(i+1,Q)
        points.insert(i+1,M)
        points.insert(i+1,P)
    fractal(points,n_max)

n_max=6
points1=[np.array([0,0]),np.array([1,0])]
points2=[np.array([1/2,-0.866]),np.array([0,0])]
points3=[np.array([1,0]),np.array([1/2,-0.866])]
fractal(points1,n_max)
fractal(points2,n_max)
fractal(points3,n_max)

data1=np.array(points1).T
data2=np.array(points2).T
data3=np.array(points3).T
fig=plt.figure(figsize=[19.2,10.8])
ax=plt.subplot(1,1,1)
ax.set_axis_bgcolor('black')
ax.set_xticks([])
ax.set_yticks([])

ax.plot(data1[0],data1[1],"-",color="cyan", linewidth=3)
ax.plot(data2[0],data2[1],"-",color="cyan", linewidth=3)
ax.plot(data3[0],data3[1],"-",color="cyan", linewidth=3)

ax.axis("equal")
plt.axis([-0.2,1.2,-1,0.4])
# ax.axis("off")
plt.savefig("/Users/xinchen/Desktop/snowflake.png",format="png",dpi=1000)
plt.show()
