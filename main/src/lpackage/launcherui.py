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
        "serverTitle"        : "",
        "serverDescription"  : "",
        "serverIp"           : "",
        "serverPort"         : "",
        "serverInstall"      : "",
        "serverLogo"         : "",
        "serverBanner"       : "",
        "serverRss"          : ""
    }

    def __init__(self, parent):
        boolExists = parent.dbServer.sqlGetOne(1)
        if not boolExists:
            self.myServer()
            parent.dbServer.sqlInsert(self.serverDict)

            self.xServer()
            parent.dbServer.sqlInsert(self.serverDict)

            self.yServer()
            parent.dbServer.sqlInsert(self.serverDict)

            self.zServer()
            parent.dbServer.sqlInsert(self.serverDict)

    def myServer(self):
        self.serverDict = {
            "serverTitle"        : "LimitZ",
            "serverDescription"  : "My personal server hosted on amazon web services",
            "serverIp"           : "111.111.111.111",
            "serverPort"         : "11111",
            "serverInstall"      : "example link",
            "serverLogo"         : "",
            "serverBanner"       : "",
            "serverRss"          : ""
    }
    def xServer(self):
        self.serverDict = {
            "serverTitle"        : "",
            "serverDescription"  : "",
            "serverIp"           : "",
            "serverPort"         : "",
            "serverInstall"      : "",
            "serverLogo"         : "",
            "serverBanner"       : "",
            "serverRss"          : ""
    }
    def yServer(self):
        self.serverDict = {
            "serverTitle"        : "",
            "serverDescription"  : "",
            "serverIp"           : "",
            "serverPort"         : "",
            "serverInstall"      : "",
            "serverLogo"         : "",
            "serverBanner"       : "",
            "serverRss"          : ""
    }
    def zServer(self):
        self.serverDict = {
            "serverTitle"        : "",
            "serverDescription"  : "",
            "serverIp"           : "",
            "serverPort"         : "",
            "serverInstall"      : "",
            "serverLogo"         : "",
            "serverBanner"       : "",
            "serverRss"          : ""
    }



######################################
# Test widget for custom list item object
######################################
class widgetServerItem(QWidget):
    serverID = None
    def __init__(self, dbData, parent = None):
        super(widgetServerItem, self).__init__(parent)

        #imageLogo = QImage()
        #imagePing = QImage()
        #imageLogo.scale()
        #imagePing.scale()

        #brushLogo = QBrush(imageLogo)
        #brushPing = QBrush(imagePing)
        #labelLogo = QLabel()
        #labelPing = QLabel()
        #labelLogo.setBackground(brushLogo)
        #labelPing.setBackground(brushPing)

        self.serverID    = dbData['ID']
        labelName        = QLabel(dbData['TITLE'])
        labelDescription = QLabel(dbData['DESCRIPTION'])

        itemLayout = QHBoxLayout()
        itemLayout.addWidget(labelName)
        itemLayout.addWidget(labelDescription)

        self.setLayout(itemLayout)





######################################
# Adding addition servers page
######################################
class widgetPageServer(QWidget):
    def __init__(self, parent):
        super(widgetPageServer, self).__init__(parent)

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

        layoutMain = QGridLayout()
        layoutMain.addWidget(buttonSaveServer, 0, 5, 1, 1)
        layoutMain.addWidget(buttonCancel,     0, 4, 1, 1)
        layoutMain.addWidget(buttonExit,       0, 7, 1, 1)
        layoutMain.addLayout(layoutEdit1,      2, 1, 1, 5)
        layoutMain.addLayout(layoutEdit2,      3, 1, 1, 5)
        layoutMain.addLayout(layoutEdit3,      4, 1, 1, 5)
        layoutMain.addLayout(layoutEdit4,      5, 1, 1, 5)
        layoutMain.addItem(verticalSpacer,     1, 0)
        layoutMain.addItem(horizontalSpacer,   0, 6)
        layoutMain.addItem(horizontalSpacer,   0, 0)
        layoutMain.setAlignment(Qt.AlignTop)

        buttonSaveServer.clicked.connect(self.parent().on_buttonSaveServer_clicked)
        buttonCancel.clicked.connect(self.parent().on_buttonCancel_clicked)
        buttonExit.clicked.connect(self.parent().on_buttonExit_clicked)

        self.setLayout(layoutMain)



