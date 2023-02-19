######################################
# Database module for all SQL get/insert/updates/deletes
######################################
import sqlite3

class sqlServer():
    sqlTable = """CREATE TABLE IF NOT EXISTS SERVERS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    TITLE            TEXT NOT NULL,
    DESCRIPTION      TEXT,
    IP               TEXT NOT NULL,
    PORT             TEXT NOT NULL,
    INSTALL          TEXT NOT NULL,
    LOGO             TEXT
    BANNER           TEXT
    RSS              TEXT);
    """

    def __init__(self):
        try:
            sqliteConnection = sqlite3.connect('server.db')
            sqlCursor = sqliteConnection.cursor()
            sqlCursor.execute(self.sqlTable)

        except sqlite3.Error as error:
            print('Error occurred - ', error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print('SQLite connection closed')

######################################
# Insert into Database
######################################
    def sqlInsert(self, serverDict):
        sqlInsert = "INSERT OR IGNORE INTO SERVERS("
        sqlInsert += "NAME, DESCRIPTION, IP, PORT, INSTALL, LOGO, BANNER, RSS) VALUES("
        sqlInsert += "'" + serverDict["serverTitle"] + "', "
        sqlInsert += "'" + serverDict["serverDescription"] + "', "
        sqlInsert += "'" + serverDict["serverIP"] + "', "
        sqlInsert += "'" + serverDict["serverPort"] + "', "
        sqlInsert += "'" + serverDict["serverInstall"] + "');"
        sqlInsert += "'" + serverDict["serverLogo"] + "', "
        sqlInsert += "'" + serverDict["serverBanner"] + "', "
        sqlInsert += "'" + serverDict["serverRss"] + "', "

        try:
            sqliteConnection = sqlite3.connect('server.db')
            sqlCursor = sqliteConnection.cursor()
            sqlCursor.execute(sqlInsert)

        except sqlite3.Error as error:
            print('Error occurred - ', error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print('SQLite connection closed')

######################################
# Delete server entry
######################################
    def sqlDelete(self, serverID):
        sqlDelete = "DELETE FROM SERVERS * WHERE ID = " + str(serverID)
        try:
            sqliteConnection = sqlite3.connect('server.db')
            sqlCursor = sqliteConnection.cursor()
            sqlCursor.execute(sqlDelete)

        except sqlite3.Error as error:
            print('Error occurred - ', error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print('SQLite connection closed')

######################################
# Update existing database entry
######################################
    def sqlUpdate(self, serverDict, serverID):
        queryUpdate = "UPDATE SERVERS SET ("
        queryUpdate += "TITLE = '"         +serverDict['serverTitle'] + "', "
        queryUpdate += "DESCRIPTION = '"   +serverDict['serverDescription'] + "', "
        queryUpdate += "IP = '"            +serverDict['serverIP'] + "', "
        queryUpdate += "INSTALL = '"       +serverDict['serverInstall'] + "');"
        queryUpdate += "WHERE ID = "       +serverID
        try:
            sqliteConnection = sqlite3.connect('server.db')
            sqlCursor = sqliteConnection.cursor()
            sqlCursor.execute(queryUpdate)

        except sqlite3.Error as error:
            print('Error occurred - ', error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print('SQLite connection closed')

######################################
# Return Database entry at serverID
######################################
    def sqlGetOne(self, serverID):
        returnData = None
        queryGetOne = "SELECT * FROM SERVERS WHERE ID = " + str(serverID)
        try:
            sqliteConnection = sqlite3.connect('server.db')
            sqlCursor = sqliteConnection.cursor()
            sqlCursor.execute(queryGetOne)
            returnData = sqlCursor.fetchall()

        except sqlite3.Error as error:
            print('Error occurred - ', error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print('SQLite connection closed')

        return returnData

######################################
# Return all databse entries
######################################
    def sqlGetAll(self):
        returnData = None
        queryGetOne = "SELECT * FROM SERVERS"
        try:
            sqliteConnection = sqlite3.connect('server.db')
            sqlCursor = sqliteConnection.cursor()
            sqlCursor.execute(queryGetOne)
            returnData = sqlCursor.fetchall()

        except sqlite3.Error as error:
            print('Error occurred - ', error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print('SQLite connection closed')

        return returnData