# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CastShadow.ui'
#
# Created: Thu Oct 20 11:56:14 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CastShadowsDockWidget(object):
    def setupUi(self, CastShadowsDockWidget):
        CastShadowsDockWidget.setObjectName("CastShadowsDockWidget")
        CastShadowsDockWidget.resize(362, 319)
        self.castShadows_DockWidgetContents = QtGui.QWidget()
        self.castShadows_DockWidgetContents.setObjectName("castShadows_DockWidgetContents")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.castShadows_DockWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.castShadows_verticalLayout = QtGui.QVBoxLayout()
        self.castShadows_verticalLayout.setObjectName("castShadows_verticalLayout")
        self.castSahdowLabel = QtGui.QLabel(self.castShadows_DockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.castSahdowLabel.setFont(font)
        self.castSahdowLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.castSahdowLabel.setObjectName("castSahdowLabel")
        self.castShadows_verticalLayout.addWidget(self.castSahdowLabel)
        self.setCastShadow_pushButton = QtGui.QPushButton(self.castShadows_DockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setCastShadow_pushButton.setFont(font)
        self.setCastShadow_pushButton.setObjectName("setCastShadow_pushButton")
        self.castShadows_verticalLayout.addWidget(self.setCastShadow_pushButton)
        self.receiveSahdowLabel = QtGui.QLabel(self.castShadows_DockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.receiveSahdowLabel.setFont(font)
        self.receiveSahdowLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.receiveSahdowLabel.setObjectName("receiveSahdowLabel")
        self.castShadows_verticalLayout.addWidget(self.receiveSahdowLabel)
        self.setReceiveShadow_pushButton = QtGui.QPushButton(self.castShadows_DockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setReceiveShadow_pushButton.setFont(font)
        self.setReceiveShadow_pushButton.setObjectName("setReceiveShadow_pushButton")
        self.castShadows_verticalLayout.addWidget(self.setReceiveShadow_pushButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.castShadows_verticalLayout.addItem(spacerItem)
        self.close_pushButton = QtGui.QPushButton(self.castShadows_DockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.close_pushButton.setFont(font)
        self.close_pushButton.setObjectName("close_pushButton")
        self.castShadows_verticalLayout.addWidget(self.close_pushButton)
        self.verticalLayout_2.addLayout(self.castShadows_verticalLayout)
        CastShadowsDockWidget.setWidget(self.castShadows_DockWidgetContents)

        self.retranslateUi(CastShadowsDockWidget)
        QtCore.QMetaObject.connectSlotsByName(CastShadowsDockWidget)

    def retranslateUi(self, CastShadowsDockWidget):
        CastShadowsDockWidget.setWindowTitle(QtGui.QApplication.translate("CastShadowsDockWidget", "Cast Shadows Attrs", None, QtGui.QApplication.UnicodeUTF8))
        self.castSahdowLabel.setText(QtGui.QApplication.translate("CastShadowsDockWidget", "Select Cast Shadow Objects", None, QtGui.QApplication.UnicodeUTF8))
        self.setCastShadow_pushButton.setText(QtGui.QApplication.translate("CastShadowsDockWidget", "Set Cast Shadow Attrs", None, QtGui.QApplication.UnicodeUTF8))
        self.receiveSahdowLabel.setText(QtGui.QApplication.translate("CastShadowsDockWidget", "Select Receive Shadow Objects", None, QtGui.QApplication.UnicodeUTF8))
        self.setReceiveShadow_pushButton.setText(QtGui.QApplication.translate("CastShadowsDockWidget", "Set Receive Shadow Attrs", None, QtGui.QApplication.UnicodeUTF8))
        self.close_pushButton.setText(QtGui.QApplication.translate("CastShadowsDockWidget", "Close", None, QtGui.QApplication.UnicodeUTF8))

