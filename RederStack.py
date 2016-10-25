from PySide import QtGui
from PySide import QtCore
from sgConnection import ShotgunUtils

from RenderStack_mainWindow import Ui_RenderStack_MainWindow
from RenderSettings import Ui_renderSettings_dockWidget


class RenderSettings(QtGui.QDockWidget, Ui_renderSettings_dockWidget):

    def __init__(self, parent=None):
        super(RenderSettings, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle('Render Settings')
        self.setFeatures(QtGui.QDockWidget.DockWidgetFloatable | QtGui.QDockWidget.DockWidgetMovable)
        self.setAllowedAreas(QtCore.Qt.RightDockWidgetArea)
        self.show()

class RenderStack(QtGui.QMainWindow, Ui_RenderStack_MainWindow):

    def __init__(self, parent=None):
        super(RenderStack, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle('MVM Render Stack')
        self.renderSettigns = RenderSettings(self)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.renderSettigns)
        self.machineId_lineEdit.setText('Render01')
        self.renderStack_tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.show()

        self.RenderLayers = []

        self.update_pushButton.clicked.connect(self.getRenderLayers)


    def getRenderLayers(self):
        sg = ShotgunUtils()

        rlDic = sg.getAllRenderLayer(self.machineId_lineEdit.text())
        if rlDic:

            self.RenderLayers = rlDic
            self.updateTable()
        else:

            self.renderStack_tableWidget.setRowCount(0)

    def updateTable(self):

        tableZise = len(self.RenderLayers)

        if not self.renderStack_tableWidget.rowCount() == 0:

            self.renderStack_tableWidget.setRowCount(0)

        self.renderStack_tableWidget.setRowCount(tableZise)

        for x, rl in enumerate(self.RenderLayers):

            sceneName = QtGui.QTableWidgetItem(rl['code'])
            renderLayer = QtGui.QTableWidgetItem(rl['sg_renderlayer'])
            status = QtGui.QTableWidgetItem(rl['sg_rlstatus'])
            priority = QtGui.QTableWidgetItem(self.mapPriority(rl['sg_rlpriority']))
            renderMachine = QtGui.QTableWidgetItem(rl['sg_rlmachine'])
            sgId = QtGui.QTableWidgetItem(str(rl['id']))

            self.renderStack_tableWidget.setItem(x, 0, sceneName)
            self.renderStack_tableWidget.setItem(x, 1, renderLayer)
            self.renderStack_tableWidget.setItem(x, 2, status)
            self.renderStack_tableWidget.setItem(x, 3, priority)
            self.renderStack_tableWidget.setItem(x, 4, renderMachine)
            self.renderStack_tableWidget.setItem(x, 6, sgId)



    def mapPriority(self, priority):

        if priority == '0':
            return 'LOW'

        elif priority == '1':
            return 'NORMAL'

        elif priority == '2':
            return 'HIGH'

        else:
            return 'EXTREME'



