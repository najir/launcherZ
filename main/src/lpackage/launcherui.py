import sys
from PySide6.QtCore import QSize, Qt, QDir, QPoint
from PySide6.QtGui import QPixmap, QImage, QBrush, QPalette
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout, QListWidget, QStackedWidget, QListWidgetItem, QLineEdit, QCheckBox, QStackedLayout, QHBoxLayout, QLineEdit, QGridLayout, QSpacerItem, QSizePolicy
from .launcherdb import sqlServer
from .launcherweb import webControllerClass

######################################
# Default server information
######################################
class serverList():
    serverDict = {
        "serverDescription"  : "",
        "serverTitle"        : "",
        "serverLogo"         : "",
        "ServerBanner"       : "",
        "serverIp"           : "",
        "serverPort"         : "",
        "serverInstall"      : "",
        "serverRss"          : ""
    }
    def myServer(self):
        self.serverDict = {
            "serverDescription" : "",
            "serverTitle"       : "",
            "serverLogo"        : "",
            "ServerBanner"      : "",
            "serverIp"          : "",
            "serverPort"        : "",
            "serverInstall"     : "",
            "serverRss"         : ""
    }
    def xServer(self):
        self.serverDict = {
            "serverDescription" : "",
            "serverTitle"       : "",
            "serverLogo"        : "",
            "ServerBanner"      : "",
            "serverIp"          : "",
            "serverPort"        : "",
            "serverInstall"     : "",
            "serverRss"         : ""
    }
    def yServer(self):
        self.serverDict = {
            "serverDescription"  : "",
            "serverTitle"        : "",
            "serverLogo"         : "",
            "ServerBanner"       : "",
            "serverIp"           : "",
            "serverPort"         : "",
            "serverInstall"      : "",
            "serverRss"          : ""
    }
    def zServer(self):
        self.serverDict = {
            "serverDescription"  : "",
            "serverTitle"        : "",
            "serverLogo"         : "",
            "ServerBanner"       : "",
            "serverIp"           : "",
            "serverPort"         : "",
            "serverInstall"      : "",
            "serverRss"          : ""
    }
    def serverInit(self):
        # Checks if default server exists in table, creates them if not
        return



