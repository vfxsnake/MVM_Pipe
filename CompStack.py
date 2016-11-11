import datetime as dt
from PySide import QtGui
from PySide import QtCore

from CompStack_mainWindow import Ui_CompStack_MainWindow
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

class CompStack(QtGui.QMainWindow, Ui_CompStack_MainWindow):

    def __init__(self, parent=None):
        super(CompStack, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle('MVM Render Stack')
        self.renderSettings = RenderSettings(self)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.renderSettings)
        self.renderStack_tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.show()

        self.sg = ShotgunUtils()

        self.RenderLayers = []
        self.user = {'type': 'HumanUser', 'id': 97}

        self.update_pushButton.clicked.connect(self.getRenderLayers)
        self.error_pushButton.clicked.connect(self.setRetake)
        self.priority_pushButton.clicked.connect(self.setPriority)
        self.renderSettings.replyNote_pushButton.clicked.connect(self.replyNote)

        self.renderStack_tableWidget.verticalHeader().sectionClicked.connect(self.updateSettings)

        model = self.renderStack_tableWidget.selectionModel()
        model.selectionChanged.connect(self.clearSettings)

        self.renderSettings.setProperties_pushButton.setDisabled(True)
        self.renderSettings.endFrameSpinBox.setDisabled(True)
        self.renderSettings.startFrameSpinBox.setDisabled(True)
        self.renderSettings.forceCheckBox.setDisabled(True)
        self.renderSettings.renderFlagsLineEdit.setDisabled(True)
        self.renderSettings.renderEngineLineEdit.setDisabled(True)
        self.renderSettings.projectPathLineEdit.setDisabled(True)


    def getRenderLayers(self):
        sg = ShotgunUtils()

        rlDic = sg.getPublished()
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
        self.renderStack_tableWidget.setSortingEnabled(False)
        for x, rl in enumerate(self.RenderLayers):

            sceneName = QtGui.QTableWidgetItem(rl['code'])
            renderLayer = QtGui.QTableWidgetItem(rl['sg_renderlayer'])
            status = QtGui.QTableWidgetItem(rl['sg_rlstatus'])
            priority = QtGui.QTableWidgetItem(self.mapPriority(rl['sg_rlpriority']))
            renderMachine = QtGui.QTableWidgetItem(rl['sg_rlmachine'])
            sgId = QtGui.QTableWidgetItem(str(rl['id']))

            updated = rl['updated_at'].isoformat()
            dateSplit = updated.split('T')
            updatedDate = dt.datetime.strptime(dateSplit[0], '%Y-%m-%d')
            today = dt.datetime.today()
            deltaTime = updatedDate - today

            self.renderStack_tableWidget.setItem(x, 0, sceneName)
            self.renderStack_tableWidget.setItem(x, 1, renderLayer)
            self.renderStack_tableWidget.setItem(x, 2, status)
            self.renderStack_tableWidget.setItem(x, 3, priority)
            self.renderStack_tableWidget.setItem(x, 4, renderMachine)
            self.renderStack_tableWidget.setItem(x, 6, sgId)

            if deltaTime.days == 0:
                sceneName.setBackground(QtGui.QColor(0, 255, 0))

            elif deltaTime.days == -1:
                sceneName.setBackground(QtGui.QColor(255,255,0))


        self.renderStack_tableWidget.setSortingEnabled(True)

    def mapPriority(self, priority):

        if priority == '0':
            return 'LOW'

        elif priority == '1':
            return 'NORMAL'

        elif priority == '2':
            return 'HIGH'

        else:
            return 'EXTREME'

    def setRetake(self):

        selection = self.renderStack_tableWidget.selectedItems()
        if selection:

            status = 'RETAKE'

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

    def updateSettings(self, index):

        sceneDic = self.RenderLayers[index]

        self.renderSettings.projectPathLineEdit.setText(sceneDic['sg_rlprojectpath'])
        self.renderSettings.renderEngineLineEdit.setText(sceneDic['sg_rlrenderengine'])
        self.renderSettings.renderFlagsLineEdit.setText(sceneDic['sg_rlrenderflags'])
        self.renderSettings.startFrameSpinBox.setValue(sceneDic['sg_startframe'])
        self.renderSettings.endFrameSpinBox.setValue(sceneDic['sg_endframe'])
        self.renderSettings.forceCheckBox.setChecked(sceneDic['sg_rlforce'])
        self.getRlNote(sceneDic)

    def clearSettings(self):

        self.renderSettings.projectPathLineEdit.setText(None)
        self.renderSettings.renderEngineLineEdit.setText(None)
        self.renderSettings.renderFlagsLineEdit.setText(None)
        self.renderSettings.startFrameSpinBox.setValue(0)
        self.renderSettings.endFrameSpinBox.setValue(0)
        self.renderSettings.forceCheckBox.setChecked(False)
        self.renderSettings.notes_textBrowser.clear()

    def replyNote(self):

        row = self.renderStack_tableWidget.currentRow()

        sceneDict = self.RenderLayers[row]

        noteDialog = noteCreateDialog()
        if noteDialog.noteText:
            self.sg.createCompNote(sceneDict, noteDialog.noteText)
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




