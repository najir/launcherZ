'''
Database module for launcher. SQLite calls for any neccessary information needed by either
web or ui modules.
'''
import sqlite3

class sqlServer():
    sqlTable = """CREATE TABLE IF NOT EXISTS SERVERS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME            = TEXT,
    DESCRIPTION     = TEXT,
    IP              = TEXT,
    INSTALL         = TEXT);
    """

    def __init__(self):
        try:
            sqliteConnection = sqlite3.connect('server.db')
            sqlCursor = sqliteConnection.cursor
            sqlCursor.execute(self.sqlTable)

        except sqlite3.Error as error:
            print('Error occurred - ', error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print('SQLite connection closed')

    def sqlInsert(serverDict):
        sqlInsert = "INSERT OR IGNORE INTO SERVERS("
        sqlInsert += "NAME, DESCRIPTION, IP, INSTALL) VALUES("
        sqlInsert += "'" + serverDict["nameText"] + "', "
        sqlInsert += "'" + serverDict["descriptionText"] + "', "
        sqlInsert += "'" + serverDict["serverIP"] + "', "
        sqlInsert += "'" + serverDict["serverInstall"] + "');"

        try:
            sqliteConnection = sqlite3.connect('server.db')
            sqlCursor = sqliteConnection.cursor
            sqlCursor.execute(sqlInsert)

        except sqlite3.Error as error:
            print('Error occurred - ', error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print('SQLite connection closed')

    def sqlDelete(serverID):
        sqlDelete = "DELETE FROM SERVERS * WHERE ID = " + serverID
        try:
            sqliteConnection = sqlite3.connect('server.db')
            sqlCursor = sqliteConnection.cursor
            sqlCursor.execute(sqlDelete)

        except sqlite3.Error as error:
            print('Error occurred - ', error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print('SQLite connection closed')

    def sqlUpdate(serverDict, serverID):
        sqlUpdate = "UPDATE SERVERS SET ("
        sqlUpdate += "NAME = '"         +serverDict['serverName'] + "', "
        sqlUpdate += "DESCRIPTION = '"  +serverDict['serverName'] + "', "
        sqlUpdate += "IP = '"           +serverDict['serverName'] + "', "
        sqlUpdate += "INSTALL = '"      +serverDict['serverName'] + "');"
        sqlUpdate += "WHERE ID = "      +serverID
        try:
            sqliteConnection = sqlite3.connect('server.db')
            sqlCursor = sqliteConnection.cursor
            sqlCursor.execute(sqlUpdate)

        except sqlite3.Error as error:
            print('Error occurred - ', error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print('SQLite connection closed')