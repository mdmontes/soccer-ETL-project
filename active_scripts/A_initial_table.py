import pprint
from active_scripts.C_get_request_playerdata import get_request
from active_scripts.D_parse_player_data import parse_data
from active_scripts.E_create_table import create_table

from dotenv import load_dotenv
import os

load_dotenv()

def initial_table(season):
  p_print = pprint.pprint
  # 1. Review documentation
  # https://www.api-football.com/documentation-v3#tag/Players/operation/get-players


  # Set API Paremeters to call API and Database Paramenters to access database(query_list, database_list)
  url = "https://api-football-v1.p.rapidapi.com/v3/players"
  headers = {
  "X-RapidAPI-Key": os.getenv('X-RapidAPI-Key'),
	"X-RapidAPI-Host": os.getenv('X-RapidAPI-Host')
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
  # # 0. createdatabase. EXECUTE ONLY ONCE
  # # create_database(database_list)

  # # 1. call get_request to obtain player data from API and pass to variable response_data

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
  initial_data = parse_data(response_data, 0)
  diminfo_column_headers = initial_data[0]
  stat_column_headers = initial_data[1]

  # p_print(diminfo_column_headers)
  # p_print(stat_column_headers)

  # 3. create initial table 'raw_player_data'
  create_table(diminfo_column_headers, database_list,'player_data_dims')
  create_table(stat_column_headers, database_list,'player_data_stats')