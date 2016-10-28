import sys
sys.path.append('D:\Data\plug-ins\MVM_Pipe\python-api')
sys.path.append('D:\Data\plug-ins\MVM_Pipe\ui')

from PySide import QtGui
from CompStack import CompStack


def main():
    app = QtGui.QApplication(sys.argv)
    ex = CompStack()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
