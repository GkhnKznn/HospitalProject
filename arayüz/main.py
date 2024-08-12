import pandas as pd
import snap7
from snap7 import util
import snap7.client as c
from snap7.util import *
from snap7.types import *
from snap7.exceptions import Snap7Exception
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import struct
import threading
import time
import datetime
import random
import numpy as np
import guncelArayuz
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import zaman_tarih
from PyQt5.QtCore import QTimer

plc = c.Client()  # burada olmazsa plc.get_connected() anlamiyor. Ayrica self.plc=c.Client() muhabbetini de anlamıyor.


class AppWindow(QtWidgets.QDialog, guncelArayuz.Ui_Dialog):
    def __init__(self):
        super(AppWindow, self).__init__()
        QWidget.__init__(self)
        self.setupUi(self)
        self.PB_TestiBalat.clicked.connect(self.test_start)
        self.PB_TestiBitir.clicked.connect(self.test_stop)
        self.PB_TestiDuraklat.clicked.connect(self.test_pause)
        self.PB_SonuclarKaydet.clicked.connect(self.to_excel) #data olarak parametre göndermen gerekiyor

        ############################################
        timing = zaman_tarih.timeday_thread()
        try:
            timing.datestime.connect(self.update_datetime)
        except Exception as e:
            print(e)
        timing1 = threading.Thread(target=timing.run)
        timing1.daemon = True
        timing1.start()
        ##############################################


    def test_start(self):

        basinc = []
        for row in range(0, 2):
            item = self.tableWidget.item(row, 0)
            itemtext = item.text()
            basinc.append(itemtext)
        PLC_Controller.innocuousPressure(self, int(basinc[0]))
        PLC_Controller.painPressure(self, int(basinc[1]))
        PLC_Controller.cycleNumber(self, int(self.LE_Cycle.text()))
        #self.LE_MevcutCycle.setText(str(plc1.readCycleNumber()))
        plc1.testStart()
        print("Test başladı.")

    def test_stop(self):
        plc1.testStop()
        print("Test durdu.")

    def test_pause(self):
        plc1.testPause()
        print("Test durdu.")


    def to_excel(self):
        hasta_adi = self.LE_HastaAdi.text()
        dosya_no = self.LE_DosyaNo.text()
        kimlik = self.LE_Kimlik.text()
        dogum_tarihi = self.LE_DogumTarihi.text()
        cinsiyet = self.LE_Cinsiyet.text()
        yas = self.LE_Yas.text()
        basinc = []
        for row in range(0, 2):
           item = self.tableWidget.item(row, 0)
           itemtext = item.text()
           basinc.append(itemtext)

        #Zaman değişkenleri
        time = datetime.datetime.now()
        hour = time.hour
        minute = time.minute

        day = time.day
        month = time.month
        year = time.year

        data = {
            'Hasta adı' : [hasta_adi],
            'Dosya no' : [dosya_no],
            'Kimlik' : [kimlik],
            'Tarihi' : [dogum_tarihi],
            'Cinsiyet' : [cinsiyet],
            'Yaş' : [yas],
            'Hazırlık basıncı' : basinc[0],
            'Uygulanan basınc' : basinc[1],
            'Saat': ["{}:{}".format(hour, minute)],
            'Tarih': ["{}.{}.{}".format(day, month, year)]
        }

        df = pd.DataFrame(data)

        dosya_adi = str(hasta_adi) + str(kimlik) + str(dogum_tarihi) + ".xlsx"
        print(dosya_adi)
        df.to_excel(dosya_adi, index=False)

    def readtable(self):
        basinc = []
        for row in range(0, 2):
            if self.tableWidget.item(row,0) != None:
                item = self.tableWidget.item(row, 0)
                itemtext = item.text()
                basinc.append(itemtext)
                flag=0
            else:
                flag = 1
        
        if flag == 1:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle("Warning")
            msg.setText("Boş olamaz")
            msg.exec_()
        elif flag==0:
            pass
        
        for n in basinc:
            if int(n) >= 10:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle("Warning")
                msg.setText("9'dan büyük olamaz veya boş olamaz")
                msg.exec_()
            else:
                PLC_Controller.innocuousPressure(self, int(basinc[0]))
                PLC_Controller.painPressure(self, int(basinc[1]))


    def update_datetime(self, date, times):
        self.LE_date.setText(date)
        self.LE_time.setText(times)
        self.LE_MevcutCycle.setText(str(plc1.readCycleNumber()))


    def value(self):
        value = 0
        return value
