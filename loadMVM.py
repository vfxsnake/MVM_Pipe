import sys

sys.path.append('D:\Data\plug-ins\MVM_Pipe\ui')
sys.path.append('D:\Data\plug-ins\MVM_Pipe')
sys.path.append('D:\Data\plug-ins\MVM_Pipe\python-api')

import MVMRL_Controller

from PySide import QtCore
from PySide import QtGui
import shiboken
import maya.OpenMayaUI as mui
 
ptr = mui.MQtUtil.mainWindow()
mainWindow = shiboken.wrapInstance(long(ptr), QtGui.QWidget)

rlSetUp = MVMRL_Controller.MVM_RLSetUp(mainWindow)     