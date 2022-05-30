#run cd documents/gurobi
#python3 facility.py

from itertools import product
import gurobipy as gp
from gurobipy import GRB
import numpy as np
import xlsxwriter as xl
import pandas as pd

# Import matrix from tables.py (put them in the same map)
from tables_volume import allowedPackaging
from tables_volume import volume
from tables_volume import partDemand
from tables_volume import packaging
from tables_volume import article_df

# Range of plants and warehouses
num_packaging = len(packaging)
num_parts = len(article_df)
#num_parts = len(partDemand)
n = 10

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
m.ModelSense = gp.GRB.MINIMIZE

# The objective function takes into consideration the utilizations and allowed packaging
obj1 = gp.quicksum(partDemand[k]*usedPackagingMatrix[l,k]*volume[l,k] for l in range(num_packaging) for k in range(num_parts))
obj2 = gp.quicksum(openPackaging[l] for l in range(num_packaging))
m.setObjective(obj1-obj2*0.00000001)

#constraints

# Every part must be assigned exactly one packaging
con1 = (sum(usedPackagingMatrix[l][k] for l in range(num_packaging)) == 1 for k in range(num_parts))
m.addConstrs(con1)

# Limit the number of packaging to n
con2 = (sum(openPackaging[l] for l in range(num_packaging)) <= n)
m.addConstr(con2)

con3 = (usedPackagingMatrix[l,k] <= openPackaging[l] for l in range(num_packaging) for k in range(num_parts))
m.addConstrs(con3)

con4 = (usedPackagingMatrix[l,k] <= allowedPackaging[l,k] for l in range(num_packaging) for k in range(num_parts))
m.addConstrs(con4)

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

tot_units = sum(partDemand)

results = (m.ObjVal/tot_units)*(pow(10,-9))
# Print solution
print('\nAverage waste per unit: %g m^3' % results)
print('SOLUTION:')
for l in range(num_packaging):
    if openPackaging[l].X > 0.99:
        print('Packaging %s used' % packaging[l])
        # print('  Parts in packaging %s : %g' %
        #               (packaging[l], gp.quicksum(usedPackagingMatrix[l,k] for k in range(num_parts))))
        for k in range(num_parts):
           if usedPackagingMatrix[l,k].X > 0:
               print('  Part %g use packaging %s' %
                     (k, packaging[l]))
    #else:
    #    print('Packaging %s not used!' % packaging[l])
box_selection = pd.DataFrame(usedPackagingMatrix.getAttr("x"))

# col = []
# row = []
# col_index = 0
# row_index = 0
#
# for a in articles:
#     col.append(f'Article {str(articles[col_index])}')
#     col_index += 1
#
# for p in packaging:
#     row.append(f'Box {str(packaging[row_index])}')
#     row_index += 1

def create_woorkbook():

    workbook = pd.ExcelWriter('Facility_Volume.xlsx', engine='xlsxwriter')

    box_selection.to_excel(workbook, sheet_name='Box Selection')

    workbook.close()

    box_selected = pd.read_excel('/Users/alexjette/Documents/GitHub/Exjobb/Facility_Volume.xlsx')
    print(box_selected)

create_woorkbook()
