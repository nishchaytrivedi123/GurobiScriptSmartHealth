#!/usr/bin/env python
# coding: utf-8

# In[39]:


import gurobipy as gb
from gurobipy import GRB, LinExpr


# In[40]:


# define model and add variable
model = gb.Model("test-drug")

x1 = model.addVar(vtype="Binary", name="x1")
x2 = model.addVar(vtype="Binary", name="x2")
x3 = model.addVar(vtype="Binary", name="x3")
x4 = model.addVar(vtype="Binary", name="x4")


# In[41]:


# set objective for model
model.setObjective(130*x1 + 95*x2 + 118*x3 + 83*x4, GRB.MINIMIZE)


# In[42]:


# add constraints
model.addConstr(x1+x2 == 1, "c0")
model.addConstr(x1+x3 == 1, "c1")
model.addConstr(x2+x4 == 1, "c2")
model.addConstr(x4+x3 == 1, "c4")


# In[43]:


# optimize the model
model.optimize()


# In[44]:


# final result of part 1
for i in model.getVars():
    print('%s %g' % (i.varName, i.x))
print('Optimal value: %g' % model.objVal)


# In[45]:


# import random
import numpy as np
np.random.seed(1997)
random_numbers = []

# create random numbers for 6x6
for i in range(0,36):
    random_numbers.append(np.random.randint(50,150))

random_numbers[18]= 130
random_numbers[19]= 95
random_numbers[24]= 118
random_numbers[25]= 83

print(random_numbers)


# In[46]:


# define model
var = model.addVars(6,6,vtype='B')


# In[47]:


# create variable list
var_list = []
for i in range(6):
    for j in range(6):
        var_list.append(var[i,j])


# In[48]:


#define model linear expression
lin_expr = LinExpr(random_numbers, var_list)
model.setObjective(lin_expr, GRB.MINIMIZE)
model.addConstrs(var.sum(i, '*') == 1 for i in [0,1,2,3,4,5])
model.addConstrs(var.sum('*',i) == 1 for i in [0,1,2,3,4,5])


# In[49]:


# finally optimize the model
model.optimize()


# In[50]:


# result
for i in model.getVars():
    print('%s %g' % (i.varName, i.x))
print('Optimal value: %g' % model.objVal)

