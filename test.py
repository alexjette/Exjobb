import numpy as np
import pandas as pd
from pandas_datareader import data as wb

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
#print(list2[0])

new_list = pd.DataFrame(columns=["Articles","Boxtypes"])
for l in list1:
    #test_list = pd.DataFrame([l, list2[l]], columns=["Articles","Boxtypes"])
    #new_list.append(test_list)
    new_list = new_list.append({'Articles': l, 'Boxtypes': list2[l]}, ignore_index=True)
    #new_list = new_list.append({'Boxtypes': list2[l]}, ignore_index=True)

print(new_list)
