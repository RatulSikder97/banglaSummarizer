# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox
from PyQt5.QtWidgets import QCalendarWidget, QFontDialog, QColorDialog, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog

import preprosess,score,genSummary,smanalysis

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(488, 424)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        MainWindow.setDocumentMode(False)

        self.textEdit = QtWidgets.QTextEdit(MainWindow)
        self.textEdit.setGeometry(QtCore.QRect(160, 100, 300, 250))
        self.textEdit.setObjectName("textEdit")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 270, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(30, 330, 91, 45))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        self.pushButton5.setFont(font)
        self.pushButton5.setObjectName("pushButton5")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 80, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(8)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 140, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(7)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setMouseTracking(True)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_3.setAcceptDrops(False)
        self.pushButton_3.setAutoFillBackground(True)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 200, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(8)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 488, 21))
        self.menubar.setObjectName("menubar")
        self.menuFILE = QtWidgets.QMenu(self.menubar)
        self.menuFILE.setObjectName("menuFILE")
        self.menuEDIT = QtWidgets.QMenu(self.menubar)
        self.menuEDIT.setObjectName("menuEDIT")
        self.menuHELP = QtWidgets.QMenu(self.menubar)
        self.menuHELP.setObjectName("menuHELP")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_file.setObjectName("actionOpen_file")
        self.actionSave_file = QtWidgets.QAction(MainWindow)
        self.actionSave_file.setObjectName("actionSave_file")
        self.actionSetting = QtWidgets.QAction(MainWindow)
        self.actionSetting.setObjectName("actionSetting")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionFONT = QtWidgets.QAction(MainWindow)
        self.actionFONT.setObjectName("actionFONT")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionPAQ = QtWidgets.QAction(MainWindow)
        self.actionPAQ.setObjectName("actionPAQ")
        self.menuFILE.addAction(self.actionOpen_file)
        self.menuFILE.addAction(self.actionSave_file)
        self.menuFILE.addAction(self.actionSetting)
        self.menuFILE.addAction(self.actionExit)
        self.menuEDIT.addAction(self.actionFONT)
        self.menuHELP.addAction(self.actionAbout)
        self.menuHELP.addAction(self.actionPAQ)
        self.menubar.addAction(self.menuFILE.menuAction())
        self.menubar.addAction(self.menuEDIT.menuAction())
        self.menubar.addAction(self.menuHELP.menuAction())
        self.actionSave_file.triggered.connect(self.saveFile)
        self.actionSave_file.setShortcut('Ctrl+s')
        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Document summerizer"))
        self.pushButton.setText(_translate("MainWindow", "ABOUT"))
        self.pushButton5.setText(_translate("MainWindow", "EXIT"))
        self.label.setText(_translate("MainWindow", "Bangla Document Summerizer"))
        self.pushButton_2.setText(_translate("MainWindow", "OPEN"))
        self.pushButton_3.setText(_translate("MainWindow", "SUMMARIZE"))
        self.pushButton_4.setText(_translate("MainWindow", "HELP"))
        self.menuFILE.setTitle(_translate("MainWindow", "FILE"))
        self.menuEDIT.setTitle(_translate("MainWindow", "EDIT"))
        self.menuHELP.setTitle(_translate("MainWindow", "HELP"))
        self.actionOpen_file.setText(_translate("MainWindow", "Open File"))
        self.actionSave_file.setText(_translate("MainWindow", "Save file"))
        self.actionSetting.setText(_translate("MainWindow", "Setting"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionFONT.setText(_translate("MainWindow", "FONT"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionPAQ.setText(_translate("MainWindow", "FAQ"))
        self.pushButton_2.clicked.connect(self.openfile)
        self.actionOpen_file.triggered.connect(self.openfile)
        self.actionOpen_file.setShortcut('Ctrl+O')

        self.actionExit.triggered.connect(self.closeApplication)
        self.actionExit.setShortcut('Ctrl+Q')
        self.pushButton5.clicked.connect(self.closeApplication)
        self.pushButton_3.clicked.connect(self.summer)
        self.pushButton.clicked.connect(self.about)
        self.pushButton_4.clicked.connect(self.help)
        self.actionFONT.triggered.connect(self.font_choice)


    def pri(self):
        print('Ratul')

    def openfile(self, MainWindow):
         name, _ = QFileDialog.getOpenFileName(self, 'Open file', options=QFileDialog.DontUseNativeDialog)
         f = open( name,encoding='utf-8')  # New line


         with f:
             text=f.read()
             self.textEdit.setText(text)
             f.close()


    def summer(self):
        text = self.textEdit.toPlainText()
        #print(text)
        sent = preprosess.prePunc(text)
        # call tokenizer
        words = preprosess.wordToke(sent);
        # print(words)

        # punc remove
        puncFree = preprosess.puncRem(words)
        # print(puncFree)

        # Stopword removing
        noStWord = preprosess.remStWors(puncFree)
        # print(noStWord)

        wordScore = score.scoreWord(noStWord)
        # print(wordScore)

        sentSclist = score.scList(sent, wordScore)
        scDict = score.sentScDict(sent, wordScore)
        # print(scDict)

        priSummary = genSummary.genSummary(sent, scDict)
        # print(priSummary)


        finalOut = smanalysis.finalSummary(priSummary)
        self.textEdit.setText(finalOut)

    def saveFile(self):
        name, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'actionSave_file',options=QFileDialog.DontUseNativeDialog)
        file = open(name, 'w', encoding='utf-8')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    def about(self):
        file=open('About.txt',encoding='utf-8')
        r=file.read()
        self.textEdit.setText(r)
        file.close()

    def font_choice(self):
        font = QFontDialog.getFont()
        self.textEdit.setFont(font)

    def help(self):
        filee=open('./help.txt','r')
        rr=filee.read()
        self.textEdit.setText(rr)
        filee.close()


    def closeApplication(self):

        choice = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if choice == QMessageBox.Yes:
            print('quit application')
            sys.exit()
        else:
            pass




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

