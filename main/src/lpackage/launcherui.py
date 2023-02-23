import sys
import urllib.parse
from PySide6.QtCore import QSize, Qt, QDir, QPoint
from PySide6.QtGui import QPixmap, QImage, QBrush, QPalette, QAction, QIcon
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout, QStatusBar
from PySide6.QtWidgets import QListWidget, QStackedWidget, QListWidgetItem, QLineEdit, QCheckBox, QToolBar
from PySide6.QtWidgets import QStackedLayout, QHBoxLayout, QLineEdit, QGridLayout, QSpacerItem, QSizePolicy
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
            "serverIp"           : "127.0.0.1",
            "serverPort"         : "75",
            "serverInstall"      : "https://www.google.com",
            "serverLogo"         : "https://i.imgur.com/suCqtLh.png",
            "serverBanner"       : "https://i.imgur.com/UebFpMK.jpeg",
            "serverRss"          : "https://www.gameskinny.com/games/monster-hunter-world/?format=rss"
    }
    def xServer(self):
        self.serverDict = {
            "serverTitle"        : "Euro server",
            "serverDescription"  : "Test element",
            "serverIp"           : "127.0.0.1",
            "serverPort"         : "75",
            "serverInstall"      : "https://www.google.com",
            "serverLogo"         : "https://i.imgur.com/suCqtLh.png",
            "serverBanner"       : "https://i.imgur.com/UebFpMK.jpeg",
            "serverRss"          : ""
    }
    def yServer(self):
        self.serverDict = {
            "serverTitle"        : "United Server",
            "serverDescription"  : "another test element",
            "serverIp"           : "127.0.0.1",
            "serverPort"         : "75",
            "serverInstall"      : "https://www.google.com",
            "serverLogo"         : "https://i.imgur.com/suCqtLh.png",
            "serverBanner"       : "https://i.imgur.com/UebFpMK.jpeg",
            "serverRss"          : ""
    }
    def zServer(self):
        self.serverDict = {
            "serverTitle"        : "community 1",
            "serverDescription"  : "3rd test server",
            "serverIp"           : "127.0.0.1",
            "serverPort"         : "75",
            "serverInstall"      : "https://www.google.com",
            "serverLogo"         : "https://i.imgur.com/suCqtLh.png",
            "serverBanner"       : "https://i.imgur.com/UebFpMK.jpeg",
            "serverRss"          : ""
    }



######################################
# Test widget for custom list item object
######################################
class widgetServerItem(QWidget):
    serverID = None
    def __init__(self, dbData, parent = None):
        super(widgetServerItem, self).__init__(parent)
        ssItem = """
        QWidget{
        border: 3px solid black;
        background-color : rgba(38, 38, 38, 220);
        }
        QLabel{ 
        background: none; 
        font: 12pt "Yu Gothic UI";
        border: none; 
        }
        """
        if not dbData['LOGO']:
            dbData.update({'LOGO' : 'https://i.imgur.com/suCqtLh.png'})
            
        self.parent().webController.pullImage(dbData['LOGO'])
        logoPull  = "./rsc/img/" + urllib.parse.quote_plus(dbData['LOGO'])
        imageLogo = QPixmap(logoPull)
        imagePing = QPixmap('img:serverdown.png')

        if self.parent().webController.serverPing(dbData['IP'], dbData['PORT']):
            imagePing = QPixmap('img:serverup.png')

        labelLogo = QLabel()
        labelPing = QLabel()
        labelLogo.setPixmap(imageLogo)
        labelPing.setPixmap(imagePing)
        labelLogo.setFixedSize(50, 50)
        labelLogo.setScaledContents(True)
        labelPing.setFixedSize(10, 10)
        labelPing.setScaledContents(True)

        self.serverID    = dbData['ID']
        labelName        = QLabel(dbData['TITLE'])
        labelDescription = QLabel(dbData['DESCRIPTION'])
        labelIp          = QLabel(dbData['IP'])
        labelDescription.setWordWrap(True)
        labelName.setWordWrap(True)
        labelName.setFixedWidth(125)
        labelIp.setFixedWidth(100)

        itemLayout = QHBoxLayout()
        itemLayout.addWidget(labelLogo)
        itemLayout.addWidget(labelName)
        itemLayout.addWidget(labelDescription)
        itemLayout.addWidget(labelIp)
        itemLayout.addWidget(labelPing)

        self.setAttribute(Qt.WA_StyledBackground)
        self.setStyleSheet(ssItem)
        self.setLayout(itemLayout)





