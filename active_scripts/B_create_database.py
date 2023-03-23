# https://www.youtube.com/watch?v=3vsC05rxZ8c
# https://www.youtube.com/watch?v=91iNR0eG8kE

def create_database(database_list):
    # 1. Query should only be run ONCE. After Database created, no need to re-run
    import mysql.connector

    db = mysql.connector.connect(
        host= database_list[0],
        user= database_list[1],
        passwd=database_list[2]
    )

    mycursor = db.cursor()

    # mycursor.execute("DROP DATABASE soccer_data")
    mycursor.execute("CREATE DATABASE soccer_data")
