import numpy as np
from sympy import *
import random 
# xp, xa, yp, ya=symbols('xp xa yp ya')
# #in PCA we minimize the perpendicular diff
# loss=sqrt((xp-xa)**2 +(yp-ya)**2)
# m, c=symbols('m c')
# pred=m*xp+c 
# #too confusing to do our own way of PCA without actually doing PCA, some other day maybe

# #let's just do linear regression 


x, y, w, c=symbols('x y w c')
loss=(y-w*x-c)**2
diff_loss_w=diff(loss, w)
diff_loss_c=diff(loss, c)
mx=np.array([i+1 for i in range(1000)])
my=np.array([4*(i+1)+17+ random.randint(-3, 3) for i in range(1000)])

#maybe the ideal w=4, and c=17

from sympy.utilities.lambdify import lambdify
w=0
c=0
alpha=0.1
sqe=lambdify([x, y],np.sum((y-w*x+c)**2))
while (sqe(mx, my)<0.00001):
    temp=w+alpha*diff_loss_w()







