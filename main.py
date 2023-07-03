# база
import sys
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QDialog, QApplication, QTableWidgetItem, QColorDialog, QMenu
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QPoint, QTimer, QThread, QObject, Qt, QDate
from PyQt6.QtGui import QColor, QAction

# окна
import mainUI
import editUI

#прочее
import sqlite3

# основное окно
class MainWindow(QtWidgets.QMainWindow, mainUI.Ui_MainWindow, QDialog, QColor):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        menubar = self.menuBar()
        fileMenu = self.m_file

        self.loadAct = QAction('Загрузить', self)
        self.saveAct = QAction('Сохранить', self)
        self.m_file.addAction(self.saveAct)
        self.m_file.addAction(self.loadAct)

        self.saveAct.triggered.connect(self.save)
        self.loadAct.triggered.connect(self.write)

        self.setWindowTitle("BusinessThing")
        self.settingTable()

        self.user = "DefaultTable"

        self.tw_table.cellClicked.connect(self.edit)
        # self.tw_table.cellDoubleClicked.connect(self.clearCell)

        self.btn_notes.clicked.connect(self.edit)
        self.btn_save.clicked.connect(self.save)

        self.editWindow = EditWindow()
        self.editWindow.mainInfo.connect(self.converter)

    def settingTable(self):

        self.tw_table.setRowCount(12)
        self.tw_table.setColumnCount(31)

        for i in range(31):
            self.tw_table.setColumnWidth(i, 20)

        self.tw_table.setLineWidth(10)

        monthTyple = (
            'Январь', 'Февраль','Март',
            'Апрель','Май','Июнь',
            'Июль','Август','Сентябрь',
            'Октябрь','Ноябрь','Декабрь',
            )
        
        self.tw_table.setVerticalHeaderLabels(monthTyple)

    # TODO: make user change is able 
    def userChange(self):
        if user != userList:
            # CREATE TABLE DefaultTable (
            #   row     INTEGER,
            #   column_ INTEGER,
            #   notes   TEXT,
            #   color   INTEGER
            #   );
            pass

    def save(self):

        connect = sqlite3.connect("d.db")
        cursor = connect.cursor()

        for column in range(self.tw_table.columnCount()):

            for row in range(self.tw_table.rowCount()): 
                cell = self.tw_table.item(row, column)

                if cell:            
                    bg = self.tw_table.item(row, column).background()
                    note = self.tw_table.item(row, column).toolTip()

                    red, green, blue, alpha = bg.color().getRgb()
                    color = (red, green, blue)
                    color = str(color)

                    rowAndColumn = f"{row}:{column}"

                    cursor.execute(f"SELECT rowAndColumn FROM {self.user} WHERE rowAndColumn = ?",
                        (rowAndColumn,))
                    
                    dbRowAndColumn = cursor.fetchone()

                    if dbRowAndColumn is None:       
                        cursor.execute(f"INSERT INTO {self.user}(rowAndColumn, notes, color) VALUES(?, ?, ?);",
                            (rowAndColumn, note, color) )
                    else:
                        cursor.execute(f"UPDATE {self.user} SET notes = ? WHERE rowAndColumn = ?",
                            (note, rowAndColumn))

                        cursor.execute(f"UPDATE {self.user} SET color = ? WHERE rowAndColumn = ?", 
                            (color, rowAndColumn))
                    
                    connect.commit()

        connect.close()
                    
    def write(self):
        connect = sqlite3.connect("d.db")
        cursor = connect.cursor()

        cursor.execute(f"SELECT count(*) FROM {self.user}")
        count = cursor.fetchone()

        countTemp = ""
        for i in count:
            countTemp += str(i)
        count = int(countTemp)

        for index in range(count):
            if index != 0:

                cursor.execute(f"SELECT rowAndColumn FROM {self.user} WHERE ROWID = ?", (index,))
                rowAndColumnTemp = cursor.fetchone()

                rowAndColumn = ""
                for i in rowAndColumnTemp:
                    rowAndColumn += str(i)

                rowAndColumn = rowAndColumn.split(":")
                row = int(rowAndColumn[0])
                column = int(rowAndColumn[1])

                self.tw_table.setItem(row, column, QTableWidgetItem())
                self.tw_table.item(row, column).setBackground(QtGui.QColor(100,100,150))

                cursor.execute(f"SELECT notes FROM {self.user} WHERE ROWID = ?", (index,))
                notesTemp = cursor.fetchone()

                notes = ""
                for i in notesTemp:
                    notes += str(i)

                self.tw_table.item(row, column).setToolTip(notes)

                cursor.execute(f"SELECT color FROM {self.user} WHERE ROWID = ?", (index,))
                color = cursor.fetchone()
                print(color)

                

    def edit(self):
        self.editWindow.show()

    def converter(self, month, day, color, notes):    
        row = month - 1  
        column = day - 1

        self.tw_table.setItem(row, column, QTableWidgetItem())
        self.tw_table.item(row, column).setToolTip(notes)

        if color != None:
            self.tw_table.item(row, column).setBackground(color)
        else:
            self.tw_table.item(row, column).setBackground(QtGui.QColor(100,100,150))


# окно изменения
class EditWindow(QtWidgets.QMainWindow, editUI.Ui_MainWindow, QDialog):
    mainInfo = QtCore.pyqtSignal(int, int, object, str)
    otherInfo = QtCore.pyqtSignal(str)

    def __init__(self):
        super(EditWindow, self).__init__()
        self.setupUi(self)
 
        self.date_in.setDate(QDate.currentDate())
        self.date_out.setDate(QDate.currentDate())

        self.btn_color.clicked.connect(self.colorDialog)
        self.btn_save.clicked.connect(self.save)
        
        self.color = None
        self.notes = None

    def colorDialog(self):
        self.color = QColorDialog.getColor()

    def save(self):
        notes = self.te_notes.toPlainText()
        timeIn = self.time_in.time().toString(Qt.DateFormat.ISODate)
        timeOut = self.time_out.time().toString(Qt.DateFormat.ISODate)

        notes = f"Заезд: {timeIn}\nВыезд: {timeOut}\n\n{notes}"

        dayOut = self.date_out.date().dayOfYear()
        monthCount = self.date_in.date()
        day = self.date_in.date().day()
        curDay = self.date_in.date()
        addedMonths = 0
        addedDays = 0

        workie = True

        while workie:

            if curDay.dayOfYear() <= dayOut:

                if day <= monthCount.daysInMonth():
                    month = monthCount.month()
                    self.mainInfo.emit(month,day, self.color, notes)
                    day += 1
                    addedDays += 1
                    curDay = self.date_in.date().addDays(addedDays) 

                else:
                    day = 1
                    addedMonths += 1
                    monthCount = self.date_in.date().addMonths(addedMonths)

            else:
                monthCount = self.date_in.date()
                day = self.date_in.date().day()
                curDay = self.date_in.date()
                addedMonths = 0
                addedDays = 0
                workie = False

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MainWindow()
    m.show()    
    sys.exit(app.exec())