######################################
# Adding addition servers page
######################################
class widgetAddServer(QWidget):
    layoutMain = None
    def __init__(self, parent):
        super(widgetAddServer, self).__init__(parent)

        labelServerName = QLabel("Server Name:")
        labelServerDesc = QLabel("Server Description:")
        labelServerIP   = QLabel("Server IP:")
        labelServerPort = QLabel("Server Port:")
        buttonExit      = QPushButton("X")

        buttonExit.setMaximumWidth(20)
        labelServerName.setMinimumWidth(175)
        labelServerDesc.setMinimumWidth(175)
        labelServerIP.setMinimumWidth(175)
        labelServerPort.setMinimumWidth(175)

        buttonSaveServer = QPushButton("Save")
        buttonCancel     = QPushButton("Cancel")

        lineServerName = QLineEdit("")
        lineServerDesc = QLineEdit("")
        lineServerIP   = QLineEdit("")
        lineServerPort = QLineEdit("")

        verticalSpacer   = QSpacerItem(1, 75, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        horizontalSpacer = QSpacerItem(50, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)


        layoutEdit1 = QHBoxLayout()
        layoutEdit1.addWidget(labelServerName)
        layoutEdit1.addWidget(lineServerName)
        
        layoutEdit2 = QHBoxLayout()
        layoutEdit2.addWidget(labelServerDesc)
        layoutEdit2.addWidget(lineServerDesc)

        layoutEdit3 = QHBoxLayout()
        layoutEdit3.addWidget(labelServerIP)
        layoutEdit3.addWidget(lineServerIP)

        layoutEdit4 = QHBoxLayout()
        layoutEdit4.addWidget(labelServerPort)
        layoutEdit4.addWidget(lineServerPort)

        self.layoutMain = QGridLayout()
        self.layoutMain.addWidget(buttonSaveServer, 0, 5, 1, 1)
        self.layoutMain.addWidget(buttonCancel,     0, 4, 1, 1)
        self.layoutMain.addWidget(buttonExit,       0, 7, 1, 1)
        self.layoutMain.addLayout(layoutEdit1,      2, 1, 1, 5)
        self.layoutMain.addLayout(layoutEdit2,      3, 1, 1, 5)
        self.layoutMain.addLayout(layoutEdit3,      4, 1, 1, 5)
        self.layoutMain.addLayout(layoutEdit4,      5, 1, 1, 5)
        self.layoutMain.addItem(verticalSpacer,     1, 0)
        self.layoutMain.addItem(horizontalSpacer,   0, 6)
        self.layoutMain.addItem(horizontalSpacer,   0, 0)
        self.layoutMain.setAlignment(Qt.AlignTop)

        buttonSaveServer.clicked.connect(self.parent().on_buttonSaveServer_clicked)
        buttonCancel.clicked.connect(self.parent().on_buttonCancel_clicked)
        buttonExit.clicked.connect(self.parent().on_buttonExit_clicked)

        self.setLayout(self.layoutMain)



######################################
# Server List Page
######################################
class widgetPageServer(QWidget):
    def __init__(self, parent):
        super(widgetPageServer, self).__init__(parent)
        listWidgetServer = QListWidget()
        buttonSettings   = QPushButton("Settings")
        buttonAddServer  = QPushButton("Add Server")
        buttonExit       = QPushButton("X")
        buttonExit.setFixedWidth(20)

        buttonSettings.clicked.connect(self.parent().on_buttonSettings_clicked)
        buttonAddServer.clicked.connect(self.parent().on_buttonAddServer_clicked)
        buttonExit.clicked.connect(self.parent().on_buttonExit_clicked)

        verticalSpacer   = QSpacerItem(1, 75, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        horizontalSpacer = QSpacerItem(50, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        labelVersion = QLabel("Version 0.1.0")

        layoutServer = QGridLayout()
        layoutServer.addWidget(listWidgetServer, 3, 1, 1, 5)
        layoutServer.addWidget(labelVersion,     6, 1, 1, 1)
        layoutServer.addWidget(buttonSettings,   1, 5, 1, 1)
        layoutServer.addWidget(buttonAddServer,  1, 4, 1, 1)
        layoutServer.addWidget(buttonExit,       1, 7, 1, 1)    
        layoutServer.addItem(verticalSpacer,     2, 0)
        layoutServer.addItem(horizontalSpacer,   4, 6)
        layoutServer.addItem(verticalSpacer,     5, 0)
        layoutServer.addItem(horizontalSpacer,   4, 0)


        self.setLayout(layoutServer)



######################################
# Individual Server Pages
######################################
class widgetPageMain(QWidget):
    defaultDict = {
        "serverDescription" : "Default",
        "serverTitle"       : "Default",
        "serverLogo"        : "Default",
        "serverBanner"      : "Default",
        "serverIp"          : "Default",
        "serverInstall"     : "Default",
        "serverRss"         : "Default"
        }
    def __init__(self, parent):
        super(widgetPageMain, self).__init__(parent)
        webController   = webControllerClass()
        dbServer        = sqlServer()
        #serverDict      = dbServer.sqlGetOne(0)
        #if not serverDict:
        serverDict  = self.defaultDict 
        labelRss        = QLabel() #self.rssWidget()

        logoImage       = QLabel()
        bannerImage     = QLabel()
        #bannerImage.setPixmap(QPixmap(webController.pullImage(serverDict['serverBanner'])))
        #logoImage.setPixmap(QPixmap(webController.pullImage(serverDict['serverLogo'])))

        labelDesc      = QLabel(serverDict['serverDescription'])
        labelTitle     = QLabel(serverDict['serverTitle'])
        labelInstall   = QLabel(serverDict['serverInstall'])
        buttonBack     = QPushButton("Back")
        buttonSettings = QPushButton("Settings")

        buttonBack.clicked.connect(self.parent().on_buttonBack_clicked)
        buttonSettings.clicked.connect(self.parent().on_buttonSettings_clicked)

        editUser     = QLineEdit("Enter")
        editPass     = QLineEdit("Enter")
        checkboxUser = QCheckBox("Save Username?")
        buttonLog    = QPushButton("Login")
        buttonPlay   = QPushButton("Start Game")
        loginLayout  = QVBoxLayout()

        loginLayout.addWidget(QLabel("User Name"))
        loginLayout.addWidget(editUser)
        loginLayout.addWidget(QLabel("Password"))
        loginLayout.addWidget(editPass)
        loginLayout.addWidget(checkboxUser)
        loginLayout.addWidget(buttonLog)
        buttonPlay.hide()

        layoutPage = QGridLayout()
        layoutPage.addWidget(labelTitle,     0, 2)
        layoutPage.addWidget(labelDesc,      1, 0)
        layoutPage.addWidget(labelRss,       1, 3)
        layoutPage.addWidget(logoImage,      0, 1)
        layoutPage.addWidget(bannerImage,    2, 0)
        layoutPage.addWidget(buttonSettings, 0, 3)
        layoutPage.addWidget(buttonBack,     0, 0)
        layoutPage.addWidget(labelInstall,   4, 0)
        layoutPage.addLayout(loginLayout,    3, 0)
 
# Creates the rssWidget based on the web pull. Seperated from init due to complexity
    def rssWidget(self):
        return


######################################
# Settings page
# Checkbox: Auto load last server joined
# Checkbox: 
######################################
class widgetPageSetting(QWidget):
    def __init__(self, parent):
        super(widgetPageSetting, parent).__init__(self)
        return




######################################
# Main Window for UI
######################################
class mainWindow(QMainWindow):
    layoutWindow  = None
    mainMenu      = None
    serverMenu    = None
    addServerMenu = None

    ssMain = """
    QListWidget, QLabel{
        background-color : rgba(51, 51, 0, 220);
        border : 1px solid rgb(163, 163, 117);
    }
    QPushButton, QLineEdit{
        background-color : rgb(51, 51, 0);
        border : 1px solid rgb(163, 163, 117);
    }
    QWidget{
        font : 700 12pt "Segoe Print";
        color : rgb(159, 190, 223)
    }
    """
    ssLog  = ""
    ssFeed = ""
    ssInfo = ""


    def __init__(self):
        super(mainWindow, self).__init__()
        QDir.addSearchPath('img', './rsc/img')

        self.setWindowTitle("LauncherZ")
        self.setFixedSize(QSize(1100, 600))

        self.mainMenu      = widgetPageMain(self)
        self.serverMenu    = widgetPageServer(self)
        self.addServerMenu = widgetAddServer(self)

        self.serverMenu.setStyleSheet(self.ssMain)
        self.addServerMenu.setStyleSheet(self.ssMain)
        self.mainMenu.setStyleSheet(self.ssMain)

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.mainMenu)
        self.stackedWidget.addWidget(self.addServerMenu)
        self.stackedWidget.addWidget(self.serverMenu)
        self.stackedWidget.setCurrentIndex(2)

        bgImage = QImage("img:bg.png")
        bgImage.scaled(QSize(1100,600))
        mainPalette = QPalette()
        mainPalette.setBrush(QPalette.Window, QBrush(bgImage))

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setPalette(mainPalette)
        self.setCentralWidget(self.stackedWidget)
        self.setStyleSheet("border: 3px solid rgb(0, 51, 51);")

    def on_buttonSettings_clicked(self):
        #Open up a new window with settings menu so I can reuse this on all pages
        return

    def on_buttonAddServer_clicked(self):
        self.stackedWidget.setCurrentIndex(1)

    def on_buttonJoinServer_clicked(self):
        self.stackedWidget.setCurrentIndex(0)

    def on_buttonBack_clicked(self):
        self.stackedWidget.setCurrentIndex(2)
    
    def on_buttonCancel_clicked(self):
        self.stackedWidget.setCurrentIndex(2)

    def on_buttonSaveServer_clicked(self):
        self.stackedWidget.setCurrentIndex(2)
        #serverList.serverDict.update({"nameText" : widget.layoutMain.layoutEdit1.lineServerName.text()})
        #serverList.serverDict.update({"descriptionText" : widget.layoutMain.layoutEdit2.lineServerDesc.text()})
        #serverList.serverDict.update({"serverIP" : widget.layoutMain.layoutEdit3.lineServerIP.text()})
    
    def on_buttonExit_clicked(self):
        sys.exit()

    def mousePressEvent(self, event):
        self.anchor = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.anchor)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.anchor = event.globalPos()
