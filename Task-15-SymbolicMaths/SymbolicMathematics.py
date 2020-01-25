#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import sympy as sy 
from sympy.interactive import printing
printing.init_printing(use_latex=True)
from sympy import *
from sympy.abc import x, y, a, b, c
from scipy import integrate


# In[4]:


def f(x):
	return 5*x**5 - 3*x**2 -17


# In[5]:


x = sy.Symbol('x')
a = sy.Function('a')(x)


# In[6]:


display(f(x))
sy.diff(f(x), x)


# In[7]:


display(f(x))
sy.integrate(f(x), x)


# In[8]:


ode_one = Eq(a.diff(x,x) - 5*a, 10)
display(ode_one)
dsolve(ode_one,a)


# In[9]:


g = Function('g')
u = g(x,y)
ux = u.diff(x)
uy = u.diff(y)
pde_one = a*ux + b*uy + c*u
display(pde_one)
pdsolve(pde_one)


# In[10]:


f = lambda x : x**2
integration = integrate.quad(f, 0 , 1)
print(integration)


# In[ ]:




