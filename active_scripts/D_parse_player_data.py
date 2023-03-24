import pprint
p_print = pprint.pprint

def parse_data(response_data, player_data_index):
    #1. API data in response_data is cleaned to produce player_info_clean 
    get_parameters = response_data['parameters']
    paging_info = response_data['paging']
    player_stats = response_data['response'][player_data_index]['statistics'][0]
    player_info = response_data['response'][player_data_index]['player']

    # 2. create player/season unique key
    player_key = str(player_info['id']) +'_'+str(get_parameters['league'])+'_'+str(get_parameters['season'])+'_'+str(paging_info['current'])+'_'+str(paging_info['total'])

    # 3. Pre birthday data
    birth_holder = player_info['birth']
    birthdate = birth_holder['date']
    birth_holder['birthdate']= birthdate

    #4.  list data attibutes that are not static for player. These change and should be excluded from dims 

    numeric_data_player_info = ['birth', 'height', 'weight', 'injured', 'photo', 'date']

    long_data = ['photo', 'logo', 'flag']

    # 5. Prep data into dictionary and columns into list
    player_diminfo_clean ={}
    player_diminfo_cleanlist = []
    player_stat_clean = {}
    player_stat_cleanlist = []

    player_diminfo_clean['player_key'] = player_key
    player_stat_clean['player_key'] = player_key

    # 6 populate descriptive data
    for data in player_info:
        if (data in numeric_data_player_info or data in long_data):
                # print(f'the data {data} has been excluded, print statement 1')
                continue
        player_diminfo_clean[data] = player_info[data]

    for birthdata in birth_holder:
        player_diminfo_clean[birthdata] = birth_holder[birthdata]

    for data in player_diminfo_clean:
        player_diminfo_cleanlist.append(data)

    # 7 populate statistical data

    for stat in player_stats:
        player_sub_stat = player_stats[stat]
        for sub_stat in player_sub_stat:
            if sub_stat in long_data:
                # print(f'the data {sub_stat} has been excluded print statement 2')
                continue
            if sub_stat == "season":
                stat_clean_header = f'{stat}_{sub_stat}'
                player_stat_clean[stat_clean_header] = get_parameters['season']
                continue
            micro_data = player_sub_stat[sub_stat]
            stat_clean_header = f'{stat}_{sub_stat}'
            player_stat_clean[stat_clean_header] = micro_data

    for data in numeric_data_player_info:
        if (data == 'date' or data == 'birth' or data == 'photo'):
            # print(f'the data {data} has been excluded print statement 3')
            continue
        player_stat_clean[data] = player_info[data]
    
    for data in player_stat_clean:
        player_stat_cleanlist.append(data)
     
    # p_print(player_diminfo_clean)
    # p_print(player_diminfo_cleanlist)
    # p_print(player_stat_clean)
    # p_print(player_stat_cleanlist)

    # 8 consolidate parsed diminfo and stat data 
        
    consolidated_data = [player_diminfo_cleanlist, player_stat_cleanlist, player_diminfo_clean, player_stat_clean]
        
    return consolidated_data

# conn = sqlite3.connect('Player_Data')
# cursor = conn.cursor()

# cursor.executescript('''DROP TABLE IF EXISTS Player_Stats; CREATE TABLE Player_Stats (Header varchar(30), Data varchar(30)) ''')

# for header in player_info_cleanlist:
#     value = player_info_clean[header]
#     cursor.execute("insert into Player_Stats values (?,?)", (header,value))

# fetch_table_sqlite = cursor.execute(''' SELECT * FROM Player_Stats''').fetchall()

# fetch_table_pd = pd.read_sql_query(''' SELECT * FROM Player_Stats''',conn)

# print(fetch_table_pd)

# cursor.close()
# conn.close()
                     


