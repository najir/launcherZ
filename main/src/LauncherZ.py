'''
Isaac Perks
2/11/23
FrontierZ Launcher for MHF through custom Binaries found in README.
'''
from lpackage import *
import sys

app = QApplication(sys.argv)

window = mainWindow()
window.show()

app.exec_()

