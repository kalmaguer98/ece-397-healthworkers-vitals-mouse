# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'draft.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from pyqtgraph import PlotWidget
import pyqtgraph as pg
from random import randint
from data_generator import singleGenerate
import csv 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 618)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.topDisplayDivider = QtWidgets.QFrame(self.centralwidget)
        self.topDisplayDivider.setGeometry(QtCore.QRect(0, 90, 801, 16))
        self.topDisplayDivider.setFrameShape(QtWidgets.QFrame.HLine)
        self.topDisplayDivider.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.topDisplayDivider.setObjectName("topDisplayDivider")
        self.menuDivider = QtWidgets.QFrame(self.centralwidget)
        self.menuDivider.setGeometry(QtCore.QRect(110, 100, 16, 501))
        self.menuDivider.setFrameShape(QtWidgets.QFrame.VLine)
        self.menuDivider.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.menuDivider.setObjectName("menuDivider")
        self.pushHistory = QtWidgets.QPushButton(self.centralwidget)
        self.pushHistory.setGeometry(QtCore.QRect(20, 140, 75, 23))
        self.pushHistory.setObjectName("pushHistory")
        self.pushAnalytics = QtWidgets.QPushButton(self.centralwidget)
        self.pushAnalytics.setGeometry(QtCore.QRect(20, 210, 75, 23))
        self.pushAnalytics.setObjectName("pushAnalytics")
        self.pushExport = QtWidgets.QPushButton(self.centralwidget)
        self.pushExport.setGeometry(QtCore.QRect(20, 280, 75, 23))
        self.pushExport.setObjectName("pushExport")
        self.pushOptions = QtWidgets.QPushButton(self.centralwidget)
        self.pushOptions.setGeometry(QtCore.QRect(20, 350, 75, 23))
        self.pushOptions.setObjectName("pushOptions")

        self.pushLive = QtWidgets.QPushButton(self.centralwidget)
        self.pushLive.setGeometry(QtCore.QRect(20, 550, 75, 23))
        self.pushLive.setObjectName("pushLive")

        self.pushGraph = QtWidgets.QPushButton(self.centralwidget)
        self.pushGraph.setGeometry(QtCore.QRect(200, 550, 75, 23))
        self.pushGraph.setObjectName("pushGraph")

        self.liveDisplay_1 = QtWidgets.QLabel(self.centralwidget)
        self.liveDisplay_1.setGeometry(QtCore.QRect(710, 20, 61, 61))
        self.liveDisplay_1.setObjectName("liveDisplay_1")
        self.liveDisplay_1.setStyleSheet("font: 30pt Arial MS")

        self.liveDisplay_2 = QtWidgets.QLabel(self.centralwidget)
        self.liveDisplay_2.setGeometry(QtCore.QRect(570, 20, 61, 61))
        self.liveDisplay_2.setObjectName("liveDisplay_2")
        self.liveDisplay_2.setStyleSheet("font: 30pt Arial MS")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 20, 61, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("heart.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(640, 20, 61, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("o2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(140, 120, 631, 311))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(210, 110, 151, 31))
        self.label_3.setObjectName("label_3")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(170, 490, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(620, 460, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(720, 460, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 20, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(630, 490, 41, 41))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(710, 490, 41, 41))
        self.textBrowser_4.setObjectName("textBrowser_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.graphWidgetLive = PlotWidget(self.centralwidget)
        self.graphWidgetLive.setGeometry(QtCore.QRect(40, 10, 400, 70))
        self.graphWidgetLive.setObjectName("graphWidgetLive")
        self.graphWidgetMain = PlotWidget(self.centralwidget)
        self.graphWidgetMain.setGeometry(QtCore.QRect(150, 140, 600, 275))
        self.graphWidgetMain.setObjectName("graphWidgetLive")

        self.textBrowser_4.setText('10')

        self.graphWidgetLive.setBackground('w')


        pen = pg.mkPen(color = (255, 0 ,0), width = 2)
        pen2 = pg.mkPen(color = (0, 255 ,0), width = 2)
        time = [1,2,3,4]
        heartRate = [90,87,88,85]
        oxygenLevel = [100,99,99,98]
        self.graphWidgetMain.setBackground('w')
        self.graphWidgetMain.plot(time, heartRate, pen=pen)
        self.graphWidgetMain.plot(time, oxygenLevel, pen=pen2)
  


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.pushExport.clicked.connect(self.show_popExport)

        self.pushOptions.clicked.connect(self.show_popOptions)

        self.pushLive.clicked.connect(self.show_graphLive)

        self.pushGraph.clicked.connect(self.show_graphMain)



    def update_plot_data(self):

        self.timeLive = self.timeLive[1:]  # Remove the first y element.
        self.timeLive.append(self.timeLive[-1] + 1)  # Add a new value 1 higher than the last.

        self.liveHR = self.liveHR[1:]  # Remove the first 
        self.liveHR.append(singleGenerate(80,5))


        self.liveO2 = self.liveO2[1:]  # Remove the first 
        self.liveO2.append(singleGenerate(99,1))

        
        self.data_line_1.setData(self.timeLive, self.liveHR)  # Update the data.
        self.data_line_2.setData(self.timeLive, self.liveO2)  # Update the data.

        self.liveDisplay_2.setText(str(self.liveHR[99]))
        self.liveDisplay_1.setText(str(self.liveO2[99]))
        

    def show_graphLive(self):
        self.timeLive = list(range(100))  # 100 time points
        self.liveHR = [0]*100
        self.liveO2 = [0]*100

        pen = pg.mkPen(color = (255, 0 ,0), width = 2)
        pen2 = pg.mkPen(color = (0, 0 ,255), width = 2)



        
        self.data_line_1 = self.graphWidgetLive.plot(self.timeLive, self.liveHR,pen = pen)
        self.data_line_2 = self.graphWidgetLive.plot(self.timeLive, self.liveO2,pen = pen2)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def show_graphMain(self):
        self.graphWidgetMain.clear()
        mainHR = [0]
        mainO2 = [0]
        mainTime = [0]
        file = open('testing', 'r')
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            print(row[0])
            mainTime.append(int(row[0]))
            mainHR.append(int(row[1]))
            mainO2.append(int(row[2]))
        #mainTime = mainTime[1:]
        #mainHR = mainHR[1:]
        #mainO2 = mainO2[1:]
        pen = pg.mkPen(color = (255, 0 ,0), width = 2)
        pen2 = pg.mkPen(color = (0, 255 ,0), width = 2)
        self.graphWidgetMain.setBackground('w')
        self.graphWidgetMain.plot(mainTime, mainHR, pen=pen)
        self.graphWidgetMain.plot(mainTime, mainO2, pen=pen2)


    def show_popExport(self):
    
        msg = QMessageBox()
        msg.setWindowTitle("Export")
        msg.setText("Here you can export data as a file")
        msg.setIcon(QMessageBox.Information)

        self.liveDisplay_1.setText("22")
        x = msg.exec()


    def show_popOptions(self):
        msg = QMessageBox()
        msg.setWindowTitle("Options")
        msg.setText("Here you can set various options")
        msg.setIcon(QMessageBox.Information)

        

        x = msg.exec()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushHistory.setText(_translate("MainWindow", "History"))
        self.pushAnalytics.setText(_translate("MainWindow", "Analytics"))
        self.pushExport.setText(_translate("MainWindow", "Export"))
        self.pushOptions.setText(_translate("MainWindow", "Options"))
        self.pushLive.setText(_translate("MainWindow","Start Live"))
        self.pushGraph.setText(_translate("MainWindow","Load Graph"))
        self.liveDisplay_1.setText("##")
        self.liveDisplay_2.setText("##")
        self.groupBox.setTitle(_translate("MainWindow", "History"))
        self.label_3.setText(_translate("MainWindow", "Graph goes here"))
        self.label_4.setText(_translate("MainWindow", "Heart Rate"))
        self.label_5.setText(_translate("MainWindow", "O2"))
        self.label_6.setText(_translate("MainWindow", "Live graph here"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">##</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">##</span></p></body></html>"))


    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
