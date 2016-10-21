# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Contour.ui'
#
# Created: Fri Oct 21 10:54:39 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ContourCtrls(object):
    def setupUi(self, ContourCtrls):
        ContourCtrls.setObjectName("ContourCtrls")
        ContourCtrls.resize(247, 167)
        self.contourCtrls_dockWidgetContents = QtGui.QWidget()
        self.contourCtrls_dockWidgetContents.setObjectName("contourCtrls_dockWidgetContents")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.contourCtrls_dockWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.contourWidth_label = QtGui.QLabel(self.contourCtrls_dockWidgetContents)
        self.contourWidth_label.setObjectName("contourWidth_label")
        self.verticalLayout.addWidget(self.contourWidth_label)
        self.contourWidth_spinBox = QtGui.QDoubleSpinBox(self.contourCtrls_dockWidgetContents)
        self.contourWidth_spinBox.setMaximum(100.0)
        self.contourWidth_spinBox.setSingleStep(0.1)
        self.contourWidth_spinBox.setProperty("value", 0.5)
        self.contourWidth_spinBox.setObjectName("contourWidth_spinBox")
        self.verticalLayout.addWidget(self.contourWidth_spinBox)
        self.normalContrast_label = QtGui.QLabel(self.contourCtrls_dockWidgetContents)
        self.normalContrast_label.setObjectName("normalContrast_label")
        self.verticalLayout.addWidget(self.normalContrast_label)
        self.normalContrast_spinBox = QtGui.QDoubleSpinBox(self.contourCtrls_dockWidgetContents)
        self.normalContrast_spinBox.setMaximum(360.0)
        self.normalContrast_spinBox.setSingleStep(0.1)
        self.normalContrast_spinBox.setProperty("value", 4.5)
        self.normalContrast_spinBox.setObjectName("normalContrast_spinBox")
        self.verticalLayout.addWidget(self.normalContrast_spinBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.setSettings_pushButton = QtGui.QPushButton(self.contourCtrls_dockWidgetContents)
        self.setSettings_pushButton.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.setSettings_pushButton.setFont(font)
        self.setSettings_pushButton.setObjectName("setSettings_pushButton")
        self.verticalLayout.addWidget(self.setSettings_pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        ContourCtrls.setWidget(self.contourCtrls_dockWidgetContents)

        self.retranslateUi(ContourCtrls)
        QtCore.QMetaObject.connectSlotsByName(ContourCtrls)

    def retranslateUi(self, ContourCtrls):
        ContourCtrls.setWindowTitle(QtGui.QApplication.translate("ContourCtrls", "Contour Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.contourWidth_label.setText(QtGui.QApplication.translate("ContourCtrls", "Contour Width", None, QtGui.QApplication.UnicodeUTF8))
        self.normalContrast_label.setText(QtGui.QApplication.translate("ContourCtrls", "Normal Contrast", None, QtGui.QApplication.UnicodeUTF8))
        self.setSettings_pushButton.setText(QtGui.QApplication.translate("ContourCtrls", "set Contour Settings", None, QtGui.QApplication.UnicodeUTF8))

