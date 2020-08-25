import sys
import sqlite3
from random import randint
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLCDNumber, QLineEdit


class FirstWidget(QWidget):
    def __init__(self, *names):
        super().__init__()
        uic.loadUi('data/main_page.ui', self)
        self.summ.clicked.connect(self.start_summ)
        self.mult.clicked.connect(self.start_mult)
        self.dedact.clicked.connect(self.start_dedact)
        self.divide.clicked.connect(self.start_divide)
        self.pixmap = QPixmap('data/img1.jpg').scaled(self.img.size(), Qt.KeepAspectRatio)
        self.img.setPixmap(self.pixmap)
        self.show()

    def start_summ(self):
        self.action_window = ActiontWidgetSumm(self)
        self.action_window.show()
        self.close()

    def start_mult(self):
        self.action_window = ActiontWidgetMult(self)
        self.action_window.show()
        self.close()

    def start_dedact(self):
        self.action_window = ActiontWidgetDedact(self)
        self.action_window.show()
        self.close()

    def start_divide(self):
        self.action_window = ActiontWidgetDivide(self)
        self.action_window.show()
        self.close()


class ActiontWidgetSumm(QWidget):
    def __init__(self, *names):
        super().__init__()
        uic.loadUi('data/page1.ui', self)
        self.pushButton.clicked.connect(self.check)
        self.initUI()

    def initUI(self):
        self.pixmap = QPixmap('data/img2.jpg').scaled(self.img.size(), Qt.KeepAspectRatio)
        self.img.setPixmap(self.pixmap)
        self.nums = [randint(0, 100), randint(0, 100)]
        while self.nums[0] + self.nums[1] > 100:
            self.nums = [randint(0, 100), randint(0, 100)]
        self.label.setText(str(self.nums[0]) + ' + ' + str(self.nums[1]) + ' = ')

    def check(self):
        if int(self.answer.text()) != int(self.nums[0] + self.nums[1]):
            self.status.setText('Неправильно! Попробуй ещё разок!')
            con = sqlite3.connect('data/results.db')
            cur = con.cursor()
            example = str(self.nums[0]) + ' + ' + str(self.nums[1])
            cur.execute(f"INSERT INTO mistakes(example, answer, correct) VALUES('{example}', '{self.answer.text()}', '{str(self.nums[0] * self.nums[1])}')").fetchall()
            cur.execute(f"UPDATE `total` SET `wrong` = `wrong` + 1").fetchall()
            con.commit()
        else:
            con = sqlite3.connect('data/results.db')
            cur = con.cursor()
            cur.execute(f"UPDATE `total` SET `correct` = `correct` + 1").fetchall()
            con.commit()
            self.action_window = NextWidget(self)
            self.action_window.show()
            self.close()


class ActiontWidgetMult(QWidget):
    def __init__(self, *names):
        super().__init__()
        uic.loadUi('data/page1.ui', self)
        self.pushButton.clicked.connect(self.check)
        self.initUI()

    def initUI(self):
        self.pixmap = QPixmap('data/img2.jpg').scaled(self.img.size(), Qt.KeepAspectRatio)
        self.img.setPixmap(self.pixmap)
        self.nums = [randint(0, 10), randint(0, 10)]
        self.label.setText(str(self.nums[0]) + ' * ' + str(self.nums[1]) + ' = ')

    def check(self):
        if int(self.answer.text()) != int(self.nums[0] * self.nums[1]):
            self.status.setText('Неправильно! Попробуй ещё разок!')
            con = sqlite3.connect('data/results.db')
            cur = con.cursor()
            example = str(self.nums[0]) + ' * ' + str(self.nums[1])
            cur.execute(f"INSERT INTO mistakes(example, answer, correct) VALUES('{example}', '{self.answer.text()}', '{str(self.nums[0] * self.nums[1])}')").fetchall()
            cur.execute(f"UPDATE `total` SET `wrong` = `wrong` + 1").fetchall()
            con.commit()
        else:
            con = sqlite3.connect('data/results.db')
            cur = con.cursor()
            cur.execute(f"UPDATE `total` SET `correct` = `correct` + 1").fetchall()
            con.commit()
            self.action_window = NextWidget(self)
            self.action_window.show()
            self.close()


