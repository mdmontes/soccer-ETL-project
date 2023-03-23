import mysql.connector
import pandas as pd
from active_scripts.A1_get_request_playerdata import get_request
from active_scripts.C_parse_player_data import parse_data
from active_scripts.main import url, headers, query_list, database_list

# def populate_table(table_names,headers,player_data,database):

table_names = ['player_data_dims', 'player_data_stats']
response_data = get_request(url, headers, query_list)
initial_data = parse_data(response_data, 0)

table_name = table_names[1]
headers = initial_data[1]
player_data = initial_data[3]
database = database_list

print(player_data)

#0. Read documentation on Inserting columns:
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html

#1. Connect to DB and parse response data
db = mysql.connector.connect(
    host = database[0],
    user = database[1],
    passwd = database[2],
    database = database[3]
)
mycursor = db.cursor()

#2. Create Pandas data frame player_columns and SQL query string SQL_CREATE_TBL
player_columns = pd.Series(headers, name='Columns')

#3 Populate SQL Insert Query with COLUMNS
# SQL_INSERT_COLUMN = 'INSERT INTO player_data_raw('
SQL_INSERT_COLUMN = 'INSERT INTO '
SQL_INSERT_COLUMN += f'{table_name} ('

for column in range(0, len(player_columns)-1):
    SQL_INSERT_COLUMN += '{}, '.format(player_columns[column])

SQL_INSERT_COLUMN += '{}) VALUES('.format(player_columns[len(player_columns)-1])

for column in range(0, len(player_columns)-1):
    SQL_INSERT_COLUMN += '%s, '

SQL_INSERT_COLUMN+= '%s)'

# print(type(player_info_clean))

# 4 Prepare data from response object into tuples,
SQL_INSERT_DICT = []

for data in player_data:
    SQL_INSERT_DICT.append(player_data[data])

SQL_INSERT_VALUE = tuple(SQL_INSERT_DICT)
SQL_INSERT_VALUE

# 5 execute query.
mycursor.execute(SQL_INSERT_COLUMN,SQL_INSERT_VALUE)
            
db.commit()
