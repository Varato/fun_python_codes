# by xiao Ling and Xin Chen, April 11, 2017

import numpy as np
import matplotlib.pyplot as plt

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

def draw_arc(Origin, r, flag, ax):

    if flag==0:
        start = 0
        end = np.pi/2
        w = r
        h = r
        
    elif flag==1:
        start = np.pi/2
        end = np.pi
        w = -r
        h = r

    elif flag==2:
        start = np.pi
        end = 3*np.pi/2
        w = -r
        h = -r

    elif flag==3:
        start = 3*np.pi/2
        end = 2*np.pi
        w = r
        h = -r

    theta=np.linspace(start, end, r*500)
    r=np.array([r]*len(theta))
    x, y = pol2cart(r, theta)
    x = x+Origin[0]
    y = y+Origin[1]
    ax.plot(x,y,color="red",linewidth=1)
    ax.plot([Origin[0], Origin[0]+w, Origin[0]+w, Origin[0], Origin[0]], 
    	[Origin[1], Origin[1], Origin[1]+h, Origin[1]+h, Origin[1]], color="white", linewidth=1)
    
def fib_recursive(n):
    if n == -1:
        return 0
    elif n == 0:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)
    
def main(n_max):
    f, ax = plt.subplots(figsize=[28.80,10.00])
    origin=np.array([0,0])
    for n in range(n_max):
        flag = np.mod(n,4)
        r=fib_recursive(n)
        draw_arc(origin, r, flag, ax)
        if flag == 0:
            origin = origin + np.array([0, -1])*fib_recursive(n-1)
        elif flag == 1:
            origin = origin + np.array([1, 0])*fib_recursive(n-1)
        elif flag == 2:
            origin = origin + np.array([0, 1])*fib_recursive(n-1)
        else:
            origin = origin + np.array([-1, 0])*fib_recursive(n-1)
            
    ax.axis("equal")
    # ax.axis("off")
    ax.set_axis_bgcolor('black')
    plt.axis([-70,30,-20,45])

    ax.set_xticks([])
    ax.set_yticks([])
    plt.savefig("fib_spiral.png", dpi=200)
    plt.show()
main(10)
