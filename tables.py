import numpy as np
import pandas as pd
from pandas_datareader import data as wb

# Hämtar excelfilerna
article_data = pd.read_excel('/Users/alexjette/Documents/Exjobb/Articles.xlsx')
boxes_data = pd.read_excel('/Users/alexjette/Documents/Exjobb/Boxes.xlsx')

# Gör excelfilerna till pandas.DataFrame
article_df = pd.DataFrame(article_data)
boxes_df = pd.DataFrame(boxes_data)

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
            utilization[box_index, article_index] = (row['height'] * row['width'] * row['length']) / (box_height * box_width * box_length)
            #print('OK', box_height, box_width, box_length, row['height'], row['width'], row['length'])
            #print(box_height * box_width * box_length, row['height'] * row['width'] * row['length'])
        elif box_height > row['length'] and box_width > row['width'] and box_length > row['height']:
            allowedPackaging[box_index, article_index] = 1
            utilization[box_index, article_index] = (row['height'] * row['width'] * row['length']) / (box_height * box_width * box_length)
            #print('OK', box_height, box_width, box_length, row['height'], row['width'], row['length'])
            #print(box_height * box_width * box_length, row['height'] * row['width'] * row['length'])
        elif box_height > row['width'] and box_width > row['height'] and box_length > row['length']:
            allowedPackaging[box_index, article_index] = 1
            utilization[box_index, article_index] = (row['height'] * row['width'] * row['length']) / (box_height * box_width * box_length)
            #print('OK', box_height, box_width, box_length, row['height'], row['width'], row['length'])
            #print(box_height * box_width * box_length, row['height'] * row['width'] * row['length'])
        elif box_height > row['length'] and box_width > row['height'] and box_length > row['width']:
            allowedPackaging[box_index, article_index] = 1
            utilization[box_index, article_index] = (row['height'] * row['width'] * row['length']) / (box_height * box_width * box_length)
            #print('OK', box_height, box_width, box_length, row['height'], row['width'], row['length'])
            #print(box_height * box_width * box_length, row['height'] * row['width'] * row['length'])
        elif box_height > row['width'] and box_width > row['length'] and box_length > row['height']:
            allowedPackaging[box_index, article_index] = 1
            utilization[box_index, article_index] = (row['height'] * row['width'] * row['length']) / (box_height * box_width * box_length)
            #print('OK', box_height, box_width, box_length, row['height'], row['width'], row['length'])
            #print(box_height * box_width * box_length, row['height'] * row['width'] * row['length'])
        elif box_height > row['height'] and box_width > row['length'] and box_length > row['width']:
            allowedPackaging[box_index, article_index] = 1
            utilization[box_index, article_index] = (row['height'] * row['width'] * row['length']) / (box_height * box_width * box_length)
            #print('OK', box_height, box_width, box_length, row['height'], row['width'], row['length'])
            #print(box_height * box_width * box_length, row['height'] * row['width'] * row['length'])
        #else:
            #print('NOT OK', box_height, box_width, box_length, row['height'], row['width'], row['length'])

# Printar matriserna
#print(allowedPackaging)
#print(utilization)

#Skapar random partDemand och packaging tills vi fått datan
import random

partDemand = []
packaging = []

package = 0

for a in range(0, len(article_df)):
    rand_demand = random.randint(10,25)
    package += 1
    packaging.append(package)
    partDemand.append(rand_demand)

#print(f'Packaging: {packaging}')
#print(f'PartDemand: {partDemand}')