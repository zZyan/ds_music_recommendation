import pandas as pd
import re
import gzip

'''
get set for user id
'''
user_id = []
with open("../data/3_1.uids", "rb") as f:
    for line in f:
        user = line.decode('utf-8')
        user_id.append(user.split(' ')[0])

user_set = set(user_id)
df_user = pd.DataFrame()
df_user['uid']=list(user_set)
df_user.to_csv('../data/parsed_data/3_1uid.csv')
# 265563
del df_user

'''
clean download log
'''
df_download = pd.read_csv('../data/parsed_data/log_download.csv')
# fix device column
df_download.loc[df_download.device.str.contains('ar', na = False), 'device'] = 'ar'
df_download.loc[df_download.device.str.contains('ip', na = False), 'device'] = 'ip'
# check completeness:
# ar:ip = 6604959:1132541
# 132/7746762 -> might use some smart way to fillna, or drop


df_download.loc[df_download['song_name'].isnull() & df_download['song_id'].isnull()]
# 487/7746762 -> use play to fill in the name and id
df_download['song_name'] = df_download['song_name'].str.strip()
df_download.to_csv('../data/parsed_data/clean_download.csv', encoding='utf-8')

del df_download


'''
clean search log
'''
df_search = pd.read_csv('../data/parsed_data/log_search.csv')
df_search.loc[df_search.device.str.contains('ar', na = False), 'device'] = 'ar'
df_search.loc[df_search.device.str.contains('ip', na = False), 'device'] = 'ip'
# ar:ip 8211985:1563802
# missing 19325/9795112 < 0.1%
# user id, drop those without uid - useless - 16% dropped
df_search = df_search.loc[~df_search['uid'].isnull()]


# construct a song dictionary from play
df_search.query = df_search.time
# date column is complete

df_search['date'], df_search['time'] = df_search['date'].str.split(' ').str
df_search.drop('query', axis=1, inplace = True)

df_search.to_csv('../data/parsed_data/clean_search.csv')

del df_search

'''
clean play log
'''
df_play = pd.read_csv('../data/parsed_data/log_play.csv')
df_play.loc[df_search.device.str.contains('ar', na = False), 'device'] = 'ar'
df_play.loc[df_search.device.str.contains('ip', na = False), 'device'] = 'ip'

import pyodbc
server = 'tcp:DESKTOP-VTML08.database.windows.net'
database = 'db_music_box'
username = 'myusername'
password = 'mypassword'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

connection_str =  """
Driver={SQL Server Native Client 11.0};
Server=DESKTOP-VTML08;
Database=master;
Trusted_Connection=yes;
"""
db_connection = pyodbc.connect(connection_str)
db_connection.autocommit = True
db_cursor = db_connection.cursor()
sql_command = """
CREATE DATABASE PythonExperimentsDb
"""

cnxn = pyodbc.connect(r'Driver={SQL Server};Server=DESKTOP-VTML08;Database=db_music_box;Trusted_Connection=yes;')
cursor = cnxn.cursor()