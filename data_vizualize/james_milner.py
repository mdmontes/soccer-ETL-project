# https://www.geeksforgeeks.org/how-to-plot-a-pandas-dataframe-with-matplotlib/
# https://www.geeksforgeeks.org/how-to-select-rows-from-a-dataframe-based-on-column-values/

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


mycursor.execute("select player_data_dims.player_key,id as player_id, name, firstname, lastname, birthdate, team_name, league_season, games_position, games_appearences, goals_total,goals_assists from player_data_dims inner join player_data_stats on player_data_dims.player_key = player_data_stats.player_key where league_season between '2005' and '2022' order by league_season")

soccer_sql_query = mycursor.fetchall()

soccer_dataframe = pd.DataFrame(soccer_sql_query, columns=['player_key', 'player_id' ,'name', 'firstname','lastname', 'birthdate', 'team_name', 'league_season', 'game_position','game_appearences','goals_total','goals_assists'])

# print(soccer_dataframe)

soccer_dataframe[['game_appearences', 'goals_total', 'goals_assists']] = soccer_dataframe[['game_appearences', 'goals_total', 'goals_assists']].apply(pd.to_numeric)

rows, columns = soccer_dataframe.shape
# print(rows)
# print(soccer_dataframe[2:5])

james_df = soccer_dataframe[soccer_dataframe['player_id'] == '296']

print(james_df)

james_df.plot(x='league_season', y='game_appearences')
plt.scatter(x = james_df['league_season'], y = james_df['game_appearences'])

xs = james_df['league_season']
ys = james_df['game_appearences']
label =''

for x, y in zip(xs, ys):
    temporary_df = james_df[james_df['league_season'] == x]
    team_df = temporary_df['team_name']
    label = '{}, '.format(team_df.iloc[0])
    # label += '({}, '.format(x)
    # label += '{})'.format(y)
    plt.annotate(label, (x,y), textcoords="offset points", xytext=(0,10),ha='center')


# plt.text(x=james_df['league_season'], y = james_df['game_appearences'], james_df['team_name'])
plt.show()



# How can I return a list of playernames based on most frequent to lease frequent within data?


