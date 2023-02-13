
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout, QListWidget, QListWidgetItem, QLineEdit, QCheckBox, QStackedLayout, QHBoxLayout, QLineEdit
from launcherdb import *
from launcherui import *

'''
Class that contains all the data needed for initial default servers
'''
class serverList():
    serverDict = {
        "descriptionText" : "",
        "nameText"        : "",
        "serverLogo"      : "",
        "ServerBanner"    : "",
        "serverIp"        : "",
        "serverInstall"   : "",
        "serverRss"       : "",
    }
    def myServer(self):
        self.serverDict = {
            "descriptionText" : "",
            "nameText"        : "",
            "serverLogo"      : "",
            "ServerBanner"    : "",
            "serverIp"        : "",
            "serverInstall"   : "",
            "serverRss"       : "",
    }
    def xServer(self):
        self.serverDict = {
            "descriptionText" : "",
            "nameText"        : "",
            "serverLogo"      : "",
            "ServerBanner"    : "",
            "serverIp"        : "",
            "serverInstall"   : "",
            "serverRss"       : "",
    }
    def yServer(self):
        self.serverDict = {
            "descriptionText" : "",
            "nameText"        : "",
            "serverLogo"      : "",
            "ServerBanner"    : "",
            "serverIp"        : "",
            "serverInstall"   : "",
            "serverRss"       : "",
    }
    def zServer(self):
        self.serverDict = {
            "descriptionText" : "",
            "nameText"        : "",
            "serverLogo"      : "",
            "ServerBanner"    : "",
            "serverIp"        : "",
            "serverInstall"   : "",
            "serverRss"       : "",
    }
    def serverInit(self):
        # Checks if default server exists in table, creates them if not
        return
"""
Server list initial page. Brings out a list of available servers from text files
List of servers, expected 5-10
Server Widget contains: Uptime-Icon, Server Name, Description, banner image
A button for settings
"""
class widgetAddServer(QWidget):
    def __init__(self):
        super().__init__()

        labelServerName = QLabel("Server Name")
        labelServerDesc = QLabel("Server Description")
        labelServerIP = QLabel("Server IP")
        buttonSettings = QPushButton("Settings")
        buttonSaveServer = QPushButton("Save")
        buttonCancel = QPushButton("Cancel")
        lineServerName = QLineEdit("")
        lineServerDesc = QLineEdit("")
        lineServerIP = QLineEdit("")

        layoutEdit1 = QHBoxLayout()
        layoutEdit1.addWidget(labelServerName)
        layoutEdit1.addWidget(lineServerName)
        
        layoutEdit2 = QHBoxLayout()
        layoutEdit2.addWidget(labelServerDesc)
        layoutEdit2.addWidget(lineServerDesc)

        layoutEdit3 = QHBoxLayout()
        layoutEdit3.addWidget(labelServerIP)
        layoutEdit3.addWidget(lineServerIP)

        layoutMain = QVBoxLayout()
        layoutMain.addWidget(layoutEdit1)
        layoutMain.addWidget(layoutEdit2)
        layoutMain.addWidget(layoutEdit3)
        layoutMain.addWidget(buttonSaveServer)
        layoutMain.addWidget(buttonCancel)
        layoutMain.addWidget(buttonSettings)

        self.setLayout(layout)

class widgetPageServer(QWidget):
    def __init__(self):
        super().__init__()

        labelMainText = QLabel("Server List")
        labelServerText = QLabel("")
        listWidgetServer = QListWidget()
        buttonSettings = QPushButton("Settings")
        buttonAddServer = QPushButton("AddServer")

        layout = QVBoxLayout()
        layout.addWidget(labelMainText)
        layout.addWidget(listWidgetServer)
        layout.addWidget(buttonAddServer)
        layout.addWidget(buttonSettings)

        self.setLayout(layout)

"""
Contains all of the details to a server
Name, Descriptions, Smaller details or info, Logo image, banner/ad image
Login information, Save username checkbox, News feeds, potential server calls
"""
class widgetPageMain(QWidget):
    def __init__(self):
        super().__init__()
        labelDesc = QLabel("")
        labelTitle = QLabel("")
        labelRss = QLabel("")
        labelInstall = QLabel("")
        editUser = QLineEdit("")
        #This needs to be hidden
        editPass = QLineEdit("")
        checkboxUser = QCheckBox("")
        buttonLog = QPushButton("")
        buttonSettings = QPushButton("")
        buttonPlay = QPushButton("")
        buttonBack = QPushButton("")


"""
Main Server Window, called and actiavted on launcherZ
"""
class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("LauncherZ")
        self.setFixedSize(QSize(1100, 600))

        mainMenu = widgetPageMain()
        serverMenu = widgetPageServer()

        layout = QStackedLayout()
        layout.addWidget(mainMenu)
        layout.addWidget(serverMenu)
        layout.setCurrentWidget(serverMenu)
        serverMenu.show()

        baseWidget = QWidget()
        baseWidget.setLayout(layout)

        self.setCentralWidget(baseWidget)
