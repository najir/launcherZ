
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxlayout

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        labelServer = QLabel("Server List")

        button = QPushButton("Press Me")
        button.setCheckable(True)
        button.clicked.connect(self.on_button_clicked)

        layoutMain = QVBoxlayout()
        layoutMain.addWidget(labelServer)
        layoutMain.addWidget(button)

        self.setWindowTitle("LauncherZ")
        self.setFixedSize(QSize(1000, 600))
        self.setCentralWidget(button)

        container = QWidget()
        container.setLayout(layoutMain)

        self.setCentralWidget(container)

    def on_button_clicked(self):
        print("clicked!")