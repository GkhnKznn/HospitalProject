# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guncelArayuz.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(924, 754)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.00492611, y1:0, x2:0.980296, y2:0.0284091, stop:0.0197044 rgba(22, 98, 159, 255), stop:1 rgba(255, 255, 255, 255));")
        self.widget.setObjectName("widget")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.L_Basinc_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.L_Basinc_2.setFont(font)
        self.L_Basinc_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.00492611, y1:0, x2:0.980296, y2:0.0284091, stop:0.0197044 rgba(22, 98, 159, 255), stop:1 rgba(255, 255, 255, 255));")
        self.L_Basinc_2.setObjectName("L_Basinc_2")
        self.verticalLayout_4.addWidget(self.L_Basinc_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalSlider = QtWidgets.QSlider(self.widget)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalLayout_2.addWidget(self.verticalSlider)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.textLabel = QtWidgets.QLabel(self.widget)
        self.textLabel.setMinimumSize(QtCore.QSize(101, 494))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.textLabel.setFont(font)
        self.textLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.textLabel.setObjectName("textLabel")
        self.verticalLayout_2.addWidget(self.textLabel)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_12.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.L_Hasta = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.L_Hasta.setFont(font)
        self.L_Hasta.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.00492611, y1:0, x2:0.980296, y2:0.0284091, stop:0.0197044 rgba(22, 98, 159, 255), stop:1 rgba(255, 255, 255, 255));")
        self.L_Hasta.setObjectName("L_Hasta")
        self.verticalLayout.addWidget(self.L_Hasta)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.L_HastaAdi = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.L_HastaAdi.setFont(font)
        self.L_HastaAdi.setStyleSheet("")
        self.L_HastaAdi.setObjectName("L_HastaAdi")
        self.horizontalLayout.addWidget(self.L_HastaAdi)
        self.LE_HastaAdi = QtWidgets.QLineEdit(self.widget)
        self.LE_HastaAdi.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.LE_HastaAdi.setObjectName("LE_HastaAdi")
        self.horizontalLayout.addWidget(self.LE_HastaAdi)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.L_DosyaNo = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.L_DosyaNo.setFont(font)
        self.L_DosyaNo.setStyleSheet("")
        self.L_DosyaNo.setObjectName("L_DosyaNo")
        self.horizontalLayout_11.addWidget(self.L_DosyaNo)
        self.LE_DosyaNo = QtWidgets.QLineEdit(self.widget)
        self.LE_DosyaNo.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.LE_DosyaNo.setObjectName("LE_DosyaNo")
        self.horizontalLayout_11.addWidget(self.LE_DosyaNo)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.L_Kimlik = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.L_Kimlik.setFont(font)
        self.L_Kimlik.setStyleSheet("")
        self.L_Kimlik.setObjectName("L_Kimlik")
        self.horizontalLayout_7.addWidget(self.L_Kimlik)
        self.LE_Kimlik = QtWidgets.QLineEdit(self.widget)
        self.LE_Kimlik.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.LE_Kimlik.setObjectName("LE_Kimlik")
        self.horizontalLayout_7.addWidget(self.LE_Kimlik)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.L_DogumTarihi = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.L_DogumTarihi.setFont(font)
        self.L_DogumTarihi.setStyleSheet("")
        self.L_DogumTarihi.setObjectName("L_DogumTarihi")
        self.horizontalLayout_6.addWidget(self.L_DogumTarihi)
        self.LE_DogumTarihi = QtWidgets.QLineEdit(self.widget)
        self.LE_DogumTarihi.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.LE_DogumTarihi.setObjectName("LE_DogumTarihi")
        self.horizontalLayout_6.addWidget(self.LE_DogumTarihi)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.L_Cinsiyet = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.L_Cinsiyet.setFont(font)
        self.L_Cinsiyet.setStyleSheet("")
        self.L_Cinsiyet.setObjectName("L_Cinsiyet")
        self.horizontalLayout_10.addWidget(self.L_Cinsiyet)
        self.LE_Cinsiyet = QtWidgets.QLineEdit(self.widget)
        self.LE_Cinsiyet.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.LE_Cinsiyet.setObjectName("LE_Cinsiyet")
        self.horizontalLayout_10.addWidget(self.LE_Cinsiyet)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.L_Yas = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.L_Yas.setFont(font)
        self.L_Yas.setStyleSheet("")
        self.L_Yas.setObjectName("L_Yas")
        self.horizontalLayout_9.addWidget(self.L_Yas)
        self.LE_Yas = QtWidgets.QLineEdit(self.widget)
        self.LE_Yas.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.LE_Yas.setObjectName("LE_Yas")
        self.horizontalLayout_9.addWidget(self.LE_Yas)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.LE_date = QtWidgets.QLineEdit(self.widget)
        self.LE_date.setObjectName("LE_date")
        self.horizontalLayout_13.addWidget(self.LE_date)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem2)
        self.LE_time = QtWidgets.QLineEdit(self.widget)
        self.LE_time.setObjectName("LE_time")
        self.horizontalLayout_13.addWidget(self.LE_time)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.L_Test = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.L_Test.setFont(font)
        self.L_Test.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.00492611, y1:0, x2:0.980296, y2:0.0284091, stop:0.0197044 rgba(22, 98, 159, 255), stop:1 rgba(255, 255, 255, 255));")
        self.L_Test.setObjectName("L_Test")
        self.verticalLayout_3.addWidget(self.L_Test)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(0, 0, 255))
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.horizontalLayout_4.addWidget(self.tableWidget)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.L_MevcutCycle = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.L_MevcutCycle.setFont(font)
        self.L_MevcutCycle.setStyleSheet("")
        self.L_MevcutCycle.setObjectName("L_MevcutCycle")
        self.horizontalLayout_5.addWidget(self.L_MevcutCycle)
        self.LE_MevcutCycle = QtWidgets.QLineEdit(self.widget)
        self.LE_MevcutCycle.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.LE_MevcutCycle.setObjectName("LE_MevcutCycle")
        self.horizontalLayout_5.addWidget(self.LE_MevcutCycle)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.L_Cycle = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.L_Cycle.setFont(font)
        self.L_Cycle.setStyleSheet("")
        self.L_Cycle.setObjectName("L_Cycle")
        self.horizontalLayout_8.addWidget(self.L_Cycle)
        self.LE_Cycle = QtWidgets.QLineEdit(self.widget)
        self.LE_Cycle.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.LE_Cycle.setObjectName("LE_Cycle")
        self.horizontalLayout_8.addWidget(self.LE_Cycle)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.PB_TestiBalat = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.PB_TestiBalat.setFont(font)
        self.PB_TestiBalat.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 255, 102, 255), stop:1 rgba(255, 255, 255, 255));")
        self.PB_TestiBalat.setObjectName("PB_TestiBalat")
        self.horizontalLayout_3.addWidget(self.PB_TestiBalat)
        self.PB_TestiDuraklat = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.PB_TestiDuraklat.setFont(font)
        self.PB_TestiDuraklat.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(236, 193, 143, 255), stop:1 rgba(255, 255, 255, 255));")
        self.PB_TestiDuraklat.setObjectName("PB_TestiDuraklat")
        self.horizontalLayout_3.addWidget(self.PB_TestiDuraklat)
        self.PB_TestiBitir = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.PB_TestiBitir.setFont(font)
        self.PB_TestiBitir.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(252, 1, 7, 255), stop:1 rgba(255, 255, 255, 255));")
        self.PB_TestiBitir.setObjectName("PB_TestiBitir")
        self.horizontalLayout_3.addWidget(self.PB_TestiBitir)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.PB_SonuclarKaydet = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.PB_SonuclarKaydet.setFont(font)
        self.PB_SonuclarKaydet.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.00492611, y1:0, x2:0.980296, y2:0.0284091, stop:0.0197044 rgba(22, 98, 159, 255), stop:1 rgba(255, 255, 255, 255));")
        self.PB_SonuclarKaydet.setObjectName("PB_SonuclarKaydet")
        self.verticalLayout_3.addWidget(self.PB_SonuclarKaydet)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout_12.addLayout(self.verticalLayout_5)
        self.horizontalLayout_15.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.L_Basinc_2.setText(_translate("Dialog", "Basınç Seviyesi"))
        self.textLabel.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">0</span></p></body></html>"))
        self.L_Hasta.setText(_translate("Dialog", "Hasta Bilgileri"))
        self.L_HastaAdi.setText(_translate("Dialog", "Hasta Adı:      "))
        self.L_DosyaNo.setText(_translate("Dialog", "Dosya No:      "))
        self.L_Kimlik.setText(_translate("Dialog", "TC.Kimlik No: "))
        self.L_DogumTarihi.setText(_translate("Dialog", "Doğum Tarihi: "))
        self.L_Cinsiyet.setText(_translate("Dialog", "Cinsiyet:         "))
        self.L_Yas.setText(_translate("Dialog", "Yaş:                "))
        self.L_Test.setText(_translate("Dialog", "Test Setup"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Hazırlık Basıncı"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "Uygulanan Basınç      "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Basınç Seviyesi"))
        self.L_MevcutCycle.setText(_translate("Dialog", "Mevcut Cycle Sayısı:"))
        self.L_Cycle.setText(_translate("Dialog", "Cycle:                       "))
        self.PB_TestiBalat.setText(_translate("Dialog", "Testi Başlat"))
        self.PB_TestiDuraklat.setText(_translate("Dialog", "Testi Duraklat"))
        self.PB_TestiBitir.setText(_translate("Dialog", "Testi Bitir"))
        self.PB_SonuclarKaydet.setText(_translate("Dialog", "Kaydet"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
