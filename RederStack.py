import shutil
import os


from PySide import QtGui
from PySide import QtCore

from RenderStack_mainWindow import Ui_RenderStack_MainWindow
from RenderSettings import Ui_renderSettings_dockWidget
from notesDialog import Ui_Dialog

from sgConnection import ShotgunUtils


class noteCreateDialog(QtGui.QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super(noteCreateDialog, self).__init__(parent)

        self.setupUi(self)
        self.noteText = None
        self.exec_()

    def accept(self):
        self.noteText = self.NoteTextEdit.toPlainText()
        self.close()


class RenderSettings(QtGui.QDockWidget, Ui_renderSettings_dockWidget):

    def __init__(self, parent=None):
        super(RenderSettings, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle('Render Settings')
        self.setFeatures(QtGui.QDockWidget.DockWidgetFloatable | QtGui.QDockWidget.DockWidgetMovable)
        self.setAllowedAreas(QtCore.Qt.RightDockWidgetArea)
        self.endFrameSpinBox.setMaximum(5000)
        self.notes_textBrowser.setReadOnly(True)
        self.notes_textBrowser.setTextBackgroundColor('white')
        self.show()

class RenderStack(QtGui.QMainWindow, Ui_RenderStack_MainWindow):

    def __init__(self, parent=None):
        super(RenderStack, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle('MVM Render Stack')
        self.renderSettings = RenderSettings(self)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.renderSettings)
        self.machineId_lineEdit.setText('Render00')
        self.renderStack_tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.show()

        self.progressBar = QtGui.QProgressBar(self)
        self.progressBar.move(100, 100)
        self.progressBar.setFixedSize(500, 50)

        self.sg = ShotgunUtils()

        self.RenderLayers = []
        self.user = {'type': 'HumanUser', 'id': 96}

        self.update_pushButton.clicked.connect(self.getRenderLayers)
        self.ready2Start_pushButton.clicked.connect(self.setStart)
        self.pushButton.clicked.connect(self.setPriority)
        self.assingMachine_pushButton.clicked.connect(self.setRenderMachine)
        self.promoteComp_pushButton.clicked.connect(self.prometeComp)
        self.renderSettings.replyNote_pushButton.clicked.connect(self.replyNote)


        self.renderStack_tableWidget.verticalHeader().sectionClicked.connect(self.updateSettings)
        self.renderSettings.setProperties_pushButton.clicked.connect(self.setSettings)

        model = self.renderStack_tableWidget.selectionModel()
        model.selectionChanged.connect(self.clearSettings)

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

    def setStart(self):

        selection = self.renderStack_tableWidget.selectedItems()
        if selection:

            rdyButton = QtGui.QPushButton('ready to start')

            ipButton = QtGui.QPushButton('in progress')

            doneButton = QtGui.QPushButton('Done')

            errorButton = QtGui.QPushButton('ERROR')

            retakeButton = QtGui.QPushButton('RETAKE')

            cancelButton = QtGui.QPushButton('cancel')

            messageBox = QtGui.QMessageBox()
            messageBox.addButton(rdyButton, QtGui.QMessageBox.AcceptRole)
            messageBox.addButton(ipButton, QtGui.QMessageBox.AcceptRole)
            messageBox.addButton(doneButton, QtGui.QMessageBox.AcceptRole)
            messageBox.addButton(errorButton, QtGui.QMessageBox.AcceptRole)
            messageBox.addButton(retakeButton, QtGui.QMessageBox.AcceptRole)
            messageBox.addButton(cancelButton, QtGui.QMessageBox.AcceptRole)

            messageBox.setText('Update Priority:')

            clicked = messageBox.exec_()

            status = None

            if clicked == 0:
                status = 'ready to start'

            elif clicked == 1:
                status = 'in progress'

            elif clicked == 2:
                status = 'Done'

            elif clicked == 3:
                status = 'ERROR'

            elif clicked == 4:
                status = 'RETAKE'

            else:
                return None
            if status:
                for cell in selection:
                    row = cell.row()
                    sceneDict = self.RenderLayers[row]
                    sceneDict['sg_rlstatus'] = status
                    self.sg.updateSgRL(sceneDict)

        self.updateTable()

    def setPriority(self):
        selection = self.renderStack_tableWidget.selectedItems()
        if selection:

            lowButton = QtGui.QPushButton('LOW')

            normalButton = QtGui.QPushButton('NORMAL')

            highButton = QtGui.QPushButton('HIGH')

            extremeButton = QtGui.QPushButton('EXTREME')

            cancelButton = QtGui.QPushButton('cancel')

            messageBox = QtGui.QMessageBox()
            messageBox.addButton(lowButton, QtGui.QMessageBox.AcceptRole)
            messageBox.addButton(normalButton, QtGui.QMessageBox.AcceptRole)
            messageBox.addButton(highButton, QtGui.QMessageBox.AcceptRole)
            messageBox.addButton(extremeButton, QtGui.QMessageBox.AcceptRole)
            messageBox.addButton(cancelButton, QtGui.QMessageBox.AcceptRole)

            messageBox.setText('Update Priority:')

            clicked = messageBox.exec_()

            status = None

            if clicked == 0:
                status = '0'

            elif clicked == 1:
                status = '1'

            elif clicked == 2:
                status = '2'

            elif clicked == 3:
                status = '3'

            else:
                return None

            if status:
                for cell in selection:
                    row = cell.row()
                    sceneDict = self.RenderLayers[row]
                    sceneDict['sg_rlpriority'] = status
                    self.sg.updateSgRL(sceneDict)
            else:
                pass

            self.updateTable()

    def setRenderMachine(self):

        selection = self.renderStack_tableWidget.selectedItems()
        if selection:

            r1Button = QtGui.QPushButton('Render00')

            r2Button = QtGui.QPushButton('Render01')

            r3Button = QtGui.QPushButton('Render02')

            r4Button = QtGui.QPushButton('Render03')

            r5Button = QtGui.QPushButton('Render04')

            cancelButton = QtGui.QPushButton('cancel')

            messageBox = QtGui.QMessageBox()
            messageBox.addButton(r1Button, QtGui.QMessageBox.AcceptRole)
            messageBox.addButton(r2Button, QtGui.QMessageBox.AcceptRole)
            messageBox.addButton(r3Button, QtGui.QMessageBox.AcceptRole)
            messageBox.addButton(r4Button, QtGui.QMessageBox.AcceptRole)
            messageBox.addButton(r5Button, QtGui.QMessageBox.AcceptRole)
            messageBox.addButton(cancelButton, QtGui.QMessageBox.AcceptRole)

            messageBox.setText('Update Priority:')

            clicked = messageBox.exec_()

            status = None

            if clicked == 0:
                status = 'Render00'

            elif clicked == 1:
                status = 'Render01'

            elif clicked == 2:
                status = 'Render02'

            elif clicked == 3:
                status = 'Render03'

            elif clicked == 4:
                status = 'Render04'

            else:
                return None

            if status:
                for cell in selection:
                    row = cell.row()
                    sceneDict = self.RenderLayers[row]
                    sceneDict['sg_rlmachine'] = status
                    self.sg.updateSgRL(sceneDict)
            else:
                pass

        self.updateTable()

    def updateSettings(self, index):

        sceneDic = self.RenderLayers[index]

        self.renderSettings.projectPathLineEdit.setText(sceneDic['sg_rlprojectpath'])
        self.renderSettings.renderEngineLineEdit.setText(sceneDic['sg_rlrenderengine'])
        self.renderSettings.renderFlagsLineEdit.setText(sceneDic['sg_rlrenderflags'])
        self.renderSettings.startFrameSpinBox.setValue(sceneDic['sg_startframe'])
        self.renderSettings.endFrameSpinBox.setValue(sceneDic['sg_endframe'])
        self.renderSettings.forceCheckBox.setChecked(sceneDic['sg_rlforce'])
        self.getRlNote(sceneDic)

    def setSettings(self):
        row = self.renderStack_tableWidget.currentRow()

        sceneDict = self.RenderLayers[row]

        sceneDict['sg_rlprojectpath'] = self.renderSettings.projectPathLineEdit.text()
        sceneDict['sg_rlrenderengine'] = self.renderSettings.renderEngineLineEdit.text()
        sceneDict['sg_rlrenderflags'] = self.renderSettings.renderFlagsLineEdit.text()
        sceneDict['sg_startframe'] = self.renderSettings.startFrameSpinBox.value()
        sceneDict['sg_endframe'] = self.renderSettings.endFrameSpinBox.value()
        sceneDict['sg_rlforce'] = self.renderSettings.forceCheckBox.isChecked()

        self.sg.updateSgRL(sceneDict)


    def clearSettings(self):

        self.renderSettings.projectPathLineEdit.setText(None)
        self.renderSettings.renderEngineLineEdit.setText(None)
        self.renderSettings.renderFlagsLineEdit.setText(None)
        self.renderSettings.startFrameSpinBox.setValue(0)
        self.renderSettings.endFrameSpinBox.setValue(0)
        self.renderSettings.forceCheckBox.setChecked(False)
        self.renderSettings.notes_textBrowser.clear()

    def prometeComp(self):

        '''  First get access to the network share with "NET USE" - without Drive letter, like:

            winCMD = 'NET USE ' + networkPath + ' /User:' + user + ' ' + password
            subprocess.Popen(winCMD, stdout=subprocess.PIPE, shell=True)
            As in here (but without specifying Drive letter): What is the best way to map windows drives using Python?

            Then copy the file/directory with shutil.copy, like:

            import shutil
            shutil.copy2(networkPath + 'sourceDir/sourceFile', 'destDir/destFile') '''

        selection = self.renderStack_tableWidget.selectedItems()
        if selection:
            for cell in selection:
                row = cell.row()
                sceneDict = self.RenderLayers[row]

                localPath = '{0}/{1}/{2}'.format(sceneDict['sg_rlprojectpath'], 'images', sceneDict['sg_renderlayer'])

                targetPath = self.getCompPath(sceneDict['sg_rlprojectpath'], sceneDict['sg_renderlayer'])
                try:
                    shutil.os.mkdir(targetPath)
                except:
                    pass

                files = None
                try:
                    files = shutil.os.listdir(localPath)
                except:
                    pass
                self.progressBar.show()

                if files:
                    size = len(files)
                    for x, image in enumerate(files):
                        shutil.copy2(localPath +'/'+image, targetPath)
                        self.progressBar.setValue((float(x + 1)/float(size)) * 100)

                    self.progressBar.close()

                    sceneDict['sg_rlstatus'] = 'Published'
                    self.sg.updateSgRL(sceneDict)

                else:
                    print 'No files found'
                    self.progressBar.close()


    def getCompPath(self, sourcePath, rlName):

        target = shutil.os.path.split(sourcePath)

        folderList = ['\\\Huevoduro','MVM_08_COMPOSICION']

        if target:
            splitString = target[1].split('_')


            if 'R' in splitString[1]:
                rollo = splitString[1].replace('R', '')
                folderList.append('MVM_ACTO_{0}'.format(rollo))
                folderList.append('MVM_{0}_SEC_{1}'.format(rollo, splitString[2]))
                folderList.append('MVM_{0}_{1}_ES_{2}'.format(rollo, splitString[2], splitString[3]))
                folderList.append('03_FRAMES (1)')
                folderList.append(rlName)


        destinationPath = '/'.join(folderList)
        return destinationPath

    def replyNote(self):

        row = self.renderStack_tableWidget.currentRow()

        sceneDict = self.RenderLayers[row]

        noteDialog = noteCreateDialog()
        if noteDialog.noteText:
            self.sg.create3DNotes(sceneDict, noteDialog.noteText)
            self.getRlNote(sceneDict)
        else:
            print 'no notes Created'

    def getRlNote(self, rlDic):
        notes = self.sg.getNotes(rlDic)
        self.renderSettings.notes_textBrowser.clear()
        if notes:
            for note in notes:
                if not note['user']['id'] == self.user['id']:
                    self.renderSettings.notes_textBrowser.setTextColor('red')
                    self.renderSettings.notes_textBrowser.append(note['user']['name'])
                    self.renderSettings.notes_textBrowser.append(note['created_at'].isoformat())
                    self.renderSettings.notes_textBrowser.setTextColor('black')
                    self.renderSettings.notes_textBrowser.append(note['content'])
                    self.renderSettings.notes_textBrowser.append('')
                    self.renderSettings.notes_textBrowser.append('')

                else:
                    self.renderSettings.notes_textBrowser.setTextColor('blue')
                    self.renderSettings.notes_textBrowser.append(note['user']['name'])
                    self.renderSettings.notes_textBrowser.append(note['created_at'].isoformat())
                    self.renderSettings.notes_textBrowser.setTextColor('black')
                    self.renderSettings.notes_textBrowser.append(note['content'])
                    self.renderSettings.notes_textBrowser.append('')
                    self.renderSettings.notes_textBrowser.append('')

        else:
            text = 'no notes'
            self.renderSettings.notes_textBrowser.append(text)




