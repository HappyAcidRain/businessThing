# Form implementation generated from reading ui file '/Users/a.klivtsov/Desktop/CodieStuff/businessThing/main/ver1_3/ui/reportUI.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1013, 495)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tw_reportTable = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tw_reportTable.setGeometry(QtCore.QRect(0, 0, 1011, 451))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tw_reportTable.sizePolicy().hasHeightForWidth())
        self.tw_reportTable.setSizePolicy(sizePolicy)
        self.tw_reportTable.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.tw_reportTable.setObjectName("tw_reportTable")
        self.tw_reportTable.setColumnCount(0)
        self.tw_reportTable.setRowCount(0)
        self.btn_save = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(890, 460, 121, 31))
        self.btn_save.setObjectName("btn_save")
        self.btn_export = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_export.setGeometry(QtCore.QRect(770, 460, 121, 31))
        self.btn_export.setObjectName("btn_export")
        self.f_msg = QtWidgets.QFrame(parent=self.centralwidget)
        self.f_msg.setGeometry(QtCore.QRect(340, 440, 300, 40))
        self.f_msg.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.f_msg.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.f_msg.setObjectName("f_msg")
        self.lbl_msg = QtWidgets.QLabel(parent=self.f_msg)
        self.lbl_msg.setGeometry(QtCore.QRect(0, 0, 300, 40))
        self.lbl_msg.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_msg.setObjectName("lbl_msg")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_save.setText(_translate("MainWindow", "сохранить"))
        self.btn_export.setText(_translate("MainWindow", "экспорт"))
        self.lbl_msg.setText(_translate("MainWindow", "Placeholder text!"))
