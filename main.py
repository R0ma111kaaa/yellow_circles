import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class RandomCircle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)

        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()

        qp.begin(self)
        self.draw_random_circle(qp)
        qp.end()

    def draw_random_circle(self, qp):
        qp.setBrush(QColor("yellow"))
        qp.drawEllipse(0, 0, 500, 500)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    rc = RandomCircle()
    rc.show()
    sys.exit(app.exec_())
