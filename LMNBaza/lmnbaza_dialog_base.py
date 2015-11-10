# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lmnbaza_dialog_base.ui'
#
# Created: Thu Nov 05 13:52:33 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(455, 464)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 431, 71))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.commandLinkButton_dane = QtGui.QCommandLinkButton(self.groupBox)
        self.commandLinkButton_dane.setGeometry(QtCore.QRect(300, 10, 121, 51))
        self.commandLinkButton_dane.setObjectName(_fromUtf8("commandLinkButton_dane"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 281, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 90, 431, 61))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.commandLinkButton_warstwy = QtGui.QCommandLinkButton(self.groupBox_2)
        self.commandLinkButton_warstwy.setGeometry(QtCore.QRect(300, 10, 121, 41))
        self.commandLinkButton_warstwy.setObjectName(_fromUtf8("commandLinkButton_warstwy"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 20, 281, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 160, 431, 121))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 20, 221, 91))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.radioButton = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton.setGeometry(QtCore.QRect(20, 20, 181, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 40, 181, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton_3.setEnabled(False)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 60, 82, 17))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.commandLinkButton_import = QtGui.QCommandLinkButton(self.groupBox_3)
        self.commandLinkButton_import.setGeometry(QtCore.QRect(300, 70, 121, 41))
        self.commandLinkButton_import.setObjectName(_fromUtf8("commandLinkButton_import"))
        self.groupBox_5 = QtGui.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 280, 431, 131))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_2 = QtGui.QLabel(self.groupBox_5)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 151, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.progressBar_pliki = QtGui.QProgressBar(self.groupBox_5)
        self.progressBar_pliki.setGeometry(QtCore.QRect(10, 40, 411, 23))
        self.progressBar_pliki.setMaximum(1000)
        self.progressBar_pliki.setProperty("value", 0)
        self.progressBar_pliki.setObjectName(_fromUtf8("progressBar_pliki"))
        self.progressBar_wiersze = QtGui.QProgressBar(self.groupBox_5)
        self.progressBar_wiersze.setGeometry(QtCore.QRect(10, 90, 411, 23))
        self.progressBar_wiersze.setProperty("value", 50)
        self.progressBar_wiersze.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_wiersze.setInvertedAppearance(False)
        self.progressBar_wiersze.setFormat(_fromUtf8("%p%"))
        self.progressBar_wiersze.setObjectName(_fromUtf8("progressBar_wiersze"))
        self.label_3 = QtGui.QLabel(self.groupBox_5)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(370, 430, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.commandLinkButton_dane)
        Dialog.setTabOrder(self.commandLinkButton_dane, self.lineEdit_2)
        Dialog.setTabOrder(self.lineEdit_2, self.commandLinkButton_warstwy)
        Dialog.setTabOrder(self.commandLinkButton_warstwy, self.radioButton)
        Dialog.setTabOrder(self.radioButton, self.radioButton_2)
        Dialog.setTabOrder(self.radioButton_2, self.radioButton_3)
        Dialog.setTabOrder(self.radioButton_3, self.commandLinkButton_import)
        Dialog.setTabOrder(self.commandLinkButton_import, self.pushButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "1. Wybierz plik zip z danymi", None))
        self.commandLinkButton_dane.setText(_translate("Dialog", "wybierz plik", None))
        self.groupBox_2.setTitle(_translate("Dialog", "2. Wybierz plik zip z warstwami pochodnymi", None))
        self.commandLinkButton_warstwy.setText(_translate("Dialog", "wybierz plik", None))
        self.groupBox_3.setTitle(_translate("Dialog", "3. Importuj dane", None))
        self.groupBox_4.setTitle(_translate("Dialog", "rodzaj importu", None))
        self.radioButton.setText(_translate("Dialog", "dane dla aplikcji mapowych", None))
        self.radioButton_2.setText(_translate("Dialog", "warstwy pochodne", None))
        self.radioButton_3.setText(_translate("Dialog", "wszystko", None))
        self.commandLinkButton_import.setText(_translate("Dialog", "Importuj", None))
        self.groupBox_5.setTitle(_translate("Dialog", "4. Postęp importu", None))
        self.label_2.setText(_translate("Dialog", "TextLabel", None))
        self.label_3.setText(_translate("Dialog", "Wiersze", None))
        self.pushButton.setText(_translate("Dialog", "Zamknij", None))

