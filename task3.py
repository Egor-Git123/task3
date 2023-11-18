from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from PyQt5.QtGui import QIcon, QPainter, QPen, QBrush
import io
from PyQt5 import uic
import random

from ui_fil import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.flag = False

        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            painter = QPainter(self)
            painter.setBrush(QBrush(Qt.yellow))
            c = random.randint(100, 200)
            painter.drawEllipse(40, 40, c, c)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())