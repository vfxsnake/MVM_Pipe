import sys
sys.path.append('D:\Data\plug-ins\MVM_Pipe\python-api')
sys.path.append('D:\Data\plug-ins\MVM_Pipe\ui')
import os
from PySide import QtGui
from PySide import QtCore
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

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.isSingleShot()

        self.show()

        self.active_pushButton.clicked.connect(self.batchRender)
        self.timer.timeout.connect(self.batchRender)


    def updateTable(self):

        self.renderSlave = self.machineId_lineEdit.text()

        self.renderStackList = self.sg.getAllRlReady(self.renderSlave)

        if self.renderStackList:

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


        else:
            self.renderStack_tableWidget.setRowCount(0)



    def batchRender(self):
        self.updateTable()

        while self.renderStackList:
            print 'batchRendering'
            scene = self.renderStackList[0]

            scene['sg_rlstatus'] = 'in progress'
            self.sg.updateSgRL(scene)

            process = []

            command = 'Render.exe'
            process.append(command)

            process.append('-proj')
            projectPath = scene['sg_rlprojectpath']
            process.append(projectPath)

            process.append('-r')
            renderEngine = scene['sg_rlrenderengine']
            process.append(renderEngine)

            renderFlags = scene['sg_rlrenderflags']
            self.splitRenderFlags(renderFlags, process)

            process.append('-s')
            startFrame = str(scene['sg_startframe'])
            process.append(startFrame)

            process.append('-e')
            endFrame = str(scene['sg_endframe'])
            process.append(endFrame)

            sceneName = scene['sg_scenename']

            process.append(sceneName)

            if not scene['sg_rlforce']:
                print process
                subprocess.call(process)

            else:

                for frame in range(scene['sg_startframe'], scene['sg_endframe'] + 1):
                    process[10] = str(frame)
                    process[12] = str(frame)

                    subprocess.call(process)

            scene['sg_rlstatus'] = 'Done'

            self.sg.updateSgRL(scene)
            self.updateTable()

        self.wait()

    def splitRenderFlags(self, renderFlags, processList):
        flags = renderFlags.split(' ')
        for flag in flags:
            processList.append(flag)


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
        print 'starting timer'
        self.timer.start()



def main():
    app = QtGui.QApplication(sys.argv)
    ex = RenderSlave()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
