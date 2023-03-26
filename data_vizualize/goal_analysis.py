import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

from dotenv import load_dotenv
import os

load_dotenv()

db = mysql.connector.connect(
    host = os.getenv('host'),
    user = os.getenv('user'),
    passwd = os.getenv('passwd'),
    database = os.getenv('database'))

mycursor = db.cursor()


mycursor.execute("select player_data_dims.player_key,id as player_id, name, team_name, league_season, games_position, games_appearences, goals_total, shots_total, shots_on, goals_assists from player_data_dims inner join player_data_stats on player_data_dims.player_key = player_data_stats.player_key where league_season between '2000' and '2022' order by league_season")

soccer_sql_query = mycursor.fetchall()

soccer_dataframe = pd.DataFrame(soccer_sql_query, columns=['player_key', 'player_id' ,'name','team_name','league_season', 'game_position','game_appearences','goals_total','shots_total', 'shots_on', 'goals_assists'])

soccer_dataframe[['game_appearences','goals_total','shots_total', 'shots_on', 'goals_assists']] = soccer_dataframe[['game_appearences','goals_total','shots_total', 'shots_on', 'goals_assists']].apply(pd.to_numeric)

positions_df = soccer_dataframe[soccer_dataframe['game_position'] == 'Attacker']

print(positions_df)