from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
import sys
import random


class Square1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = False
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.circle)

    def circle(self):
        self.flag = True
        self.n = 10
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(255, 255, 0))
            qp.setBrush(QColor(255, 255, 0))
            x = random.randint(100, 700)
            y = random.randint(100, 500)
            w = h = random.randint(10, 100)
            qp.drawEllipse(x, y, w, h)
            qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Square1()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
