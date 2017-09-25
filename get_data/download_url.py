import pandas as pd
from urllib import request
import os

file_dict = pd.read_csv('bittiger_data.csv')

directory = '../data'

try:
    os.stat(directory)
except:
    os.mkdir(directory) 

success = 0
failed = 0

for link in file_dict['link-href']:
#    if not link.endswith('.gz'):
#        continue
    try:
        file_name = 'data/'+ link.split('/')[-1]
        request.urlretrieve(link, filename = file_name)
        success += 1
    except:
        print ('Error in downloading: ',link)
        failed += 1

print ('Success: ', success, 'Failed: ', failed)
	     
    
