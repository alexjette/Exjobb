import numpy as np
import pandas as pd
from pandas_datareader import data as wb

# Hämtar excelfilerna
article_data = pd.read_excel('Batchsnurra.xlsx', 'Lagerdata')
boxes_data = pd.read_excel('Batchsnurra.xlsx', 'Boxtype')

# Gör excelfilerna till pandas.DataFrame
article_df = pd.DataFrame(article_data)
boxes_df = pd.DataFrame(boxes_data)
#print(boxes_df)
# Skapar två nollmatriser med antal rader = antar lådor och kolumner = antal artiklar (rader, kolumner)
allowedPackaging = np.zeros((len(boxes_df),len(article_df)))
utilization = np.zeros((len(boxes_df),len(article_df)))

# Skapar indexvariabler
box_index = -1
article_index = -1

# En forloop som ittererar över respektive låda
for index, row in boxes_df.iterrows():
    # Skapar variabler för låd-dimensioner som används i nästa forloop
    box_height = row['height']
    box_width = row['width']
    box_length = row['length']
    # Ökar lådindex med 1 för varje itteration
    box_index += 1
    # Ittererar igenom alla artiklar för respektive låda för att se vilka artiklar som får plats
    for index, row in article_df.iterrows():
        # Ökar artikelindex med 1 för varje itteration
        article_index += 1
        # Artikelindex nollställs för varje ny rad, dvs att när man ittererat igenom alla artiklar för en låda så ska det börja om när man kollar nästa låda
        if article_index >= len(article_df):
            article_index = 0
        # För given låda och artikel testas de 6 kombinationer av intresse för att avgöra om artiklen kan få plats i lådan
        if box_height > row['height'] and box_width > row['width'] and box_length > row['length']:
            allowedPackaging[box_index, article_index] = 1
            if ((row['height'] * row['width'] * row['length'] * row['Capacity']) / (box_height * box_width * box_length)) <= 1:
                utilization[box_index, article_index] = (row['height'] * row['width'] * row['length'] * row['Capacity']) / (box_height * box_width * box_length)
            else:
                utilization[box_index, article_index] = 0
            # print('OK', box_height, box_width, box_length, row['height'], row['width'], row['length'], row['Capacity'])
            # print(box_height * box_width * box_length, row['height'] * row['width'] * row['length'] * row['Capacity'])
        elif box_height > row['length'] and box_width > row['width'] and box_length > row['height']:
            allowedPackaging[box_index, article_index] = 1
            if ((row['height'] * row['width'] * row['length'] * row['Capacity']) / (box_height * box_width * box_length)) <= 1:
                utilization[box_index, article_index] = (row['height'] * row['width'] * row['length'] * row['Capacity']) / (box_height * box_width * box_length)
            else:
                utilization[box_index, article_index] = 0
            # print('OK', box_height, box_width, box_length, row['height'], row['width'], row['length'], row['Capacity'])
            # print(box_height * box_width * box_length, row['height'] * row['width'] * row['length'] * row['Capacity'])
        elif box_height > row['width'] and box_width > row['height'] and box_length > row['length']:
            allowedPackaging[box_index, article_index] = 1
            if ((row['height'] * row['width'] * row['length'] * row['Capacity']) / (box_height * box_width * box_length)) <= 1:
                utilization[box_index, article_index] = (row['height'] * row['width'] * row['length'] * row['Capacity']) / (box_height * box_width * box_length)
            else:
                utilization[box_index, article_index] = 0
            # print('OK', box_height, box_width, box_length, row['height'], row['width'], row['length'], row['Capacity'])
            # print(box_height * box_width * box_length, row['height'] * row['width'] * row['length'] * row['Capacity'])
        elif box_height > row['length'] and box_width > row['height'] and box_length > row['width']:
            allowedPackaging[box_index, article_index] = 1
            if ((row['height'] * row['width'] * row['length'] * row['Capacity']) / (box_height * box_width * box_length)) <= 1:
                utilization[box_index, article_index] = (row['height'] * row['width'] * row['length'] * row['Capacity']) / (box_height * box_width * box_length)
            else:
                utilization[box_index, article_index] = 0
            # print('OK', box_height, box_width, box_length, row['height'], row['width'], row['length'], row['Capacity'])
            # print(box_height * box_width * box_length, row['height'] * row['width'] * row['length'] * row['Capacity'])
        elif box_height > row['width'] and box_width > row['length'] and box_length > row['height']:
            allowedPackaging[box_index, article_index] = 1
            if ((row['height'] * row['width'] * row['length'] * row['Capacity']) / (box_height * box_width * box_length)) <= 1:
                utilization[box_index, article_index] = (row['height'] * row['width'] * row['length'] * row['Capacity']) / (box_height * box_width * box_length)
            else:
                utilization[box_index, article_index] = 0
            # print('OK', box_height, box_width, box_length, row['height'], row['width'], row['length'], row['Capacity'])
            # print(box_height * box_width * box_length, row['height'] * row['width'] * row['length'] * row['Capacity'])
        elif box_height > row['height'] and box_width > row['length'] and box_length > row['width']:
            allowedPackaging[box_index, article_index] = 1
            if ((row['height'] * row['width'] * row['length'] * row['Capacity']) / (box_height * box_width * box_length)) <= 1:
                utilization[box_index, article_index] = (row['height'] * row['width'] * row['length'] * row['Capacity']) / (box_height * box_width * box_length)
            else:
                utilization[box_index, article_index] = 0
            # print('OK', box_height, box_width, box_length, row['height'], row['width'], row['length'], row['Capacity'])
            # print(box_height * box_width * box_length, row['height'] * row['width'] * row['length'] * row['Capacity'])
        #else:
            #print('NOT OK', box_height, box_width, box_length, row['height'], row['width'], row['length'])

# Printar matriserna
print(allowedPackaging)
print(utilization)

articles = np.array(article_df['Articles'])
box_types = np.array(boxes_df['Loctype'])
#partDemand = np.array(article_df['orders'])

col = []
row = []
col_index = 0
row_index = 0

for a in articles:
    col.append(f'{col_index}-Part {str(articles[col_index])}')
    col_index += 1

for p in box_types:
    row.append(f'{str(box_types[row_index])}')
    row_index += 1

checkBox = pd.DataFrame(allowedPackaging, columns=col)
checkBox.index = row
utilizationTable = pd.DataFrame(utilization, columns=col)
utilizationTable.index = row

#print(checkBox)
#print(utilizationTable)

suggested_boxtype = pd.DataFrame(columns=["Articles","Boxtypes"])

part = []
box_type = []
for part in col:
    suggested_boxtype = suggested_boxtype.append({'Articles': part, 'Boxtypes': utilizationTable[part].idxmax()}, ignore_index=True)

print(suggested_boxtype)

def create_woorkbook():

    workbook = pd.ExcelWriter('Part_and_BoxType.xlsx', engine='xlsxwriter')

    suggested_boxtype.to_excel(workbook, sheet_name='BoxType Selection')

    workbook.close()

    box_selected = pd.read_excel('/Users/alexjette/Documents/GitHub/Exjobb/Part_and_BoxType.xlsx')
    print(box_selected)

create_woorkbook()