######################################
# Adding addition servers page
######################################
class widgetPageServer(QWidget):
    lineServerName = None
    lineServerDesc = None
    lineServerIP   = None
    lineServerPort = None
    def __init__(self, parent):
        super(widgetPageServer, self).__init__(parent)

        labelServerName = QLabel("Server Name:")
        labelServerDesc = QLabel("Server Description:")
        labelServerIP   = QLabel("Server IP:")
        labelServerPort = QLabel("Server Port:")

        labelServerName.setMinimumWidth(175)
        labelServerDesc.setMinimumWidth(175)
        labelServerIP.setMinimumWidth(175)
        labelServerPort.setMinimumWidth(175)

        buttonSaveServer = QPushButton("Save")
        buttonSaveServer.setFixedSize(150, 30)

        self.lineServerName = QLineEdit("")
        self.lineServerDesc = QLineEdit("")
        self.lineServerIP   = QLineEdit("")
        self.lineServerPort = QLineEdit("")

        horizontalSpacer = QSpacerItem(65, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)


        layoutEdit1 = QHBoxLayout()
        layoutEdit1.addWidget(labelServerName)
        layoutEdit1.addWidget(self.lineServerName)
        
        layoutEdit2 = QHBoxLayout()
        layoutEdit2.addWidget(labelServerDesc)
        layoutEdit2.addWidget(self.lineServerDesc)

        layoutEdit3 = QHBoxLayout()
        layoutEdit3.addWidget(labelServerIP)
        layoutEdit3.addWidget(self.lineServerIP)

        layoutEdit4 = QHBoxLayout()
        layoutEdit4.addWidget(labelServerPort)
        layoutEdit4.addWidget(self.lineServerPort)

        layoutMain = QGridLayout()
        layoutMain.addWidget(buttonSaveServer, 1, 1, 1, 1)
        layoutMain.addLayout(layoutEdit1,      2, 1, 1, 5)
        layoutMain.addLayout(layoutEdit2,      3, 1, 1, 5)
        layoutMain.addLayout(layoutEdit3,      4, 1, 1, 5)
        layoutMain.addLayout(layoutEdit4,      5, 1, 1, 5)
        layoutMain.addItem(horizontalSpacer,   0, 6)
        layoutMain.addItem(horizontalSpacer,   0, 0)
        layoutMain.setAlignment(Qt.AlignTop)

        buttonSaveServer.clicked.connect(self.parent().on_buttonSaveServer_clicked)

        self.setLayout(layoutMain)



