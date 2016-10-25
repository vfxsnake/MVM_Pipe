import sys
from PySide import QtGui
from RederStack import RenderStack


def main():
    app = QtGui.QApplication(sys.argv)
    ex = RenderStack()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()