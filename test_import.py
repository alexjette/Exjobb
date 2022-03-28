from tables import allowedPackaging
from tables import utilization
from tables import packaging
import xlsxwriter as xl
import pandas as pd
import numpy as np

col = []
row = []
c = 0
for p in packaging:
    col.append(f'Part {packaging[c]}')
    row.append(f'Box {packaging[c]}')
    c += 1

checkPackaging = pd.DataFrame(allowedPackaging, columns=col)
checkPackaging.index = row
utilizationTable = pd.DataFrame(utilization, columns=col)
utilizationTable.index = row
print(checkPackaging)
print(utilizationTable)

def create_woorkbook():

    packagingRange = np.array([10, 20, 30, 40])
    a = -1
    workbook = pd.ExcelWriter('XTR_box.xlsx', engine='xlsxwriter')
    #workbook = xl.Workbook('XTR_box.xlsx')
    checkPackaging.to_excel(workbook, sheet_name='Check Packaging', index=row)
    utilizationTable.to_excel(workbook, sheet_name='Utilization Table', index=row)

    # for p in packagingRange:
    #     a = a + 1
    #     sheet_name = str(packagingRange[a])
    #     worksheet = workbook.add_worksheet(sheet_name + '%')

    workbook.close()

    box_data = pd.read_excel('/Users/alexjette/Documents/Exjobb/XTR_box.xlsx')
    print(box_data)

create_woorkbook()