class ActiontWidgetDedact(QWidget):
    def __init__(self, *names):
        super().__init__()
        uic.loadUi('data/page1.ui', self)
        self.pushButton.clicked.connect(self.check)
        self.initUI()

    def initUI(self):
        self.pixmap = QPixmap('data/img2.jpg').scaled(self.img.size(), Qt.KeepAspectRatio)
        self.img.setPixmap(self.pixmap)
        self.nums = [randint(0, 100), randint(0, 100)]
        if self.nums[0] < self.nums[1]:
            self.nums[0], self.nums[1] = self.nums[1], self.nums[0]
        self.label.setText(str(self.nums[0]) + ' - ' + str(self.nums[1]) + ' = ')

    def check(self):
        if int(self.answer.text()) != int(self.nums[0] - self.nums[1]):
            self.status.setText('Неправильно! Попробуй ещё разок!')
            con = sqlite3.connect('data/results.db')
            cur = con.cursor()
            example = str(self.nums[0]) + ' - ' + str(self.nums[1])
            cur.execute(f"INSERT INTO mistakes(example, answer, correct) VALUES('{example}', '{self.answer.text()}', '{str(self.nums[0] * self.nums[1])}')").fetchall()
            cur.execute(f"UPDATE `total` SET `wrong` = `wrong` + 1").fetchall()
            con.commit()
        else:
            con = sqlite3.connect('data/results.db')
            cur = con.cursor()
            cur.execute(f"UPDATE `total` SET `correct` = `correct` + 1").fetchall()
            con.commit()
            self.action_window = NextWidget(self)
            self.action_window.show()
            self.close()


class ActiontWidgetDivide(QWidget):
    def __init__(self, *names):
        super().__init__()
        uic.loadUi('data/page1.ui', self)
        self.pushButton.clicked.connect(self.check)
        self.initUI()

    def initUI(self):
        self.pixmap = QPixmap('data/img2.jpg').scaled(self.img.size(), Qt.KeepAspectRatio)
        self.img.setPixmap(self.pixmap)
        self.nums = [randint(0, 100), randint(1, 10)]
        while self.nums[0] % self.nums[1] != 0 or self.nums[0] / self.nums[1] > 10:
            self.nums = [randint(0, 100), randint(1, 10)]
        self.label.setText(str(self.nums[0]) + ' / ' + str(self.nums[1]) + ' = ')

    def check(self):
        if int(self.answer.text()) != int(self.nums[0] / self.nums[1]):
            self.status.setText('Неправильно! Попробуй ещё разок!')
            con = sqlite3.connect('data/results.db')
            cur = con.cursor()
            example = str(self.nums[0]) + ' / ' + str(self.nums[1])
            cur.execute(f"INSERT INTO mistakes(example, answer, correct) VALUES('{example}', '{self.answer.text()}', '{str(self.nums[0] * self.nums[1])}')").fetchall()
            cur.execute(f"UPDATE `total` SET `wrong` = `wrong` + 1").fetchall()
            con.commit()
        else:
            con = sqlite3.connect('data/results.db')
            cur = con.cursor()
            cur.execute(f"UPDATE `total` SET `correct` = `correct` + 1").fetchall()
            con.commit()
            self.action_window = NextWidget(self)
            self.action_window.show()
            self.close()


class NextWidget(QWidget):
    def __init__(self, *names):
        super().__init__()
        uic.loadUi('data/correct.ui', self)
        self.pushButton.clicked.connect(self.next)
        self.pixmap = QPixmap(['data/correct.jpg', 'data/correct2.jpg', 'data/correct3.jpg'][randint(0, 2)]).scaled(self.img.size(), Qt.KeepAspectRatio)
        self.img.setPixmap(self.pixmap)
        self.show()

    def next(self):
        self.action_window = FirstWidget(self)
        self.action_window.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstWidget()
    sys.exit(app.exec())