######################################
# Server List Page
######################################
class widgetPageList(QWidget):
    listWidgetServer = None
    def __init__(self, parent):
        super(widgetPageList, self).__init__(parent)
        self.listWidgetServer = self.listUpdate()
        buttonAddServer       = QPushButton("Add Server")
        buttonAddServer.setFixedSize(150, 30)
        self.listWidgetServer.setSpacing(7)

        self.listWidgetServer.setStyleSheet('QListWidget {border-image: url(./rsc/img/list.png) 5 0 0 0 stretch stretch;}')
        self.listWidgetServer.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.listWidgetServer.itemDoubleClicked.connect(self.parent().on_serverList_doubleClicked)
        buttonAddServer.clicked.connect(self.parent().on_buttonAddServer_clicked)

        verticalSpacer   = QSpacerItem(1, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        horizontalSpacer = QSpacerItem(65, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)


        layoutServer = QGridLayout()
        layoutServer.addWidget(self.listWidgetServer, 3, 1, 1, 5)
        layoutServer.addWidget(buttonAddServer,  2, 1, 1, 1)
        layoutServer.addItem(verticalSpacer,     2, 0)
        layoutServer.addItem(horizontalSpacer,   4, 6)
        layoutServer.addItem(verticalSpacer,     6, 0)
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

            dbItem = widgetServerItem(dataDict, self.parent())
            item.setSizeHint(dbItem.minimumSizeHint())

            returnList.setItemWidget(item, dbItem)
                
        return returnList 

    # Method called post init, p = stackedW p.p = window
    def listAddOne(self, serverData):
        self.parent().parent().dbServer.sqlInsert(serverData)
        row = self.parent().parent().dbServer.sqlGetLast()[0]
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

        list   = self.listWidgetServer
        dbItem = widgetServerItem(dataDict, self.parent().parent())
        item   = QListWidgetItem(list)
        list.addItem(item)
        item.setSizeHint(dbItem.minimumSizeHint())
        list.setItemWidget(item, dbItem)



######################################
# Individual Server Pages
######################################
class widgetPageMain(QWidget):
    def __init__(self, parent):
        super(widgetPageMain, self).__init__(parent)

    def loadPage(self, parent, serverID):
        ssPage = """
        QWidget#pageMain{
        border: 3px solid black;
        background-color : rgba(50, 50, 50, 220);
        }
        QWidget{
        border: 3px solid black;
        background-color : rgba(120, 120, 0, 120);
        font: 12pt "Yu Gothic UI";
        color : rgb(159, 190, 223);
        }
        QWidget#lBanner{
        background-color: none;
        border: 3px solid black;
        }
        QWidget#lDesc, QWidget#lTitle, QWidget#lInstall, QWidget#lLogo{
        background-color: none;
        border: none;
        }
        QLineEdit{
        background-color: rgba(120, 120, 120, 120);
        }
        QPushButton{
        background-color : rgb(51, 51, 0);
        border-image: url(./rsc/img/button.png) 0 0 0 0 stretch stretch;
        border : none;
        }
        QCheckBox{
        background: none;
        border: none;
        }
        """

        self.setObjectName('pageMain')
        serverDict      = self.serverGet(parent, serverID)
        labelRss        = self.rssWidget(parent, serverDict['RSS'])
        logoImage       = QLabel()
        bannerImage     = QLabel()

        if not serverDict['BANNER']:
            serverDict.update({"BANNER" : "https://i.imgur.com/UebFpMK.jpeg"})

        if not serverDict['LOGO']:
            serverDict.update({"LOGO" : "https://i.imgur.com/suCqtLh.png"})

        parent.webController.pullImage(serverDict['BANNER'])
        parent.webController.pullImage(serverDict['LOGO'])
        logoPull  = "./rsc/img/" + urllib.parse.quote_plus(serverDict['LOGO'])
        bannerPull  = "./rsc/img/" + urllib.parse.quote_plus(serverDict['BANNER'])

        bannerImage.setPixmap(QPixmap(bannerPull))
        logoImage.setPixmap(QPixmap(logoPull))
        bannerImage.setFixedSize(QSize(980, 100))
        logoImage.setFixedSize(QSize(100, 100))
        logoImage.setScaledContents(True)

        labelDesc      = QLabel(serverDict['DESCRIPTION'])
        labelTitle     = QLabel(serverDict['TITLE'])
        labelInstall   = QLabel(serverDict['INSTALL'])
        labelDesc.setFixedWidth(750)
        labelTitle.setFixedWidth(100)

        labelDesc.setObjectName("lDesc")
        labelTitle.setObjectName("lTitle")
        labelInstall.setObjectName("lInstall")
        bannerImage.setObjectName("lBanner")
        logoImage.setObjectName("lLogo")

        imageLayout = QHBoxLayout()
        imageLayout.addWidget(logoImage)
        imageLayout.addWidget(bannerImage)

        infoWrapper = QWidget()

        infoLayout = QHBoxLayout()
        infoLayout.addWidget(labelTitle)
        infoLayout.addWidget(labelDesc)
        infoLayout.addWidget(labelInstall)
        infoLayout.setAlignment(Qt.AlignLeft)
        infoWrapper.setLayout(infoLayout)

        editUser     = QLineEdit("Username")
        editPass     = QLineEdit("Password")
        checkboxUser = QCheckBox("Save Username?")
        buttonLog    = QPushButton("Login")
        buttonPlay   = QPushButton("Start Game")
        loginLayout  = QVBoxLayout()
        buttonPlay.hide()

        loginWrapper = QWidget()

        loginLayout.addWidget(editUser)
        loginLayout.addWidget(editPass)
        loginLayout.addWidget(checkboxUser)
        loginLayout.addWidget(buttonLog)
        loginLayout.setSpacing(5)
        loginWrapper.setLayout(loginLayout)

        verticalSpacer   = QSpacerItem(1, 75, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        horizontalSpacer = QSpacerItem(50, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        layoutPage = QGridLayout()
        layoutPage.addLayout(imageLayout,    0, 0, 1, 8)
        layoutPage.addWidget(infoWrapper,    1, 0, 1, 8)
        layoutPage.addWidget(labelRss,       2, 4, 6, 4)
        layoutPage.addWidget(loginWrapper,   6, 1, 1, 2)

        self.setAttribute(Qt.WA_StyledBackground)
        self.setStyleSheet(ssPage)
        self.setLayout(layoutPage)
 
    def rssWidget(self, parent, rssFeed):
        ssFeed = """
        QWidget#wFeed{
        background-color: rgb(45, 45, 65);
        border: 3px solid black;
        }
        QWidget{
        background-color: rgb(25, 25, 45);
        border: 1px solid black;
        }
        QLabel{
        background-color: none;
        border: none;
        }
        """
        returnFeed = QLabel("rss")
        if rssFeed:
            returnFeed = QWidget()
            returnFeed.setObjectName('wFeed')
            returnLayout = QVBoxLayout()

            rssDict = parent.webController.pullRss(rssFeed)

            for rss in rssDict:
                rssLayout = QVBoxLayout()
                labelName = QLabel(" " + rssDict[rss]['NAME'])
                labelDesc = QLabel(" " + rssDict[rss]['DESCRIPTION'])
                labelLink = QLabel(" " + rssDict[rss]['LINK'])
                labelDesc.setWordWrap(True)

                rssWrapper = QWidget()
                rssLayout.addWidget(labelName)
                rssLayout.addWidget(labelDesc)
                rssLayout.addWidget(labelLink)
                rssWrapper.setLayout(rssLayout)
                returnLayout.addWidget(rssWrapper)
            returnFeed.setLayout(returnLayout)
        returnFeed.setStyleSheet(ssFeed)
        return returnFeed

    def serverGet(self, parent, id):
        row = parent.dbServer.sqlGetOne(id)[0]
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
        buttonSave  = QPushButton("Save")
        buttonClear = QPushButton("Clear Data?")
        labelSkip   = QLabel("Skip Server List?")
        labelUser   = QLabel("Save Username?")
        checkSkip   = QCheckBox()
        checkUser   = QCheckBox()

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
        layoutMain.addWidget(buttonClear,      4, 1, 1, 1)
        layoutMain.addLayout(layoutEdit1,      2, 1, 1, 5)
        layoutMain.addLayout(layoutEdit2,      3, 1, 1, 5)
        layoutMain.addItem(verticalSpacer,     1, 0)
        layoutMain.addItem(horizontalSpacer,   0, 6)
        layoutMain.addItem(horizontalSpacer,   0, 0)
        layoutMain.setAlignment(Qt.AlignTop)
        
        self.setLayout(layoutMain)


class toolBarWidget(QWidget):
    def __init__(self, parent):
        super(toolBarWidget, self).__init__(parent)
        ssTool = """
        QPushButton{
        background-color: rgb(28, 53, 74);
        border: 1px solid rgb(0, 0, 0);
        }
        """

        imageSettings = QIcon("img:setting.png")
        imageBack     = QIcon("img:back.png")
        imageExit     = QIcon("img:x.png")

        buttonSettings = QPushButton()
        buttonBack     = QPushButton()
        buttonExit     = QPushButton()
        buttonExit.clicked.connect(self.parent().on_buttonExit_clicked)
        buttonBack.clicked.connect(self.parent().on_buttonBack_clicked)
        buttonSettings.clicked.connect(self.parent().on_buttonSettings_clicked)

        buttonSettings.setIcon(imageSettings)
        buttonBack.setIcon(imageBack)
        buttonExit.setIcon(imageExit)

        buttonSettings.setFixedSize(QSize(36, 36))
        buttonBack.setFixedSize(QSize(36, 36))
        buttonExit.setFixedSize(QSize(36, 36))

        buttonSettings.setIconSize(QSize(30, 30))
        buttonBack.setIconSize(QSize(30, 30))
        buttonExit.setIconSize(QSize(30, 30))

        labelVersion = QLabel("Version 0.1.0")

        horizontalSpacer = QSpacerItem(900, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        layoutTool = QHBoxLayout()
        layoutTool.addWidget(labelVersion)
        layoutTool.addItem(horizontalSpacer)
        layoutTool.addWidget(buttonBack)
        layoutTool.addWidget(buttonSettings)
        layoutTool.addWidget(buttonExit)

        layoutTool.setContentsMargins(0, 0, 5, 0)
        self.setAttribute(Qt.WA_StyledBackground)
        self.setStyleSheet(ssTool)
        self.setLayout(layoutTool)


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
    mainTool      = None
    pageIndex     = 0

    ssMain = """
    QListWidget{
        background-color : rgba(51, 51, 0, 220);
        border: 1px solid rgba(51, 77, 77, 180);
    }
    QLabel{
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
        color : rgb(159, 190, 223);
    }
    """
    ssWindow = """
    QToolBar{
        background-color : rgb(21, 39, 55);
        border: none
    }
    QMainWindow{
        border: 3px solid rgba(21, 39, 55, 200);
    }
    """


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

        self.mainTool      = QToolBar()
        self.mainTool.setFixedHeight(50)
        self.mainTool.setIconSize(QSize(32,32))
        self.mainTool.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.mainTool.addWidget(toolBarWidget(self))

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

        bgImage = QPixmap("img:bg.png")
        bgImage.scaled(QSize(1100, 600), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        mainPalette = QPalette()
        mainPalette.setBrush(QPalette.Window, QBrush(bgImage))

        self.setStatusBar(QStatusBar(self))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setPalette(mainPalette)
        self.setCentralWidget(self.stackedWidget)
        self.addToolBar(self.mainTool)
        self.setStyleSheet(self.ssWindow)

    def on_buttonSettings_clicked(self):
        self.stackedWidget.setCurrentIndex(3)

    def on_buttonAddServer_clicked(self):
        self.stackedWidget.setCurrentIndex(1)

    def on_buttonBack_clicked(self):
        self.stackedWidget.setCurrentIndex(2)
    
    def on_buttonCancel_clicked(self):
        self.stackedWidget.setCurrentIndex(2)

    def on_buttonSaveServer_clicked(self):
        name = self.pageServer.lineServerName.text()
        desc = self.pageServer.lineServerDesc.text()
        Ip   = self.pageServer.lineServerIP.text()
        port = self.pageServer.lineServerPort.text()
        serverData = {
            "serverTitle"        : name,
            "serverDescription"  : desc,
            "serverIp"           : Ip,
            "serverPort"         : port,
            "serverInstall"      : "",
            "serverLogo"         : "",
            "serverBanner"       : "",
            "serverRss"          : ""
            }

        self.stackedWidget.widget(2).listAddOne(serverData)
        self.stackedWidget.setCurrentIndex(2)

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

    def on_serverList_doubleClicked(self, item):
        self.stackedWidget.widget(0).loadPage(self ,self.sender().itemWidget(item).serverID)
        self.stackedWidget.setCurrentIndex(0)

    def rssGen(self):
        # Create widgets for each page and vertical layout to return
        return