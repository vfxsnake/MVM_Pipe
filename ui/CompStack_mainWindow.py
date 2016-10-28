# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CompStack_mainWindow.ui'
#
# Created: Fri Oct 28 12:11:24 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CompStack_MainWindow(object):
    def setupUi(self, CompStack_MainWindow):
        CompStack_MainWindow.setObjectName("CompStack_MainWindow")
        CompStack_MainWindow.resize(694, 1144)
        self.CompStack_centralwidget = QtGui.QWidget(CompStack_MainWindow)
        self.CompStack_centralwidget.setObjectName("CompStack_centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.CompStack_centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.CompStack_veticalLayout = QtGui.QVBoxLayout()
        self.CompStack_veticalLayout.setObjectName("CompStack_veticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.update_pushButton = QtGui.QPushButton(self.CompStack_centralwidget)
        self.update_pushButton.setObjectName("update_pushButton")
        self.horizontalLayout.addWidget(self.update_pushButton)
        self.CompStack_veticalLayout.addLayout(self.horizontalLayout)
        self.renderStack_tableWidget = QtGui.QTableWidget(self.CompStack_centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.renderStack_tableWidget.sizePolicy().hasHeightForWidth())
        self.renderStack_tableWidget.setSizePolicy(sizePolicy)
        self.renderStack_tableWidget.setObjectName("renderStack_tableWidget")
        self.renderStack_tableWidget.setColumnCount(4)
        self.renderStack_tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.renderStack_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.renderStack_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.renderStack_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.renderStack_tableWidget.setHorizontalHeaderItem(3, item)
        self.renderStack_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.renderStack_tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.renderStack_tableWidget.horizontalHeader().setStretchLastSection(False)
        self.CompStack_veticalLayout.addWidget(self.renderStack_tableWidget)
        self.action_horizontalLayout = QtGui.QHBoxLayout()
        self.action_horizontalLayout.setObjectName("action_horizontalLayout")
        self.error_pushButton = QtGui.QPushButton(self.CompStack_centralwidget)
        self.error_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.error_pushButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.error_pushButton.setObjectName("error_pushButton")
        self.action_horizontalLayout.addWidget(self.error_pushButton)
        self.priority_pushButton = QtGui.QPushButton(self.CompStack_centralwidget)
        self.priority_pushButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.priority_pushButton.setObjectName("priority_pushButton")
        self.action_horizontalLayout.addWidget(self.priority_pushButton)
        self.CompStack_veticalLayout.addLayout(self.action_horizontalLayout)
        self.verticalLayout.addLayout(self.CompStack_veticalLayout)
        CompStack_MainWindow.setCentralWidget(self.CompStack_centralwidget)

        self.retranslateUi(CompStack_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(CompStack_MainWindow)

    def retranslateUi(self, CompStack_MainWindow):
        CompStack_MainWindow.setWindowTitle(QtGui.QApplication.translate("CompStack_MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.update_pushButton.setText(QtGui.QApplication.translate("CompStack_MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.renderStack_tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("CompStack_MainWindow", "Scene Name", None, QtGui.QApplication.UnicodeUTF8))
        self.renderStack_tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("CompStack_MainWindow", "Render Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.renderStack_tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("CompStack_MainWindow", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.renderStack_tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("CompStack_MainWindow", "Priority", None, QtGui.QApplication.UnicodeUTF8))
        self.error_pushButton.setText(QtGui.QApplication.translate("CompStack_MainWindow", "Report Error", None, QtGui.QApplication.UnicodeUTF8))
        self.priority_pushButton.setText(QtGui.QApplication.translate("CompStack_MainWindow", "Set Priority", None, QtGui.QApplication.UnicodeUTF8))

