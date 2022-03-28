#run cd documents/gurobi
#python3 facility.py

#!/usr/bin/env python3.9

# Copyright 2022, Gurobi Optimization, LLC

# Facility location: a company currently ships its product from 5 plants
# to 4 warehouses. It is considering closing some plants to reduce
# costs. What plant(s) should the company close, in order to minimize
# transportation and fixed costs?
#
# Note that this example uses lists instead of dictionaries.  Since
# it does not work with sparse data, lists are a reasonable option.
#
# Based on an example from Frontline Systems:
#   http://www.solver.com/disfacility.htm
# Used with permission.

from itertools import product
import gurobipy as gp
from gurobipy import GRB
import numpy as np
# Importera matriserna från tables.py (behöver ligga i samma mapp)
from tables import allowedPackaging
from tables import utilization
from tables import partDemand
from tables import packaging

# Warehouse demand in thousands of units
#partDemand = [15, 18, 14, 20]

#packagingCapacity = [999, 999, 999, 999]
#packaging = [1, 2, 3, 4]

#Beräkna tillåtna emballage och utilization istället
#allowedPackaging = np.array([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])

# utilization = np.array([[0.95, 0.93, 0.45, 0.67],
#                 [0.67, 0.82, 0.35, 0.55],
#                 [0.79, 0.56, 0.12, 0.89],
#                 [0.55, 0.66, 0.53, 0.59]])

#print(utilization)

# Range of plants and warehouses
num_packaging = len(packaging)
num_parts = len(partDemand)
#size_matrix = list(product(range(num_packaging),range(num_parts)))

#print(size_matrix)
#print(num_packaging)
#print(num_parts)

# Model
m = gp.Model("facility")

# Plant open decision variables: open[p] == 1 if plant p is open.
openPackaging = m.addVars(num_packaging,
                 vtype=GRB.BINARY,
                 name="open")

# Transportation decision variables: transport[w,p] captures the
# optimal quantity to transport to warehouse w from plant p
#usedPackagingMatrix = m.addVars(range(num_packaging),
#                                range(num_parts),
#                                vtype=GRB.BINARY,
#                                name="utilization rate")


usedPackagingMatrix = m.addMVar((num_packaging,num_parts),vtype=GRB.BINARY, name="utilization rate")

# You could use Python looping constructs and m.addVar() to create
# these decision variables instead.  The following would be equivalent
# to the preceding two statements...
#
# open = []
# for p in plants:
#     open.append(m.addVar(vtype=GRB.BINARY,
#                          obj=fixedCosts[p],
#                          name="open[%d]" % p))
#
# transport = []
# for w in warehouses:
#     transport.append([])
#     for p in plants:
#         transport[w].append(m.addVar(obj=transCosts[w][p],
#                                      name="trans[%d,%d]" % (w, p)))

# The objective is to minimize waste / maximize utilization
m.ModelSense = gp.GRB.MAXIMIZE

#obj = gp.quicksum(usedPackagingMatrix[l,k]*utilization[l,k] for l in range(num_packaging) for k in range(num_parts))

obj1 = gp.quicksum(openPackaging[l]*usedPackagingMatrix[l,k]*utilization[l,k] for l in range(num_packaging) for k in range(num_parts))

m.setObjective(obj1)

#constraints

#Alla artiklar ska ha ett emballage
con1 = (sum(usedPackagingMatrix[l][k] for l in range(num_packaging)) == 1 for k in range(num_parts))
m.addConstrs(con1)

con2 = (sum(openPackaging[l] for l in range(num_packaging)) <= 2)
#Begränsa antalet emballage
m.addConstr(con2)




# Production constraints
# Note that the right-hand limit sets the production to zero if the plant
# is closed
#m.addConstrs(
#    (transport.sum('*', p) <= capacity[p]*open[p] for p in plants), "Capacity")

# Using Python looping constructs, the preceding would be...
#
# for p in plants:
#     m.addConstr(sum(transport[w][p] for w in warehouses)
#                 <= capacity[p] * open[p], "Capacity[%d]" % p)

# Demand constraints
#m.addConstrs(
#    (transport.sum(w) == demand[w] for w in warehouses),
#    "Demand")

# ... and the preceding would be ...
# for w in warehouses:
#     m.addConstr(sum(transport[w][p] for p in plants) == demand[w],
#                 "Demand[%d]" % w)

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
        print('Packaging %s used' % l)
        for k in range(num_parts):
            if usedPackagingMatrix[l,k].X > 0:
                print('  Part %g use packaging %s' %
                      (k, l))
    else:
        print('Packaging %s not used!' % l)