class PLC_Controller:

    def __init__(self, address, rack, slot):
        self.address = address
        self.rack = rack
        self.slot = slot


    # throws exception
    def connect(self):
        count = 0

        if plc.get_connected() == False:
            print("Try " + str(count) + " - Connecting to PLC: " +
                  self.address + ", Rack: " + str(self.rack) + ", Slot: " + str(self.slot))
            try:
                plc.connect(self.address, self.rack, self.slot)  # ('IP-address', rack, slot)
            except Exception as e:
                print("plc bağlantı koptu=", e)

        if plc.get_connected() == True:
            return plc.get_connected() == True

    def get_word(self, _bytearray, byte_index):
        data = _bytearray[byte_index:byte_index + 2]
        data = data[::-1]
        dword = struct.unpack('H', struct.pack('2B', *data))[0]
        return dword

    def emergencyStop(self):
        stop = 1
        stop = struct.pack('H', int(stop))
        stop = stop[::-1]
        plc.db_write(110, 0, stop)

    def testStart(self):
        start = 1
        start = struct.pack('H', int(start))
        start = start[::-1]
        plc.db_write(110, 2, start)
        time.sleep(1)
        stop = 0
        stop1 = struct.pack('H', int(stop))
        stop1 = stop1[::-1]
        plc.db_write(110, 2, stop1)

    def testPause(self):
        pause = 1
        pause = struct.pack('H', int(pause))
        pause = pause[::-1]
        plc.db_write(110, 4, pause)
        time.sleep(1)
        stop = 0
        stop1 = struct.pack('H', int(stop))
        stop1 = stop1[::-1]
        plc.db_write(110, 4, stop1)

    def testStop(self):
        stop = 1
        stop = struct.pack('H', int(stop))
        stop = stop[::-1]
        plc.db_write(110, 6, stop)
        time.sleep(1)
        stop = 0
        stop1 = struct.pack('H', int(stop))
        stop1 = stop1[::-1]
        plc.db_write(110, 6, stop1)

    def innocuousTime(self, time):
        time = struct.pack('H', int(time))
        time = time[::-1]
        plc.db_write(110, 16, time)

    def innocuousPressure(self, pressure):
        pressure = struct.pack('H', int(pressure))
        pressure = pressure[::-1]
        plc.db_write(110, 18, pressure)

    def painTime(self, time):
        time = struct.pack('H', int(time))
        time = time[::-1]
        plc.db_write(110, 20, time)

    def painPressure(self, pressure):
        pressure = struct.pack('H', int(pressure))
        pressure = pressure[::-1]
        plc.db_write(110, 22, pressure)

    def cycleNumber(self, number):
        number = struct.pack('H', int(number))
        number = number[::-1]
        print(number)
        plc.db_write(110, 24, number)

    def readCycleNumber(self):
        readCycleNumber = plc.db_read(110, 28, 2)
        readCycleNumber = PLC_Controller.get_word(self, readCycleNumber, 0)
        return readCycleNumber

    def disconnect(self):
        plc.disconnect()

    def readPressure(self):
        innocuousPressure = plc.db_read(110, 18, 2)
        innocuousPressure = PLC_Controller.get_word(self, innocuousPressure, 0)
        painPressure = plc.db_read(110, 22, 2)
        painPressure = PLC_Controller.get_word(self, painPressure, 0)
        return innocuousPressure, painPressure

    def readTime(self):
        innocuousTime = plc.db_read(110, 16, 2)
        innocuousTime = PLC_Controller.get_word(self, innocuousTime, 0)
        painTime = plc.db_read(110, 20, 2)
        painTime = PLC_Controller.get_word(self, painTime, 0)
        return innocuousTime, painTime

    def readData(self):
        data_received = plc.read_area(Areas.DB, 110, 0, 30)

        innTime = PLC_Controller.get_word(self,data_received,16)
        innPressure = PLC_Controller.get_word(self,data_received,18)
        painTime = PLC_Controller.get_word(self, data_received,20)
        painPressure = PLC_Controller.get_word(self, data_received, 22)
        data = [innTime, innPressure, painTime, painPressure]

        return data



if __name__ == "__main__":
    plc1 = PLC_Controller('192.168.30.100',0,1)
    plc1.connect()
    plc1.innocuousTime(25)
    plc1.painTime(5)
    app = QtWidgets.QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())

