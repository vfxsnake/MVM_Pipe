# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RenderStack.ui'
#
# Created: Tue Oct 18 16:37:13 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_renderStack_DockWidget(object):
    def setupUi(self, renderStack_DockWidget):
        renderStack_DockWidget.setObjectName("renderStack_DockWidget")
        renderStack_DockWidget.resize(1030, 896)
        self.renderStack_Widget = QtGui.QWidget()
        self.renderStack_Widget.setObjectName("renderStack_Widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.renderStack_Widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.renderStack_veticalLayout = QtGui.QVBoxLayout()
        self.renderStack_veticalLayout.setObjectName("renderStack_veticalLayout")
        self.renderStack_tableWidget = QtGui.QTableWidget(self.renderStack_Widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.renderStack_tableWidget.sizePolicy().hasHeightForWidth())
        self.renderStack_tableWidget.setSizePolicy(sizePolicy)
        self.renderStack_tableWidget.setObjectName("renderStack_tableWidget")
        self.renderStack_tableWidget.setColumnCount(7)
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
        item = QtGui.QTableWidgetItem()
        self.renderStack_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.renderStack_tableWidget.setHorizontalHeaderItem(6, item)
        self.renderStack_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.renderStack_tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.renderStack_tableWidget.horizontalHeader().setStretchLastSection(False)
        self.renderStack_veticalLayout.addWidget(self.renderStack_tableWidget)
        self.action_horizontalLayout = QtGui.QHBoxLayout()
        self.action_horizontalLayout.setObjectName("action_horizontalLayout")
        self.ready2Start_pushButton = QtGui.QPushButton(self.renderStack_Widget)
        self.ready2Start_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.ready2Start_pushButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.ready2Start_pushButton.setObjectName("ready2Start_pushButton")
        self.action_horizontalLayout.addWidget(self.ready2Start_pushButton)
        self.pushButton = QtGui.QPushButton(self.renderStack_Widget)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton.setObjectName("pushButton")
        self.action_horizontalLayout.addWidget(self.pushButton)
        self.assingMachine_pushButton = QtGui.QPushButton(self.renderStack_Widget)
        self.assingMachine_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.assingMachine_pushButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.assingMachine_pushButton.setObjectName("assingMachine_pushButton")
        self.action_horizontalLayout.addWidget(self.assingMachine_pushButton)
        spacerItem = QtGui.QSpacerItem(40, 50, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.action_horizontalLayout.addItem(spacerItem)
        self.promoteComp_pushButton = QtGui.QPushButton(self.renderStack_Widget)
        self.promoteComp_pushButton.setMinimumSize(QtCore.QSize(0, 80))
        self.promoteComp_pushButton.setMaximumSize(QtCore.QSize(16777215, 60))
        self.promoteComp_pushButton.setObjectName("promoteComp_pushButton")
        self.action_horizontalLayout.addWidget(self.promoteComp_pushButton)
        self.renderStack_veticalLayout.addLayout(self.action_horizontalLayout)
        self.horizontalLayout.addLayout(self.renderStack_veticalLayout)
        renderStack_DockWidget.setWidget(self.renderStack_Widget)

        self.retranslateUi(renderStack_DockWidget)
        QtCore.QMetaObject.connectSlotsByName(renderStack_DockWidget)

    def retranslateUi(self, renderStack_DockWidget):
        renderStack_DockWidget.setWindowTitle(QtGui.QApplication.translate("renderStack_DockWidget", "DockWidget", None, QtGui.QApplication.UnicodeUTF8))
        self.renderStack_tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("renderStack_DockWidget", "Scene Name", None, QtGui.QApplication.UnicodeUTF8))
        self.renderStack_tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("renderStack_DockWidget", "Render Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.renderStack_tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("renderStack_DockWidget", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.renderStack_tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("renderStack_DockWidget", "Priority", None, QtGui.QApplication.UnicodeUTF8))
        self.renderStack_tableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("renderStack_DockWidget", "Render Machine", None, QtGui.QApplication.UnicodeUTF8))
        self.renderStack_tableWidget.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("renderStack_DockWidget", "Machine Status", None, QtGui.QApplication.UnicodeUTF8))
        self.renderStack_tableWidget.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("renderStack_DockWidget", "ID", None, QtGui.QApplication.UnicodeUTF8))
        self.ready2Start_pushButton.setText(QtGui.QApplication.translate("renderStack_DockWidget", "Set Ready to Start", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("renderStack_DockWidget", "Set Priority", None, QtGui.QApplication.UnicodeUTF8))
        self.assingMachine_pushButton.setText(QtGui.QApplication.translate("renderStack_DockWidget", "Assign Render Machine", None, QtGui.QApplication.UnicodeUTF8))
        self.promoteComp_pushButton.setText(QtGui.QApplication.translate("renderStack_DockWidget", "Promote to Comp", None, QtGui.QApplication.UnicodeUTF8))

