import requests
import time

from active_scripts.A_initial_table import initial_table
from active_scripts.A_obtain_season_data import get_season_data

from dotenv import load_dotenv
import os

load_dotenv()

url = "https://api-football-v1.p.rapidapi.com/v3/players/seasons"

headers = {
	"X-RapidAPI-Key": os.getenv('X-RapidAPI-Key'),
	"X-RapidAPI-Host": os.getenv('X-RapidAPI-Host')
}

response = requests.request("GET", url, headers=headers)

seasons = response.json()

season_years = []

for years in seasons['response']:
    season_years.append(int(years))

# print(len(season_years))

initial_table(season_years[37])

for year in range(0,38):
    print(f'Starting next call. Requesting season year {season_years[year]}')
    get_season_data(season_years[year])
    time.sleep(1)
    print(f'completed year {season_years[year]}')




