Soccer API Project Doc
Goals:
•	To learn how to successfully scrape data related to soccer players from through the https://api-football-v1.p.rapidapi.com API.
o	Includes a combination of source data and calculated data needed to identify predictive measures.
o	Create a rating.

Possible Tasks:
- Key Documentation: https://www.api-football.com/documentation-v3#tag/Players/operation/get-players

	
o	Get Json Data into tables that can be managed using SQL
	Look at Python Modules: sqlite3
o	Start visualizing. Create line graphs & bar graphs
	Look at Pandas
	Look at matplotlib

2/12/2022
- Discuss Tabble creation.
    -Should

2/23/2023
- Discuss priorities:
    - Do we need SQlite?
    - Entering data in original format
        - capture data type original format, place in list
    - Consider using dataframes from Pandas instead of dictionaries
- Read link below in order to pull more players:
    - https://www.api-football.com/news/post/how-to-get-all-teams-and-players-from-a-league-id
- Outstanding issues
    - Changing data within raw tables from string to date.
    - Automate the API requests using for loop for a small range of players
        - How many requests can I get?
