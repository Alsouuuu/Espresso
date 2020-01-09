from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic
import sqlite3
import sys


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffee.db')

        cur = self.con.cursor()
        result = cur.execute('SELECT * FROM cofe').fetchall()
        print(result)
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
