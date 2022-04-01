#run cd documents/gurobi
#python3 facility.py

from itertools import product
import gurobipy as gp
from gurobipy import GRB
import numpy as np

# Import matrix from tables.py (put them in the same map)
from tables import allowedPackaging
from tables import utilization
from tables import partDemand
from tables import packaging
from tables import article_df

# Range of plants and warehouses
num_packaging = len(packaging)
num_parts = len(article_df)
#num_parts = len(partDemand)
n = 2

# Model
m = gp.Model("facility")
#m.setParam('TimeLimit', 100)

# Packaging decision variables: openPackaging[l] == 1 if packaging l is used.
openPackaging = m.addVars(num_packaging,
                 vtype=GRB.BINARY,
                 name="open")
# Used packaging decision variables: usedPackagingMatrix[l,k] == 1 if part k use packaging l
usedPackagingMatrix = m.addMVar((num_packaging,num_parts),vtype=GRB.BINARY, name="utilization_rate")

# objective

# The objective is to minimize waste / maximize utilization
m.ModelSense = gp.GRB.MAXIMIZE

# The objective function takes into consideration the utilizations and allowed packaging
obj1 = gp.quicksum(openPackaging[l]*usedPackagingMatrix[l,k]*utilization[l,k]*allowedPackaging[l,k] for l in range(num_packaging) for k in range(num_parts))
obj2 = gp.quicksum(openPackaging[l] for l in range(num_packaging))
m.setObjective(obj1-obj2*0.00000001)

#constraints

# Every part must be assigned exactly one packaging
con1 = (sum(usedPackagingMatrix[l][k] for l in range(num_packaging)) == 1 for k in range(num_parts))
m.addConstrs(con1)

# Limit the number of packaging to n
con2 = (sum(openPackaging[l] for l in range(num_packaging)) <= n)
m.addConstr(con2)

# Vary the number of packaging (n) here?
# Re-write model and re-do optimization for new n
# Loop for n here
# n needs to be changed before adding con2 to the model

# Save model
m.write('facilityPY.lp')

# Guess at the starting point: close the plant with the highest fixed costs;
# open all others

# First open all plants
for l in range(num_packaging):
    openPackaging[l].Start = 1.0

# Now close the plant with the highest fixed cost
#print('Initial guess:')
#maxFixed = max(fixedCosts)
#for p in plants:
#    if fixedCosts[p] == maxFixed:
#        open[p].Start = 0.0
#        print('Closing plant %s' % p)
#        break
#print('')

# Use barrier to solve root relaxation
m.Params.Method = 2

# Solve
m.optimize()

results = m.ObjVal/num_parts
# Print solution
print('\nAverage utilization: %g' % results)
print('SOLUTION:')
for l in range(num_packaging):
    if openPackaging[l].X > 0.99:
        print('Packaging %s used' % packaging[l])
#        print('  Parts in packaging %s : %g' %
#                      (packaging[l], gp.quicksum(usedPackagingMatrix[l,k] for k in range(num_parts))
        #for k in range(num_parts):
        #    if usedPackagingMatrix[l,k].X > 0:
        #        print('  Part %g use packaging %s' %
        #              (k, packaging[l]))
    #else:
    #    print('Packaging %s not used!' % packaging[l])
