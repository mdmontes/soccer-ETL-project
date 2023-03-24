from active_scripts.C_get_request_playerdata import get_request
from active_scripts.G_populate_table import populate_table
from active_scripts.D_parse_player_data import parse_data
import time

def complete_table(table_names,response_current_page, response_page_max, results_per_page,url, headers, query_list, database_list):
    player_data_index = 0
    
    response_data = get_request(url, headers, query_list)
    results_per_page = response_data["results"]
    print(f'the results per page is {results_per_page}')
    response_current_page = response_data["paging"]["current"]
    response_page_max = response_data["paging"]["total"]
    
    while player_data_index < results_per_page:
      new_player_data_parsed = parse_data(response_data, player_data_index)
      
      player_dimdata_columns = new_player_data_parsed[0] 
      player_stat_columns = new_player_data_parsed[1]
      player_dimdata_data = new_player_data_parsed[2]
      player_stat_data = new_player_data_parsed[3]
      
      populate_table(table_names[0], player_dimdata_columns, player_dimdata_data, database_list)

      populate_table(table_names[1], player_stat_columns, player_stat_data, database_list)
      
      player_data_index+=1
      print(f'player data index for parsing process is now {player_data_index}')
    
    if response_current_page < response_page_max:
       response_current_page+=1
       query_list[2] = response_current_page
       time.sleep(1)
       print(f'pagination is now {response_current_page}')
       complete_table(table_names, response_current_page, response_page_max, results_per_page,url, headers, query_list, database_list)
    else:
       print(f'All data has been exported!')
