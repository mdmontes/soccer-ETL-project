import mysql.connector
import pandas as pd

def create_table(headers,database_list,title):
    # from active_scripts.C_parsedata import player_info_cleanlist

    #0. Read documentation on Inserting columns:
    # https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html

    # 1. Connect to Database
    db = mysql.connector.connect(
        host = database_list[0],
        user = database_list[1],
        passwd = database_list[2],
        database = database_list[3],
    )

    mycursor = db.cursor()

    # 2. Create Pandas data frame 'player_columns' and SQL query string SQL_CREATE_TBL
    player_columns = pd.Series(headers, name='Columns')

    
    # SQL_CREATE_TBL = 'CREATE TABLE player_data_raw('
    
    SQL_CREATE_TBL= 'CREATE TABLE '
    SQL_DELETE_TBL = 'DROP TABLE IF EXISTS '
    
    SQL_CREATE_TBL += '{}('.format(title)
    SQL_DELETE_TBL += '{}'.format(title)
    
    for column in range(0, len(player_columns)-1):
        SQL_CREATE_TBL += '{} VARCHAR(50), '.format(player_columns[column])
    SQL_CREATE_TBL += '{} VARCHAR(50))'.format(player_columns[len(player_columns)-1])

    # 3. Drop table if it exits and recreate. Then commit to database
    # mycursor.execute( "DROP TABLE IF EXISTS player_data_raw") 
    mycursor.execute(SQL_DELETE_TBL) 
    mycursor.execute(SQL_CREATE_TBL)

    db.commit()
