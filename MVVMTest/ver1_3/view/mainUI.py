# Form implementation generated from reading ui file '/Users/a.klivtsov/Desktop/CodieStuff/businessThing/main/ver1_3/ui/uiTest/mainUI.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(933, 518)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_report = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_report.setGeometry(QtCore.QRect(680, 0, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_report.setFont(font)
        self.btn_report.setObjectName("btn_report")
        self.sw_main = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.sw_main.setGeometry(QtCore.QRect(10, 50, 911, 441))
        self.sw_main.setObjectName("sw_main")
        self.btn_calendar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_calendar.setGeometry(QtCore.QRect(800, 0, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_calendar.setFont(font)
        self.btn_calendar.setObjectName("btn_calendar")
        self.lbl_logo = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_logo.setGeometry(QtCore.QRect(20, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_logo.setFont(font)
        self.lbl_logo.setObjectName("lbl_logo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 933, 24))
        self.menubar.setObjectName("menubar")
        self.m_file = QtWidgets.QMenu(parent=self.menubar)
        self.m_file.setObjectName("m_file")
        self.m_settings = QtWidgets.QMenu(parent=self.menubar)
        self.m_settings.setObjectName("m_settings")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.m_file.menuAction())
        self.menubar.addAction(self.m_settings.menuAction())

        self.retranslateUi(MainWindow)
        self.sw_main.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_report.setText(_translate("MainWindow", "Отчёт"))
        self.btn_calendar.setText(_translate("MainWindow", "Календарь"))
        self.lbl_logo.setText(_translate("MainWindow", "Лого"))
        self.m_file.setTitle(_translate("MainWindow", "файл"))
        self.m_settings.setTitle(_translate("MainWindow", "настройки"))
