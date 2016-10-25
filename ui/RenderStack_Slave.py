# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RenderStack_Slave.ui'
#
# Created: Mon Oct 24 19:21:23 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_RenderStack_MainWindow_slave(object):
    def setupUi(self, RenderStack_MainWindow_slave):
        RenderStack_MainWindow_slave.setObjectName("RenderStack_MainWindow_slave")
        RenderStack_MainWindow_slave.resize(775, 957)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RenderStack_MainWindow_slave.sizePolicy().hasHeightForWidth())
        RenderStack_MainWindow_slave.setSizePolicy(sizePolicy)
        self.RenderStack_centralwidget_slave = QtGui.QWidget(RenderStack_MainWindow_slave)
        self.RenderStack_centralwidget_slave.setObjectName("RenderStack_centralwidget_slave")
        self.verticalLayout = QtGui.QVBoxLayout(self.RenderStack_centralwidget_slave)
        self.verticalLayout.setObjectName("verticalLayout")
        self.renderStack_veticalLayout = QtGui.QVBoxLayout()
        self.renderStack_veticalLayout.setObjectName("renderStack_veticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.machineId_label = QtGui.QLabel(self.RenderStack_centralwidget_slave)
        self.machineId_label.setObjectName("machineId_label")
        self.horizontalLayout.addWidget(self.machineId_label)
        self.machineId_lineEdit = QtGui.QLineEdit(self.RenderStack_centralwidget_slave)
        self.machineId_lineEdit.setObjectName("machineId_lineEdit")
        self.horizontalLayout.addWidget(self.machineId_lineEdit)
        self.active_pushButton = QtGui.QPushButton(self.RenderStack_centralwidget_slave)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.active_pushButton.sizePolicy().hasHeightForWidth())
        self.active_pushButton.setSizePolicy(sizePolicy)
        self.active_pushButton.setMaximumSize(QtCore.QSize(500, 200))
        self.active_pushButton.setObjectName("active_pushButton")
        self.horizontalLayout.addWidget(self.active_pushButton)
        self.renderStack_veticalLayout.addLayout(self.horizontalLayout)
        self.renderStack_tableWidget = QtGui.QTableWidget(self.RenderStack_centralwidget_slave)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.renderStack_tableWidget.sizePolicy().hasHeightForWidth())
        self.renderStack_tableWidget.setSizePolicy(sizePolicy)
        self.renderStack_tableWidget.setObjectName("renderStack_tableWidget")
        self.renderStack_tableWidget.setColumnCount(5)
        self.renderStack_tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.renderStack_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.renderStack_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.renderStack_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.renderStack_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.renderStack_tableWidget.setHorizontalHeaderItem(4, item)
        self.renderStack_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.renderStack_tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.renderStack_tableWidget.horizontalHeader().setStretchLastSection(False)
        self.renderStack_veticalLayout.addWidget(self.renderStack_tableWidget)
        self.verticalLayout.addLayout(self.renderStack_veticalLayout)
        RenderStack_MainWindow_slave.setCentralWidget(self.RenderStack_centralwidget_slave)

        self.retranslateUi(RenderStack_MainWindow_slave)
        QtCore.QMetaObject.connectSlotsByName(RenderStack_MainWindow_slave)

    def retranslateUi(self, RenderStack_MainWindow_slave):
        RenderStack_MainWindow_slave.setWindowTitle(QtGui.QApplication.translate("RenderStack_MainWindow_slave", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.machineId_label.setText(QtGui.QApplication.translate("RenderStack_MainWindow_slave", "Machine Id", None, QtGui.QApplication.UnicodeUTF8))
        self.active_pushButton.setText(QtGui.QApplication.translate("RenderStack_MainWindow_slave", "Active", None, QtGui.QApplication.UnicodeUTF8))
        self.renderStack_tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("RenderStack_MainWindow_slave", "Scene Name", None, QtGui.QApplication.UnicodeUTF8))
        self.renderStack_tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("RenderStack_MainWindow_slave", "Render Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.renderStack_tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("RenderStack_MainWindow_slave", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.renderStack_tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("RenderStack_MainWindow_slave", "Priority", None, QtGui.QApplication.UnicodeUTF8))
        self.renderStack_tableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("RenderStack_MainWindow_slave", "ID", None, QtGui.QApplication.UnicodeUTF8))

