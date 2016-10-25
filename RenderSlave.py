import sys
import os
from PySide import QtGui
from sgConnection import ShotgunUtils
import subprocess


from RenderStack_Slave import Ui_RenderStack_MainWindow_slave

class RenderSlave(QtGui.QMainWindow, Ui_RenderStack_MainWindow_slave):

    def __init__(self, parent=None):
        super(RenderSlave, self).__init__(parent)

        self.renderSlave = ''
        self.renderStackList = []
        self.sg = ShotgunUtils()
        self.setupUi(self)
        self.setWindowTitle("RenderSlave")
        self.show()

        self.active_pushButton.clicked.connect(self.renderQueui)

    def renderQueui(self):
        print 'reder Queui'
        self.renderSlave = self.machineId_lineEdit.text()
        print self.renderSlave
        self.renderStackList = self.sg.getAllRlReady(self.renderSlave)
        print self.renderStackList

        if self.renderStackList:
            self.updateTable()
        else:
            self.wait()

    def updateTable(self):

        tableZise = len(self.renderStackList)

        if not self.renderStack_tableWidget.rowCount() == 0:

            self.renderStack_tableWidget.setRowCount(0)

        self.renderStack_tableWidget.setRowCount(tableZise)

        for x, rl in enumerate(self.renderStackList):
            name = os.path.split(rl['sg_scenename'])[1]

            sceneName = QtGui.QTableWidgetItem(name)
            renderLayer = QtGui.QTableWidgetItem(rl['sg_renderlayer'])
            status = QtGui.QTableWidgetItem(rl['sg_rlstatus'])
            priority = QtGui.QTableWidgetItem(self.mapPriority(rl['sg_rlpriority']))
            sgId = QtGui.QTableWidgetItem(str(rl['id']))

            self.renderStack_tableWidget.setItem(x, 0, sceneName)
            self.renderStack_tableWidget.setItem(x, 1, renderLayer)
            self.renderStack_tableWidget.setItem(x, 2, status)
            self.renderStack_tableWidget.setItem(x, 3, priority)
            self.renderStack_tableWidget.setItem(x, 4, sgId)



    def mapPriority(self, priority):

        if priority == '0':
            return 'LOW'

        elif priority == '1':
            return 'NORMAL'

        elif priority == '2':
            return 'HIGH'

        else:
            return 'EXTREME'

    def wait(self):
        pass

    def batchRender(self):
        pass







def main():
    app = QtGui.QApplication(sys.argv)
    ex = RenderSlave()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()