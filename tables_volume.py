
# I kommentarerna nedan och genom koden finns beskrivningar av vad koden är ämnad för och vad som sker i olika steg av koden.
# Den här koden utför den "pre-processing" av datan som behövs för att sedan utföra optimeringen i "facility_volume.py".

# Importerar de paket som är nödvända för att utföra bearbetningen av data
import numpy as np
import pandas as pd
from pandas_datareader import data as wb

# Hämtar excelfilerna där datan för artiklarna och lådorna finns
article_data = pd.read_excel('Articles_ny.xlsx', 'Big+XTR')
boxes_data = pd.read_excel('Boxes.xlsx', 'All packaging') # Standard packaging All packaging QPallet

# Gör excelfilerna till pandas.DataFrame för att lättare kunna bearbeta dom
article_df = pd.DataFrame(article_data)
boxes_df = pd.DataFrame(boxes_data)

# Skapar två nollmatriser med antal rader = antar lådor och kolumner = antal artiklar (rader, kolumner)
# I matrisen "allowed_packaging" kommer 1:or sättas in på de index där en artikel får plats i en låda och 0:or kommer stå kvar för de lådor där inte en artikel får plats
allowedPackaging = np.zeros((len(boxes_df),len(article_df)))
# I matrisen "volume" kommer volymutnyttjandet att fyllas i för tillåtna lådor för respektive artikel, alltså ersätta alla 1:or i förra matrisen
volume = np.zeros((len(boxes_df),len(article_df)))

# Skapar indexvariabler
box_index = -1
article_index = -1

# Den kommande loopen kommer att kolla om respektive artikel får plats i respektive låda

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
        # För given låda och artikel testas 6st 90-graders rotationer för att avgöra om artiklen får plats i lådan
        if box_height > row['height'] and box_width > row['width'] and box_length > row['length']:
            allowedPackaging[box_index, article_index] = 1
            volume[box_index, article_index] = (box_height * box_width * box_length) - (row['height'] * row['width'] * row['length'])

        elif box_height > row['length'] and box_width > row['width'] and box_length > row['height']:
            allowedPackaging[box_index, article_index] = 1
            volume[box_index, article_index] = (box_height * box_width * box_length) - (row['height'] * row['width'] * row['length'])

        elif box_height > row['width'] and box_width > row['height'] and box_length > row['length']:
            allowedPackaging[box_index, article_index] = 1
            volume[box_index, article_index] = (box_height * box_width * box_length) - (row['height'] * row['width'] * row['length'])

        elif box_height > row['length'] and box_width > row['height'] and box_length > row['width']:
            allowedPackaging[box_index, article_index] = 1
            volume[box_index, article_index] = (box_height * box_width * box_length) - (row['height'] * row['width'] * row['length'])

        elif box_height > row['width'] and box_width > row['length'] and box_length > row['height']:
            allowedPackaging[box_index, article_index] = 1
            volume[box_index, article_index] = (box_height * box_width * box_length) - (row['height'] * row['width'] * row['length'])

        elif box_height > row['height'] and box_width > row['length'] and box_length > row['width']:
            allowedPackaging[box_index, article_index] = 1
            volume[box_index, article_index] = (box_height * box_width * box_length) - (row['height'] * row['width'] * row['length'])

# Skapar variabler som sedan importeras i "facility_volume.py" vid optimeringen
# "articles" är en "dataframe" av artiklarna
articles = np.array(article_df['Articles'])
# "packaging" är en "dataframe" av lådorna
packaging = np.array(boxes_df['Boxes'])
# "partDemand" är en "dataframe" av efterfrågan för respektive artikel
partDemand = np.array(article_df['orders'])
