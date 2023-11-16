from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
import sys
import random


class Square1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.SCREEN_SIZE = [800, 900]
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, *self.SCREEN_SIZE)
        self.setWindowTitle('Круги')
        self.btn = QPushButton(self)
        self.btn.setText('Нарисовать круг')
        self.btn.move(100, 10)
        self.flag = False
        self.btn.clicked.connect(self.circle)

    def circle(self):
        self.flag = True
        self.n = 10
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            qp.setPen(QColor(r, g, b))
            qp.setBrush(QColor(r, g, b))
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
