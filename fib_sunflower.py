# by xiao Ling and Xin Chen, April 12, 2017

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

def fib(n):
    if n == -1:
        return 0
    elif n == 0:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def draw_spiral(O0, theta, n_max, ax, curl=1):
    def draw_arc(o, n):
        if n >= n_max:
            return 0
        flag = np.mod(n, 4)
        if flag == 0:
            translation = curl*np.array([np.sin(theta), -np.cos(theta)])
            start = theta
            stop = curl*np.pi/2 + theta
        elif flag == 1:
            translation = np.array([np.cos(theta), np.sin(theta)])
            start = curl*np.pi/2 + theta
            stop = curl*np.pi + theta
        elif flag == 2:
            translation = curl*np.array([-np.sin(theta), np.cos(theta)])
            start = curl*np.pi + theta
            stop = curl*3*np.pi/2 + theta
        elif flag == 3:
            translation = np.array([-np.cos(theta), -np.sin(theta)])
            start = curl*3*np.pi/2 + theta
            stop = curl*2*np.pi + theta
        r = fib(n)
        phi = np.linspace(start, stop, r*5)
        x, y = pol2cart(r, phi)
        x = x+o[0]
        y = y+o[1]        
        ax.plot(x,y,color="red",linewidth=3)
        draw_arc(o+translation*fib(n-1), n+1)
    draw_arc(O0, 0)
    
    
def main():
    f, ax = plt.subplots(figsize=[10.00,10.00])        
    ax.axis("equal")
    origin=np.array([0,0])
    n_max=10
    spiral_number=8
    # draw_spiral(origin, np.pi/3, 5, ax, curl=-1)    
    for theta in np.arange(0, 2*np.pi, 2*np.pi/spiral_number):
        draw_spiral(origin, theta, n_max, ax, curl=1)
    for theta in np.arange(0, 2*np.pi, 2*np.pi/spiral_number):
        draw_spiral(origin, theta, n_max, ax, curl=-1)    
    # ax.axis("off")
    ax.set_axis_bgcolor('white')
    # plt.axis([-70,30,-20,45])
    ax.set_xticks([])
    ax.set_yticks([])
    plt.savefig("fib_sunflower.png", dpi=500)
    plt.show()
main()
