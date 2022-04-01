from tables import allowedPackaging
from tables import utilization
from tables import packaging
from tables import articles
from tables import partDemand
#from facility import usedPackagingMatrix
import xlsxwriter as xl
import pandas as pd
import numpy as np

col = []
row = []
col_index = 0
row_index = 0

for a in articles:
    col.append(f'Article {str(articles[col_index])}')
    col_index += 1

for p in packaging:
    row.append(f'Box {str(packaging[row_index])}')
    row_index += 1

demand_table = pd.DataFrame(partDemand, columns=['Demand'])
demand_table.index = col
#usedPackagingMatrix_1 = pd.DataFrame(usedPackagingMatrix.x, columns=col)
#usedPackagingMatrix_1.index = row
checkPackaging = pd.DataFrame(allowedPackaging, columns=col)
checkPackaging.index = row
utilizationTable = pd.DataFrame(utilization, columns=col)
utilizationTable.index = row
#print('Used Packaging: \n', usedPackagingMatrix_1)
#print('Check Packaging: \n', checkPackaging)
#print('Utilization: \n', utilizationTable)

def create_woorkbook():

    workbook = pd.ExcelWriter('XTR_box.xlsx', engine='xlsxwriter')

    checkPackaging.to_excel(workbook, sheet_name='Check Packaging', index=row)
    utilizationTable.to_excel(workbook, sheet_name='Utilization Table', index=row)
    #usedPackagingMatrix_1.to_excel(workbook, sheet_name='Used Packaging Table', index=row)
    demand_table.to_excel(workbook, sheet_name='Demand Table', index=col)

    workbook.close()

    box_data = pd.read_excel('/Users/alexjette/Documents/GitHub/Exjobb/XTR_box.xlsx')
    print(box_data)

create_woorkbook()
