'''
Database module for launcher. SQLite calls for any neccessary information needed by either
web or ui modules.
'''
import sqlite3

class sqlServer():
    sqlTable = """CREATE TABLE IF NOT EXISTS SERVERS(
    NAME            = TEXT,
    DESCRIPTION     = TEXT,
    IP              = TEXT,
    INSTALL         = TEXT);
    """

    def __init__():
        try:
            sqliteConnection = sqlite3.connect('server.db')
            sqlCursor = sqliteConnection.cursor
            sqlCursor.execute(sqlTable)

        except sqlite3.Error as error:
            print('Error occurred - ', error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print('SQLite connection closed')

    def sqlInsert(serverDict):
        try:
            sqliteConnection = sqlite3.connect('server.db')


        except sqlite3.Error as error:
            print('Error occurred - ', error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print('SQLite connection closed')

    def sqlDelete(serverDict):
        try:
            sqliteConnection = sqlite3.connect('server.db')


        except sqlite3.Error as error:
            print('Error occurred - ', error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print('SQLite connection closed')

    def sqlUpdate(serverDict):
        try:
            sqliteConnection = sqlite3.connect('server.db')


        except sqlite3.Error as error:
            print('Error occurred - ', error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print('SQLite connection closed')