######################################
# Server List Page
######################################
class widgetPageList(QWidget):
    def __init__(self, parent):
        super(widgetPageList, self).__init__(parent)
        listWidgetServer = self.listUpdate()
        buttonSettings   = QPushButton("Settings")
        buttonAddServer  = QPushButton("Add Server")
        buttonExit       = QPushButton("X")
        buttonExit.setFixedWidth(20)
        listWidgetServer.setStyleSheet('QListWidget {border-image: url(./rsc/img/list.png) 0 0 0 0 stretch stretch;}')
        listWidgetServer.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        listWidgetServer.itemDoubleClicked.connect(self.parent().on_serverList_doubleClicked)
        buttonSettings.clicked.connect(self.parent().on_buttonSettings_clicked)
        buttonAddServer.clicked.connect(self.parent().on_buttonAddServer_clicked)
        buttonExit.clicked.connect(self.parent().on_buttonExit_clicked)

        verticalSpacer   = QSpacerItem(1, 65, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        horizontalSpacer = QSpacerItem(65, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

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

    def listUpdate(self):
        dataDict = {}
        dbData = self.parent().dbServer.sqlGetAll()
        returnList = QListWidget()
        for row in dbData:
            dataDict.update({
                'ID'          :row[0],
                'TITLE'       :row[1],
                'DESCRIPTION' :row[2],
                'IP'          :row[3],
                'PORT'        :row[4],
                'INSTALL'     :row[5],
                'LOGO'        :row[6],
                'BANNER'      :row[7],
                'RSS'         :row[8]})
            item = QListWidgetItem(returnList)
            returnList.addItem(item)

            dbItem = widgetServerItem(dataDict)
            item.setSizeHint(dbItem.minimumSizeHint())

            returnList.setItemWidget(item, dbItem)
                
        return returnList 



######################################
# Individual Server Pages
######################################
class widgetPageMain(QWidget):
    def __init__(self, parent):
        super(widgetPageMain, self).__init__(parent)

    def loadPage(self, parent, serverID):
        serverDict      = self.serverGet(serverID)
        labelRss        = self.rssWidget()
        logoImage       = QLabel()
        bannerImage     = QLabel()
        bannerImage.setPixmap(QPixmap(parent.webController.pullImage(serverDict['BANNER'])))
        logoImage.setPixmap(QPixmap(parent.webController.pullImage(serverDict['LOGO'])))

        labelDesc      = QLabel(serverDict['DESCRIPTION'])
        labelTitle     = QLabel(serverDict['NAME'])
        labelInstall   = QLabel(serverDict['INSTALL'])
        buttonBack     = QPushButton("Back")
        buttonSettings = QPushButton("Settings")

        buttonBack.clicked.connect(parent.on_buttonBack_clicked)
        buttonSettings.clicked.connect(parent.on_buttonSettings_clicked)

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
        self.setLayout(layoutPage)
 
    def rssWidget(self):
        return

    def serverGet(self, id):
        dbData = self.parent().dbServer.sqlGetOne(id)
        row = dbData[0]
        dataDict = {
                'ID'          :row[0],
                'TITLE'       :row[1],
                'DESCRIPTION' :row[2],
                'IP'          :row[3],
                'PORT'        :row[4],
                'INSTALL'     :row[5],
                'LOGO'        :row[6],
                'BANNER'      :row[7],
                'RSS'         :row[8]}
        return dataDict


######################################
# Settings page
# Checkbox: Auto load last server joined
# Checkbox: 
######################################
class widgetPageSetting(QWidget):
    def __init__(self, parent):
        super(widgetPageSetting, self).__init__(parent)
        buttonBack  = QPushButton("Back")
        buttonSave  = QPushButton("Save")
        buttonClear = QPushButton("Clear Data?")
        buttonExit  = QPushButton("X")
        labelSkip   = QLabel("Skip Server List?")
        labelUser   = QLabel("Save Username?")
        checkSkip   = QCheckBox()
        checkUser   = QCheckBox()

        buttonExit.setFixedWidth(20)
        checkSkip.setStyleSheet("border: none")
        checkUser.setStyleSheet("border: none")
        labelSkip.setFixedWidth(150)
        labelUser.setFixedWidth(150)
        buttonClear.setFixedWidth(150)


        layoutEdit1 = QHBoxLayout()
        layoutEdit1.addWidget(labelSkip)
        layoutEdit1.addWidget(checkSkip)

        layoutEdit2 = QHBoxLayout()
        layoutEdit2.addWidget(labelUser)
        layoutEdit2.addWidget(checkUser)

        layoutEdit1 = QHBoxLayout()
        layoutEdit1.addWidget(labelSkip)
        layoutEdit1.addWidget(checkSkip)

        verticalSpacer   = QSpacerItem(1, 75, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        horizontalSpacer = QSpacerItem(50, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        layoutMain = QGridLayout()
        layoutMain.addWidget(buttonSave,       0, 5, 1, 1)
        layoutMain.addWidget(buttonBack,       0, 4, 1, 1)
        layoutMain.addWidget(buttonExit,       0, 7, 1, 1)
        layoutMain.addWidget(buttonClear,      4, 1, 1, 1)
        layoutMain.addLayout(layoutEdit1,      2, 1, 1, 5)
        layoutMain.addLayout(layoutEdit2,      3, 1, 1, 5)
        layoutMain.addItem(verticalSpacer,     1, 0)
        layoutMain.addItem(horizontalSpacer,   0, 6)
        layoutMain.addItem(horizontalSpacer,   0, 0)
        layoutMain.setAlignment(Qt.AlignTop)

        buttonExit.clicked.connect(self.parent().on_buttonExit_clicked)
        buttonBack.clicked.connect(self.parent().on_buttonBack_clicked)
        buttonClear.clicked.connect(self.parent().on_buttonClear_clicked)
        
        self.setLayout(layoutMain)



######################################
# Main Window for UI
######################################
class mainWindow(QMainWindow):
    webController = None
    dbServer      = None
    dbServerList  = None
    layoutWindow  = None
    pageMain      = None
    pageList      = None
    pageServer    = None
    pageSetting   = None
    pageIndex     = 0

    ssMain = """
    QListWidget, QLabel{
        background-color : rgba(51, 51, 0, 220);
        border : 1px solid rgb(163, 163, 117);
    }
    QPushButton{
        background-color : rgb(51, 51, 0);
        border-image: url(./rsc/img/button.png) 0 0 0 0 stretch stretch;
        border : None
    }
    QLineEdit{
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

        self.webController = webControllerClass()
        self.dbServer      = sqlServer()
        self.dbServerList  = serverList(self)

        self.pageMain      = widgetPageMain(self)
        self.pageList      = widgetPageList(self)
        self.pageServer    = widgetPageServer(self)
        self.pageSetting   = widgetPageSetting(self)


        self.pageList.setStyleSheet(self.ssMain)
        self.pageServer.setStyleSheet(self.ssMain)
        self.pageMain.setStyleSheet(self.ssMain)
        self.pageSetting.setStyleSheet(self.ssMain)

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.pageMain)
        self.stackedWidget.addWidget(self.pageServer)
        self.stackedWidget.addWidget(self.pageList)
        self.stackedWidget.addWidget(self.pageSetting)
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
        self.stackedWidget.setCurrentIndex(3)

    def on_buttonAddServer_clicked(self):
        self.stackedWidget.setCurrentIndex(1)

    def on_buttonBack_clicked(self):
        self.stackedWidget.indexOf(2).updateList()
        self.stackedWidget.setCurrentIndex(2)
    
    def on_buttonCancel_clicked(self):
        self.stackedWidget.indexOf(2).updateList()
        self.stackedWidget.setCurrentIndex(2)

    def on_buttonSaveServer_clicked(self):
        self.stackedWidget.indexOf(2).updateList()
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

    def on_buttonClear_clicked(self):
        return

    def on_serverList_doubleClicked(self):
        self.stackedWidget.indexOf(0).loadPage(self, self.sender().selectedItems().serverID)
        self.stackedWidget.setCurrentIndex(0)

    def rssGen(self):
        # Create widgets for each page and vertical layout to return
        return