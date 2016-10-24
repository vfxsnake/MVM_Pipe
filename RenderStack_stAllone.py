import sys

from PySide import QtGui
from PySide import QtCore

from RenderStack import Ui_renderStack_DockWidget
from RenderSettings import Ui_renderSettings_dockWidget


class RenderSettings(QtGui.QDockWidget, Ui_renderSettings_dockWidget):

    def __init__(self, parent=None):
        super(RenderSettings, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle('Render Settings')
        self.setFeatures(QtGui.QDockWidget.DockWidgetFloatable | QtGui.QDockWidget.DockWidgetMovable)
        self.setAllowedAreas(QtCore.Qt.RightDockWidgetArea)
        self.show()

class RenderStack(QtGui.QDockWidget, Ui_renderStack_DockWidget):

    def __init__(self, parent=None):
        super(RenderStack, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle('MVM Render Stack')
        self.renderSettigns = RenderSettings(self)
        #self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.renderSettigns)
        self.show()




def main():
    app = QtGui.QApplication(sys.argv)
    ex = RenderStack()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()