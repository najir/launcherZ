
from ctypes import alignment
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout, QListWidget, QListWidgetItem, QLineEdit, QCheckBox, QStackedLayout, QHBoxLayout, QLineEdit, QGridLayout, QSpacerItem, QSizePolicy
from .launcherdb import *
from .launcherui import *

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
    def __init__(self, parent):
        super(widgetAddServer, self).__init__(parent)

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
        layoutMain.addLayout(layoutEdit1)
        layoutMain.addLayout(layoutEdit2)
        layoutMain.addLayout(layoutEdit3)
        layoutMain.addWidget(buttonSaveServer)
        layoutMain.addWidget(buttonCancel)
        layoutMain.addWidget(buttonSettings)

        self.setLayout(layoutMain)

class widgetPageServer(QWidget):
    def __init__(self, parent):
        super(widgetPageServer, self).__init__(parent)

        labelMainText = QLabel("Server List")
        listWidgetServer = QListWidget()
        buttonSettings = QPushButton("Settings")
        buttonAddServer = QPushButton("AddServer")
        buttonJoinServer = QPushButton("Join")

        buttonSettings.clicked.connect(self.parent().on_buttonSettings_clicked)
        buttonAddServer.clicked.connect(self.parent().on_buttonAddServer_clicked)
        buttonJoinServer.clicked.connect(self.parent().on_buttonJoinServer_clicked)

        verticalSpacer = QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        layoutServer = QGridLayout()
        layoutServer.addWidget(labelMainText, 0, 0, 1, 1, Qt.AlignBottom)
        layoutServer.addWidget(listWidgetServer, 1, 0, 1, 4)
        layoutServer.addWidget(buttonJoinServer, 3, 1, 1, 2)
        layoutServer.addWidget(buttonSettings, 0, 3, 1, 1)
        layoutServer.addWidget(buttonAddServer, 0, 2, 1, 1)
        layoutServer.addItem(verticalSpacer, 2, 0)

        self.setLayout(layoutServer)


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
    layoutWindow = None
    mainMenu = None
    serverMenu = None
    addServerMenu = None

    def __init__(self):
        super(mainWindow, self).__init__()

        self.setWindowTitle("LauncherZ")
        self.setFixedSize(QSize(1100, 600))

        self.mainMenu = widgetPageMain()
        self.serverMenu = widgetPageServer(self)
        self.addServerMenu = widgetAddServer(self)

        self.layoutWindow = QStackedLayout()
        self.layoutWindow.addWidget(self.mainMenu)
        self.layoutWindow.addWidget(self.addServerMenu)
        self.layoutWindow.addWidget(self.serverMenu)
        self.layoutWindow.setCurrentWidget(self.serverMenu)
        self.serverMenu.show()

        baseWidget = QWidget()
        baseWidget.setLayout(self.layoutWindow)

        self.setCentralWidget(baseWidget)

    def on_buttonSettings_clicked(self):
        return

    def on_buttonAddServer_clicked(self):
        self.layoutWindow.setCurrentWidget(self.addServerMenu)

    def on_buttonJoinServer_clicked(self):
        return
