from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import pyqtSignal
from datetime import datetime
import time

import main


class timeday_thread(QtCore.QThread):
    
    datestime = pyqtSignal(str, str)

   
    
    def __init__(self):
        super(timeday_thread,self).__init__()
        

    def run(self):

        while True:
            date=datetime.now().strftime('%d-%m-%Y')
            times=datetime.now().strftime('%H:%M:%S')
            self.datestime.emit(date, times)
            time.sleep(1)


   