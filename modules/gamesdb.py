import sys
import sqlite3 as sqlite

class GamesDB:

    def __init__(self, config_path):

        self.db_path = config_path + '/games.db'

    def write(self, games_list):

        with sqlite.connect(self.db_path) as sqlite_con:

            sqlite_cursor = sqlite_con.cursor()

            sqlite_cursor.execute('CREATE TABLE IF NOT EXISTS Games(\
                    Name TEXT, Id TEXT, Title TEXT, Banner TEXT, Icon TEXT, \
                    Dlcs TEXT, \
                    UNIQUE(Name, Id, Title, Banner, Icon, Dlcs))')

            for game_data in games_list:
                sqlite_cursor.execute('INSERT OR IGNORE INTO Games VALUES' + str(game_data))

    def get_ids(self):

        ids_list = []

        with sqlite.connect(self.db_path) as sqlite_con:

            sqlite_cursor = sqlite_con.cursor()
            sqlite_cursor.execute('SELECT Id FROM Games')
            rows = sqlite_cursor.fetchall()
            for row in rows:
                ids_list.append(row[0])

        return ids_list

    def get_games_data(self):

        games_data = {}

        with sqlite.connect(self.db_path) as sqlite_con:

            sqlite_cursor = sqlite_con.cursor()
            sqlite_cursor.execute('SELECT * FROM Games')
            rows = sqlite_cursor.fetchall()

            for row in rows:
                games_data[row[0]] = row[1:]

        return games_data
