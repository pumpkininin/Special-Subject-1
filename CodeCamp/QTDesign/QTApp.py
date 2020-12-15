# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 0, 461, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(130, 130, 301, 161))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(90, 30, 181, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 70, 47, 13))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(90, 70, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(130, 300, 301, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(20, 30, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(170, 30, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(140, 80, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_2.setGeometry(QtCore.QRect(140, 110, 42, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(80, 80, 47, 13))
        self.label_4.setObjectName("label_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 0, 301, 171))
        self.groupBox_3.setObjectName("groupBox_3")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 30, 70, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_4.setGeometry(QtCore.QRect(170, 30, 70, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_3.setGeometry(QtCore.QRect(140, 80, 42, 22))
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_4.setGeometry(QtCore.QRect(140, 110, 42, 22))
        self.spinBox_4.setObjectName("spinBox_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(80, 80, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(70, 110, 61, 21))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 490, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 490, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(380, 490, 47, 13))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.calculate)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Ứng dụng tính tiền phòng khám"))
        self.groupBox.setTitle(_translate("MainWindow", "Thông tin khách hàng"))
        self.label_2.setText(_translate("MainWindow", "Họ và tên"))
        self.label_3.setText(_translate("MainWindow", "Giới tính"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Nam"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Nữ"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Dịch vụ"))
        self.checkBox.setText(_translate("MainWindow", "Tẩy trắng"))
        self.checkBox_2.setText(_translate("MainWindow", "Niềng răng"))
        self.label_4.setText(_translate("MainWindow", "Nhổ răng"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Dịch vụ"))
        self.checkBox_3.setText(_translate("MainWindow", "Tẩy trắng"))
        self.checkBox_4.setText(_translate("MainWindow", "Niềng răng"))
        self.label_5.setText(_translate("MainWindow", "Nhổ răng"))
        self.label_6.setText(_translate("MainWindow", "Trồng răng"))
        self.pushButton.setText(_translate("MainWindow", "Tính tổng"))
        self.label_7.setText(_translate("MainWindow", "VND"))
    def calculate(self):
        prices = {
            "tayTrang": 100000,
            "niengRang": 200000,
            "nhoRang": 50000,
            "trongRang": 500000,
        }
        total = (0 if self.checkBox.checkState() == 0 else prices["tayTrang"]) \
            + (0 if self.checkBox_2.checkState() == 0 else prices["niengRang"]) \
            + int(self.spinBox_3.text()) * prices["nhoRang"] \
            + int(self.spinBox_4.text()) * prices["trongRang"]
        self.lineEdit_2.setText(str(total))
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Khách hàng {} | Giới tính {}!".format( self.lineEdit.text(),self.comboBox.currentText()))
        msg.setInformativeText(" Tổng chi phí là {}vnđ".format(str(total)))
        msg.setWindowTitle("Chi phí")
        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

