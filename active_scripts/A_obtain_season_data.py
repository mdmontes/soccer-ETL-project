import time
import pprint
from active_scripts.C_get_request_playerdata import get_request
from active_scripts.F_complete_table import complete_table

from dotenv import load_dotenv
import os

load_dotenv()

def get_season_data(season):
  p_print = pprint.pprint
  # 1. Review documentation
  # https://www.api-football.com/documentation-v3#tag/Players/operation/get-players


  # Set API Paremeters to call API and Database Paramenters to access database(query_list, database_list)
  url = "https://api-football-v1.p.rapidapi.com/v3/players"
  querystring = {"league":"39","season":"2020", "page":"1"}
  headers = {
    "X-RapidAPI-Key": os.getenv('X-RapidAPI-Key'), 
    "X-RapidAPI-Host":os.getenv('X-RapidAPI-Host')
    }

  league_query = 39
  season_query = season
  page_query = 1

  query_list = [league_query, season_query, page_query]

  host = os.getenv('host')
  user = os.getenv('user')
  passwd = os.getenv('passwd')
  database = os.getenv('database')

  database_list = [host, user, passwd, database]

  # if __name__=="__main__":
  # 0. createdatabase. EXECUTE ONLY ONCE
  # create_database(database_list)

  # 1. call get_request to obtain player data from API and pass to variable response_data
  response_data = get_request(url, headers,query_list)
  results_per_page = response_data["results"]
  response_current_page = response_data["paging"]["current"]
  response_page_max = response_data["paging"]["total"]

  print(f'the current page is {response_current_page}')
  print(f'the last page is {response_page_max}')
  print(f'the current results per page is {results_per_page}')

  if results_per_page == 0:
    print(f'Exiting, since the results per page for this season is {results_per_page}')
    return None

  # 2. call 'parse_data' to obtain column headers and initial player data
  # data = parse_data(response_data, 0)
  # diminfo_column_headers = data[0]
  # stat_column_headers = data[1]

  # p_print(diminfo_column_headers)
  # p_print(stat_column_headers)

  # 3. recursively populate entire table 
  time.sleep(1)
  table_names = ['player_data_dims', 'player_data_stats']
  complete_table(table_names, response_current_page, response_page_max, results_per_page, url, headers, query_list, database_list)