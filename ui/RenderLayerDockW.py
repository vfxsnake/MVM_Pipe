# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RenderLayerDockW.ui'
#
# Created: Mon Oct 24 13:48:05 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_renderLayerDockWidget(object):
    def setupUi(self, renderLayerDockWidget):
        renderLayerDockWidget.setObjectName("renderLayerDockWidget")
        renderLayerDockWidget.resize(677, 976)
        self.renderLayerWidget = QtGui.QWidget()
        self.renderLayerWidget.setObjectName("renderLayerWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.renderLayerWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.renderLayers_verticalLayout = QtGui.QVBoxLayout()
        self.renderLayers_verticalLayout.setObjectName("renderLayers_verticalLayout")
        self.utilities_label = QtGui.QLabel(self.renderLayerWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.utilities_label.setFont(font)
        self.utilities_label.setAlignment(QtCore.Qt.AlignCenter)
        self.utilities_label.setObjectName("utilities_label")
        self.renderLayers_verticalLayout.addWidget(self.utilities_label)
        self.utilities_horizontalLayout = QtGui.QHBoxLayout()
        self.utilities_horizontalLayout.setObjectName("utilities_horizontalLayout")
        self.renderSettings_pushButton = QtGui.QPushButton(self.renderLayerWidget)
        self.renderSettings_pushButton.setMaximumSize(QtCore.QSize(16777215, 200))
        self.renderSettings_pushButton.setObjectName("renderSettings_pushButton")
        self.utilities_horizontalLayout.addWidget(self.renderSettings_pushButton)
        self.texture_pushButton = QtGui.QPushButton(self.renderLayerWidget)
        self.texture_pushButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.texture_pushButton.setObjectName("texture_pushButton")
        self.utilities_horizontalLayout.addWidget(self.texture_pushButton)
        self.contourSettings_pushButton = QtGui.QPushButton(self.renderLayerWidget)
        self.contourSettings_pushButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.contourSettings_pushButton.setObjectName("contourSettings_pushButton")
        self.utilities_horizontalLayout.addWidget(self.contourSettings_pushButton)
        self.renderLayers_verticalLayout.addLayout(self.utilities_horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.renderLayers_verticalLayout.addItem(spacerItem)
        self.renderLayer_Label = QtGui.QLabel(self.renderLayerWidget)
        self.renderLayer_Label.setMaximumSize(QtCore.QSize(1000, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.renderLayer_Label.setFont(font)
        self.renderLayer_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.renderLayer_Label.setObjectName("renderLayer_Label")
        self.renderLayers_verticalLayout.addWidget(self.renderLayer_Label)
        self.colorLightRl_pushButton = QtGui.QPushButton(self.renderLayerWidget)
        self.colorLightRl_pushButton.setMaximumSize(QtCore.QSize(1000, 50))
        self.colorLightRl_pushButton.setObjectName("colorLightRl_pushButton")
        self.renderLayers_verticalLayout.addWidget(self.colorLightRl_pushButton)
        self.glowRl_pushButton = QtGui.QPushButton(self.renderLayerWidget)
        self.glowRl_pushButton.setMaximumSize(QtCore.QSize(1000, 50))
        self.glowRl_pushButton.setObjectName("glowRl_pushButton")
        self.renderLayers_verticalLayout.addWidget(self.glowRl_pushButton)
        self.trailRl_pushButton = QtGui.QPushButton(self.renderLayerWidget)
        self.trailRl_pushButton.setMaximumSize(QtCore.QSize(1000, 50))
        self.trailRl_pushButton.setObjectName("trailRl_pushButton")
        self.renderLayers_verticalLayout.addWidget(self.trailRl_pushButton)
        self.shadow_pushButton = QtGui.QPushButton(self.renderLayerWidget)
        self.shadow_pushButton.setMaximumSize(QtCore.QSize(1000, 50))
        self.shadow_pushButton.setObjectName("shadow_pushButton")
        self.renderLayers_verticalLayout.addWidget(self.shadow_pushButton)
        self.matteRl_pushButton = QtGui.QPushButton(self.renderLayerWidget)
        self.matteRl_pushButton.setMaximumSize(QtCore.QSize(1000, 50))
        self.matteRl_pushButton.setObjectName("matteRl_pushButton")
        self.renderLayers_verticalLayout.addWidget(self.matteRl_pushButton)
        self.inOutLine_pushButton = QtGui.QPushButton(self.renderLayerWidget)
        self.inOutLine_pushButton.setMaximumSize(QtCore.QSize(1000, 50))
        self.inOutLine_pushButton.setObjectName("inOutLine_pushButton")
        self.renderLayers_verticalLayout.addWidget(self.inOutLine_pushButton)
        self.includeRl_pushButton = QtGui.QPushButton(self.renderLayerWidget)
        self.includeRl_pushButton.setMaximumSize(QtCore.QSize(1000, 50))
        self.includeRl_pushButton.setObjectName("includeRl_pushButton")
        self.renderLayers_verticalLayout.addWidget(self.includeRl_pushButton)
        self.zDepth_pushButton = QtGui.QPushButton(self.renderLayerWidget)
        self.zDepth_pushButton.setMaximumSize(QtCore.QSize(1000, 50))
        self.zDepth_pushButton.setObjectName("zDepth_pushButton")
        self.renderLayers_verticalLayout.addWidget(self.zDepth_pushButton)
        spacerItem1 = QtGui.QSpacerItem(100, 300, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.renderLayers_verticalLayout.addItem(spacerItem1)
        self.submitStack_pushButton = QtGui.QPushButton(self.renderLayerWidget)
        self.submitStack_pushButton.setMaximumSize(QtCore.QSize(1000, 80))
        self.submitStack_pushButton.setObjectName("submitStack_pushButton")
        self.renderLayers_verticalLayout.addWidget(self.submitStack_pushButton)
        self.openStack_pushButton = QtGui.QPushButton(self.renderLayerWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openStack_pushButton.sizePolicy().hasHeightForWidth())
        self.openStack_pushButton.setSizePolicy(sizePolicy)
        self.openStack_pushButton.setMaximumSize(QtCore.QSize(16777215, 40))
        self.openStack_pushButton.setObjectName("openStack_pushButton")
        self.renderLayers_verticalLayout.addWidget(self.openStack_pushButton)
        self.verticalLayout_2.addLayout(self.renderLayers_verticalLayout)
        renderLayerDockWidget.setWidget(self.renderLayerWidget)

        self.retranslateUi(renderLayerDockWidget)
        QtCore.QMetaObject.connectSlotsByName(renderLayerDockWidget)

    def retranslateUi(self, renderLayerDockWidget):
        renderLayerDockWidget.setWindowTitle(QtGui.QApplication.translate("renderLayerDockWidget", "DockWidget", None, QtGui.QApplication.UnicodeUTF8))
        self.utilities_label.setText(QtGui.QApplication.translate("renderLayerDockWidget", "Utilities", None, QtGui.QApplication.UnicodeUTF8))
        self.renderSettings_pushButton.setText(QtGui.QApplication.translate("renderLayerDockWidget", "Gobal Render Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.texture_pushButton.setText(QtGui.QApplication.translate("renderLayerDockWidget", "NaveGlobo Texture", None, QtGui.QApplication.UnicodeUTF8))
        self.contourSettings_pushButton.setText(QtGui.QApplication.translate("renderLayerDockWidget", "Contour Settings Window", None, QtGui.QApplication.UnicodeUTF8))
        self.renderLayer_Label.setText(QtGui.QApplication.translate("renderLayerDockWidget", "RenderLayers", None, QtGui.QApplication.UnicodeUTF8))
        self.colorLightRl_pushButton.setText(QtGui.QApplication.translate("renderLayerDockWidget", "Color-Light RLs", None, QtGui.QApplication.UnicodeUTF8))
        self.glowRl_pushButton.setText(QtGui.QApplication.translate("renderLayerDockWidget", "Glow RL", None, QtGui.QApplication.UnicodeUTF8))
        self.trailRl_pushButton.setText(QtGui.QApplication.translate("renderLayerDockWidget", "Trail RL", None, QtGui.QApplication.UnicodeUTF8))
        self.shadow_pushButton.setText(QtGui.QApplication.translate("renderLayerDockWidget", "Shadow RL", None, QtGui.QApplication.UnicodeUTF8))
        self.matteRl_pushButton.setText(QtGui.QApplication.translate("renderLayerDockWidget", "Matte RL", None, QtGui.QApplication.UnicodeUTF8))
        self.inOutLine_pushButton.setText(QtGui.QApplication.translate("renderLayerDockWidget", "In/Out_line RL", None, QtGui.QApplication.UnicodeUTF8))
        self.includeRl_pushButton.setText(QtGui.QApplication.translate("renderLayerDockWidget", "Include RL", None, QtGui.QApplication.UnicodeUTF8))
        self.zDepth_pushButton.setText(QtGui.QApplication.translate("renderLayerDockWidget", "ZDepth RL", None, QtGui.QApplication.UnicodeUTF8))
        self.submitStack_pushButton.setText(QtGui.QApplication.translate("renderLayerDockWidget", "Submit to Stack", None, QtGui.QApplication.UnicodeUTF8))
        self.openStack_pushButton.setText(QtGui.QApplication.translate("renderLayerDockWidget", "Open Render Stack", None, QtGui.QApplication.UnicodeUTF8))

