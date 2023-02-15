######################################
# Isaac Perks
# 2/14/23
# Launcher application to pair with IEless binaries
######################################
from lpackage import *
import sys

app = QApplication(sys.argv)

window = mainWindow()
window.show()

app.exec_()

