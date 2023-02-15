from ctypes import alignment
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout, QListWidget, QListWidgetItem, QLineEdit, QCheckBox, QStackedLayout, QHBoxLayout, QLineEdit, QGridLayout, QSpacerItem, QSizePolicy
from .launcherdb import sqlServer
from .launcherweb import webControllerClass

######################################
# Default server information
######################################
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



######################################
# Adding addition servers page
######################################
class widgetAddServer(QWidget):
    def __init__(self, parent):
        layoutMain = None
        super(widgetAddServer, self).__init__(parent)

        labelServerName = QLabel("Server Name")
        labelServerDesc = QLabel("Server Description")
        labelServerIP = QLabel("Server IP")

        buttonSaveServer = QPushButton("Save")
        buttonCancel = QPushButton("Cancel")

        lineServerName = QLineEdit("")
        lineServerDesc = QLineEdit("")
        lineServerIP = QLineEdit("")

        verticalSpacer = QSpacerItem(10, 250, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        layoutEdit1 = QVBoxLayout()
        layoutEdit1.addWidget(labelServerName)
        layoutEdit1.addWidget(lineServerName)
        
        layoutEdit2 = QVBoxLayout()
        layoutEdit2.addWidget(labelServerDesc)
        layoutEdit2.addWidget(lineServerDesc)

        layoutEdit3 = QVBoxLayout()
        layoutEdit3.addWidget(labelServerIP)
        layoutEdit3.addWidget(lineServerIP)

        self.layoutMain = QVBoxLayout()
        self.layoutMain.addItem(verticalSpacer)
        self.layoutMain.addLayout(layoutEdit1)
        self.layoutMain.addLayout(layoutEdit2)
        self.layoutMain.addLayout(layoutEdit3)
        self.layoutMain.addItem(verticalSpacer)
        self.layoutMain.addWidget(buttonSaveServer)
        self.layoutMain.addWidget(buttonCancel)
        self.layoutMain.setAlignment(Qt.AlignTop)

        buttonSaveServer.clicked.connect(self.parent().on_buttonSaveServer_clicked(self))
        buttonCancel.clicked.connect(self.parent().on_buttonCancel_clicked)

        self.setLayout(layoutMain)



######################################
# Server List Page
######################################
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
        layoutServer.addWidget(labelMainText,    0, 0, 1, 1, Qt.AlignBottom)
        layoutServer.addWidget(listWidgetServer, 1, 0, 1, 4)
        layoutServer.addWidget(buttonJoinServer, 3, 1, 1, 2)
        layoutServer.addWidget(buttonSettings,   0, 3, 1, 1)
        layoutServer.addWidget(buttonAddServer,  0, 2, 1, 1)
        layoutServer.addItem(verticalSpacer,     2, 0)

        self.setLayout(layoutServer)



######################################
# Individual Server Pages
######################################
class widgetPageMain(QWidget):
    def __init__(self, parent):
        super(widgetPageMain, self).__init__(parent)
        dbServer = sqlServer()
        serverStruct = dbServer.sqlGetOne(0)
        webController = webControllerClass()
        labelRss = QLabel(webController.pullRss(serverStruct['serverRss']))
        logoImage = QLabel()
        bannerImage = QLabel()
        bannerImage.setPixmap(QPixmap(webController.pullImage(serverStruct['serverBanner'])))
        logoImage.setPixmap(QPixmap(webController.pullImage(serverStruct['serverLogo'])))

        labelDesc = QLabel(serverStruct['serverDescription'])
        labelTitle = QLabel(serverStruct['serverTitle'])
        labelInstall = QLabel(serverStruct['serverInstall'])

        editUser = QLineEdit("Enter")
        editPass = QLineEdit("Enter")
        checkboxUser = QCheckBox("Save Username?")
        buttonLog = QPushButton("Login")
        buttonPlay = QPushButton("Start Game")

        buttonBack = QPushButton("Back")
        buttonSettings = QPushButton("Settings")

        buttonPlay.hide()
        buttonBack.clicked.connect(self.parent().on_buttonBack_clicked)
        buttonSettings.clicked.connect(self.parent().on_buttonSettings_clicked)

        loginLayout = QVBoxLayout()
        loginLayout.addWidget(QLabel("User Name"))
        loginLayout.addWidget(editUser)
        loginLayout.addWidget(QLabel("Password"))
        loginLayout.addWidget(editPass)
        loginLayout.addWidget(checkboxUser)
        loginLayout.addWidget(buttonLog)

        layoutPage = QGridLayout()
        layoutPage.addWidget(labelTitle,     0, 2)
        layoutPage.addWidget(labelDesc,      1, 0)
        layoutPage.addWidget(labelRss,       1, 3)
        layoutPage.addWidget(logoImage,      0, 1)
        layoutPage.addWidget(bannerImage,    2, 0)
        layoutPage.addWidget(buttonSettings, 0, 3)
        layoutPage.addWidget(buttonBack,     0, 0)
        layoutPage.addLayout(loginLayout,    3, 0)
        layoutPage.addlayout(labelInstall,   4, 0)
 


######################################
# Individual Server Pages
# Still have to figure this page out
######################################
class widgetPageSetting(QWidget):
    def __init__(self, parent):
        super(widgetPageSetting, parent).__init__(self)

        labelFilePath = ""




######################################
# Main Window for UI
######################################
class mainWindow(QMainWindow):
    layoutWindow = None
    mainMenu = None
    serverMenu = None
    addServerMenu = None

    def __init__(self):
        super(mainWindow, self).__init__()

        self.setWindowTitle("LauncherZ")
        self.setFixedSize(QSize(1100, 600))

        self.mainMenu = widgetPageMain(self)
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
        #Open up a new window with settings menu so I can reuse this on all pages
        return

    def on_buttonAddServer_clicked(self):
        self.layoutWindow.setCurrentWidget(self.addServerMenu)

    def on_buttonJoinServer_clicked(self):
        self.layoutWindow.setCurrentWidget(self.mainMenu)

    def on_buttonBack_clicked(self):
        self.layoutWindow.setCurrentWidget(self.mainMenu)
    
    def on_buttonCancel_clicked(self):
        self.layoutWindow.setCurrentWidget(self.serverMenu)

    def on_buttonSaveServer_clicked(widget, self):
        self.layoutWindow.setCurrentWidget(self.serverMenu)
        serverList.serverDict.update({"nameText" : widget.layoutMain.layoutEdit1.lineServerName.text()})
        serverList.serverDict.update({"descriptionText" : widget.layoutMain.layoutEdit2.lineServerDesc.text()})
        serverList.serverDict.update({"serverIP" : widget.layoutMain.layoutEdit3.lineServerIP.text()})
