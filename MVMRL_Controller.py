import sys
import os
from PySide import QtGui
from PySide import QtCore

import pymel.core as pm
import maya.mel as mel

from RenderLayerDockW import Ui_renderLayerDockWidget
from CastShadow import Ui_CastShadowsDockWidget
from Contour import Ui_ContourCtrls
from sgConnection import ShotgunUtils
from RederStack import RenderStack

class ContourCtrls(QtGui.QDockWidget, Ui_ContourCtrls):
    def __init__(self, parent=None):
        super(ContourCtrls, self).__init__(parent)
        self.setupUi(self)
        self.setAllowedAreas(QtCore.Qt.RightDockWidgetArea)
        self.setFloating(True)

        self.isInline()
        val = self.getContourSwitch()

        self.contourWidth_spinBox.setValue(float(val))

        '''Connections'''
        self.setSettings_pushButton.clicked.connect(self.setContourSettings)
        self.enableNormaContrast_checkBox.stateChanged.connect(self.checkState)
        self.show()

    def setContourSettings(self):

        normalContrast = self.normalContrast_spinBox.value()
        enableContrast = self.enableNormaContrast_checkBox.isChecked()

        self.setContourSwitch()

        miOptions = pm.ls(type="mentalrayOptions")

        for options in miOptions:

            if options.name() == "miDefaultOptions":
                try:
                    options.contourNormal.set(normalContrast)
                    options.enableContourNormal.set(enableContrast)
                except:
                    pass

        self.close()

    def isInline(self):
        rls = pm.ls(type='renderLayer')

        if rls:
            currentRl = rls[0].currentLayer()

            if 'Inline' in currentRl.name():
                self.enableNormaContrast_checkBox.setChecked(True)
                self.normalContrast_spinBox.setDisabled(False)
                self.normalContrast_label.setDisabled(False)

            else:
                self.enableNormaContrast_checkBox.setChecked(False)
                self.normalContrast_spinBox.setDisabled(True)
                self.normalContrast_label.setDisabled(True)

    def checkState(self, state):

        if state == QtCore.Qt.Checked:
            self.normalContrast_spinBox.setDisabled(False)
            self.normalContrast_label.setDisabled(False)

        else:
            self.normalContrast_spinBox.setDisabled(True)
            self.normalContrast_label.setDisabled(True)


    def getContourSwitch(self):

        defaultRGs = pm.ls(type='renderGlobals')
        if defaultRGs:
            drg = defaultRGs[0]
            contourSwitch = drg.preRenderLayerMel.get()
            if contourSwitch:
                splited = contourSwitch.split(' ')
                print splited
                value = splited[-1].split(';')
                print value[0]
                return value[0]

            else:
                messageBox = QtGui.QMessageBox()
                messageBox.setText('No flag set')
                messageBox.exec_()


    def setContourSwitch(self):

        defaultRGs = pm.ls(type='renderGlobals')
        if defaultRGs:
            drg = defaultRGs[0]
            contourSwitch = drg.preRenderLayerMel.get()
            if contourSwitch:
                splited = contourSwitch.split(' ')
                print splited
                splited[-1] = '{0};'.format(self.contourWidth_spinBox.value())
                melcmd = ' '.join(splited)
                print melcmd
                drg.preRenderLayerMel.set(melcmd)

            else:
                messageBox = QtGui.QMessageBox()
                messageBox.setText('No flag set')
                messageBox.exec_()



class CastShadow(QtGui.QDockWidget, Ui_CastShadowsDockWidget):
    def __init__(self, parent=None):
        super(CastShadow, self).__init__(parent)
        self.setupUi(self)
        self.setAllowedAreas(QtCore.Qt.RightDockWidgetArea)
        self.setFloating(True)

        '''Connections'''
        self.setCastShadow_pushButton.clicked.connect(self.setCastShadows)
        self.setReceiveShadow_pushButton.clicked.connect(self.setReceiveShadows)
        self.close_pushButton.clicked.connect(self.closeWindow)

        self.shadowCastSh = pm.shadingNode('surfaceShader', asShader=True, name='Shadow_Cast')
        self.shadowCastSh.outColor.set(pm.dt.Color(1, 1, 1))

        self.shadowReceiveSh = pm.shadingNode('useBackground', asShader=True, name='Shadow_Receive')
        self.shadowReceiveSh.specularColor.set(pm.dt.Color(0, 0, 0))
        self.shadowReceiveSh.reflectivity.set(0)
        self.shadowReceiveSh.reflectionLimit.set(0)

        self.show()

    def setCastShadows(self):
        objts = pm.ls(selection=True)

        if objts:
            rls = pm.ls(type='renderLayer')
            renderLayer = rls[0].currentLayer()


            for obj in objts:
                print obj
                meshes = obj.listRelatives(shapes=True)
                for mesh in meshes:

                    try:
                        renderLayer.addAdjustments([mesh.primaryVisibility, mesh.castsShadows])
                        mesh.primaryVisibility.set(0)
                        mesh.castsShadows.set(1)

                    except:
                        pass

                    shadingGroups = mesh.listConnections(type='shadingEngine')
                    print shadingGroups
                    for sg in shadingGroups:
                        print sg
                        try:
                            renderLayer.addAdjustments(sg.surfaceShader)
                            pm.connectAttr(self.shadowCastSh.outColor, sg.surfaceShader, force=True)
                        except:
                            pass

    def setReceiveShadows(self):

        objts = pm.ls(selection=True)

        if objts:
            rls = pm.ls(type='renderLayer')
            renderLayer = rls[0].currentLayer()

            for obj in objts:
                meshes = obj.listRelatives(shapes=True)

                for mesh in meshes:
                    try:
                        renderLayer.addAdjustments(mesh.castsShadows)
                        mesh.castsShadows.set(0)
                    except:
                        pass

                shadingGroups = mesh.listConnections(type='shadingEngine')

                for sg in shadingGroups:
                    try:
                        renderLayer.addAdjustments(sg.surfaceShader)
                        pm.connectAttr(self.shadowReceiveSh.outColor, sg.surfaceShader, force=True)
                    except:
                        pass

    def closeWindow(self):

        rls = pm.ls(type='renderLayer')
        renderLayer = rls[0].currentLayer()

        masterLayer = renderLayer.defaultRenderLayer()
        masterLayer.setCurrent()
        pm.select(clear=True)
        self.close()


class MVM_RLSetUp(QtGui.QDockWidget, Ui_renderLayerDockWidget):

    def __init__(self, parent=None):
        super(MVM_RLSetUp, self).__init__(parent)

        self.mainWindow = parent
        self.setupUi(self)
        self.setWindowTitle('RenderLayer SetUp')
        self.setAllowedAreas(QtCore.Qt.RightDockWidgetArea)
        self.setFloating(True)
        self.show()

        '''Connect Buttons'''

        self.colorLightRl_pushButton.clicked.connect(self.setColorLightRls)
        self.glowRl_pushButton.clicked.connect(self.setGlowRl)
        self.trailRl_pushButton.clicked.connect(self.setTrailRl)
        self.shadow_pushButton.clicked.connect(self.setShadowRl)
        self.matteRl_pushButton.clicked.connect(self.setMatteRl)
        self.inOutLine_pushButton.clicked.connect(self.setInOutLineRl)
        self.includeRl_pushButton.clicked.connect(self.setIncludeRl)
        self.zDepth_pushButton.clicked.connect(self.setZDepth)
        self.submitStack_pushButton.clicked.connect(self.submit2Stack)
        self.openStack_pushButton.clicked.connect(self.openStack)

        self.texture_pushButton.clicked.connect(self.getConTextura)
        self.contourSettings_pushButton.clicked.connect(self.contourWindow)

        ''' default rl Dictionary'''
        self.rlDic = {'code': 'shotName','sceneName':'test/test/test.ma', 'renderLayer': 'RenderTest',
                      'renderStatus': 'ready to start', 'renderPriority': '1', 'rlMachine': 'Render00',
                      'rlProjectPath': 'test', 'startFrame': 1, 'endFrame': 48, 'rlForce': False,
                      'rlEngine': 'mr', 'rlFlags': '-v 5'}

    def setColorLightRls(self):

        selection = pm.ls(selection=True)
        if not selection:
            self.openMessage('Select objects for this render Layer')
            return None
        else:

            prefix = self.openTextDialog('RL Prefix', 'set RL Prefix')

            if prefix:

                ''' create RlColor'''
                colorPrefix = prefix + '_Color'

                rlColor = self.createRenderLayer(selection, colorPrefix)
                rlColor.setCurrent()
                self.brightness(rlColor)
                print 'Render Layer {0} created and Overrides Applied'.format(rlColor.name())


                lightDirPrefix = prefix + '_Light_Dir'
                rlLightDir = self.createRenderLayer(selection, lightDirPrefix)
                rlLightDir.setCurrent()
                self.setBaseColorOverride(rlLightDir)

                print 'Render Layer {0} created and Overrides Applied'.format(rlLightDir.name())

                lightAmbPrefix = prefix + '_Light_Amb'
                rlLightAmb = self.createRenderLayer(selection, lightAmbPrefix)
                rlLightAmb.setCurrent()
                self.setBaseColorOverride(rlLightAmb)

                print 'Render Layer {0} created and Overrides Applied'.format(rlLightAmb.name())

                masterLayer = rlLightDir.defaultRenderLayer()
                masterLayer.setCurrent()
        pm.select(clear=True)

    def setGlowRl(self):

        selection = pm.ls(selection=True)
        if not selection:
            self.openMessage('Select objects for this render Layer')
            return None
        else:
            prefix = self.openTextDialog('RL Prefix', 'set RL Prefix')

            if prefix:
                glowPrefix = prefix + '_Glow'
                rlGlow = self.createRenderLayer(selection, glowPrefix)
                rlGlow.setCurrent()
                self.glowSetUp(rlGlow)
                print 'Render Layer {0} created and Overrides Applied'.format(rlGlow.name())
                masterLayer = rlGlow.defaultRenderLayer()
                masterLayer.setCurrent()
        pm.select(clear=True)

    def setTrailRl(self):

        selection = pm.ls(selection=True)
        if not selection:
            self.openMessage('Select objects for this render Layer')
            return None
        else:
            prefix = self.openTextDialog('RL Prefix', 'set RL Prefix')

            if prefix:
                TrailPrefix = prefix + '_Trails'
                rlTrail = self.createRenderLayer(selection, TrailPrefix)
                rlTrail.setCurrent()
                self.TrailRlSetUp(rlTrail)
                print 'Render Layer {0} created and Overrides Applied'.format(rlTrail.name())

                masterLayer = rlTrail.defaultRenderLayer()
                masterLayer.setCurrent()
        pm.select(clear=True)

    def setShadowRl(self):

        selection = pm.ls(selection=True)
        if not selection:
            self.openMessage('Select objects for this render Layer')
            return None
        else:
            prefix = self.openTextDialog('RL Prefix', 'set RL Prefix')

            if prefix:
                shadowPrefix = prefix + '_Shadows'
                rlShadow = self.createRenderLayer(selection, shadowPrefix)
                rlShadow.setCurrent()
                pm.select(clear=True)

                castShadowWidget = CastShadow(self.mainWindow)


        pm.select(clear=True)

    def setMatteRl(self):

        selection = pm.ls(selection=True)
        if not selection:
            self.openMessage('Select objects for this render Layer')
            return None
        else:
            prefix = self.openTextDialog('RL Prefix', 'set RL Prefix')

            if prefix:
                mattePrefix = prefix + '_Matte'
                rlMatte = self.createRenderLayer(selection, mattePrefix)
                rlMatte.setCurrent()

                '''RL Matte settings'''
                matteSh = pm.shadingNode('surfaceShader', asShader=True, name='matteSh')
                matteSh.outColor.set(pm.dt.Color(1, 1, 1))

                for obj in selection:

                    meshes = obj.listRelatives(type='shape')

                    for mesh in meshes:
                        shadingGroups = mesh.listConnections(type='shadingEngine')

                        for sg in shadingGroups:
                            try:
                                rlMatte.addAdjustments(sg.surfaceShader)
                                pm.connectAttr(matteSh.outColor, sg.surfaceShader, force=True)
                            except:
                                pass

                print 'Render Layer {0} created and Overrides Applied'.format(rlMatte.name())

                masterLayer = rlMatte.defaultRenderLayer()
                masterLayer.setCurrent()

        pm.select(clear=True)

    def setInOutLineRl(self):

        selection = pm.ls(selection=True)
        if not selection:
            self.openMessage('Select objects for this render Layer')
            return None
        else:
            prefix = self.openTextDialog('RL Prefix', 'set RL Prefix')

            if prefix:
                inlinePrefix = prefix + '_Inline'
                rlInline = self.createRenderLayer(selection, inlinePrefix)
                rlInline.setCurrent()
                self.inlineDefault(rlInline)
                print 'Render Layer {0} created and Overrides Applied'.format(rlInline.name())

                outLinePrefix = prefix + '_Outline'
                rlOutline = self.createRenderLayer(selection, outLinePrefix)
                rlOutline.setCurrent()
                self.outlineDefault(rlOutline)
                print 'Render Layer {0} created and Overrides Applied'.format(rlOutline.name())

                masterLayer = rlOutline.defaultRenderLayer()
                masterLayer.setCurrent()


        pm.select(clear=True)

    def setIncludeRl(self):

        selection = pm.ls(selection=True)
        if not selection:
            self.openMessage('Select objects for this render Layer')
            return None
        else:
            prefix = self.openTextDialog('RL Prefix', 'set RL Prefix')

            if prefix:
                includePrefix = prefix + '_Include'
                rlInclude = self.createRenderLayer(selection, includePrefix)
                rlInclude.setCurrent()
                self.includeDefault(rlInclude)
                print 'Render Layer {0} created and Overrides Applied'.format(rlInclude.name())

        pm.select(clear=True)

    def setZDepth(self):
        pm.select(clear=True)

    def submit2Stack(self):

        renderLayers = pm.ls(type='renderLayer')
        renderSettings = pm.ls(type='renderGlobals')[0]

        if renderLayers:
            sg = ShotgunUtils()
            sceneName = pm.sceneName().splitext()
            projectPath = os.path.split(os.path.split(sceneName[0])[0])[0]

            shotName = os.path.split(sceneName[0])[1]
            rendeGlobals = pm.ls(type='renderGlobals')[0]

            for rl in renderLayers:
                if 'defaultRenderLayer' in rl.name():
                    pass

                else:
                    if rl.renderable.get() == 0:
                        pass
                    else:

                        rlSceneName = '{0}_{1}{2}'.format(sceneName[0], rl.name(), sceneName[1])
                        rl.setCurrent()

                        pm.saveAs(rlSceneName)

                        rlDict = self.rlDic
                        rlDict['code'] = shotName
                        rlDict['sceneName'] = rlSceneName
                        rlDict['renderLayer'] = rl.name()
                        rlDict['rlProjectPath'] = projectPath
                        rlDict['startFrame'] = int(rendeGlobals.startFrame.get())
                        rlDict['endFrame'] = int(rendeGlobals.endFrame.get())
                        rlDict['rlFlags'] = '-v 5 -rl {0}'.format(rl.name())

                        if 'Inline' in rl.name():
                            print renderSettings.preRenderLayerMel.get()
                            mel.eval(renderSettings.preRenderLayerMel.get())
                            rl.removeAdjustments(renderSettings.preRenderLayerMel)

                            rlDict['rlForce'] = True

                        elif 'Outline' in rl.name():
                            print renderSettings.preRenderLayerMel.get()
                            mel.eval(renderSettings.preRenderLayerMel.get())
                            rl.removeAdjustments(renderSettings.preRenderLayerMel)
                            rlDict['rlForce'] = True
                        else:
                            rlDict['rlForce'] = False
                        sg.createRenderLayer(rlDict)

    def openStack(self):
        renderStack = RenderStack(self.mainWindow)

    def openTextDialog(self, windowTitle, infoText):
        text, ok = QtGui.QInputDialog.getText(self, windowTitle, infoText)
        if ok:
            return text
        else:
            return None

    def openMessage(self, message):

        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(message)
        msgBox.exec_()

    def createRenderLayer(self, objList, rlName):

        rl = pm.createRenderLayer(objList, noRecurse=True, name=rlName)
        return rl

    def brightness(self, renderLayer):

        rampShaders = pm.ls(type='rampShader')
        for rampSh in rampShaders:

            if rampSh.colorInput.get() == 0:
                try:
                    renderLayer.addAdjustments(rampSh.colorInput)
                    rampSh.colorInput.set(2)

                except:
                    pass

    def setBaseColorOverride(self, renderLayer):

        rampList = pm.ls(type='rampShader')

        for rampShader in rampList:

            if (rampShader.name().find('ParaGlow')) == -1:
                try:
                    renderLayer.addAdjustments(rampShader.color[0].color_Color)
                    rampShader.color[0].color_Color.set(pm.dt.Color(0, 0, 0))
                except:
                    print rampShader.name()
                    pass
            else:
                pass

        fileList = pm.ls(type='file')

        for texture in fileList:
            if not (texture.name().find('dark_file') == -1):
                try:
                    renderLayer.addAdjustments(texture.colorGain)
                    texture.colorGain.set(pm.dt.Color(0, 0, 0))
                except:
                    pass
            else:
                pass

        for texture in fileList:
            if not (texture.name().find('NGlobo_TextureDark') == -1):
                try:
                    renderLayer.addAdjustments(texture.colorGain)
                    texture.colorGain.set(pm.dt.Color(0, 0, 0))
                except:
                    pass
            else:
                pass

    def glowSetUp(self, renderLayer):

        shadingGroups = pm.ls(type='shadingEngine')

        black = pm.shadingNode('surfaceShader', asShader=True, name='Glow_Black')
        black.outMatteOpacity.set(pm.dt.Color(0, 0, 0))

        for sg in shadingGroups:

            if not 'GlowSG' in sg.name():
                try:
                    renderLayer.addAdjustments(sg.surfaceShader)

                    pm.connectAttr(black.outColor, sg.surfaceShader, f=True)


                except:
                    pass

    def TrailRlSetUp(self, renderLayer):

        ''' set RenderSetings'''
        miGlobals = pm.ls(type='mentalrayGlobals')
        if miGlobals:
            for globals in miGlobals:
                try:
                    globals.exportCustomMotion.set(1)
                    globals.exportMotionOffset.set(0)
                except:
                    pass

        renderSettings = pm.ls(type='mentalrayOptions')

        miDefault = None

        for settings in renderSettings:

            if 'miDefaultOptions' in settings.name():
                miDefault = settings

        if miDefault:
            renderLayer.addAdjustments([miDefault.motionBlur, miDefault.miRenderUsing, miDefault.miSamplesQualityR,
                                    miDefault.motionSteps, miDefault.motionBlurBy])

            miDefault.motionBlur.set(2)
            miDefault.miRenderUsing.set(0)
            miDefault.miSamplesQualityR.set(1.5)
            miDefault.motionSteps.set(4)
            miDefault.motionBlurBy.set(4)

        '''shaders create'''

        black = pm.shadingNode('surfaceShader', asShader=True, name='Trail_Black')
        white = pm.shadingNode('surfaceShader', asShader=True, name='Trail_White')

        black.outMatteOpacity.set(pm.dt.Color(0, 0, 0))
        white.outColor.set(pm.dt.Color(1, 1, 1))

        ''' geo settings'''

        geoList = pm.ls(type='mesh')

        for geo in geoList:

            if 'turbina_centro_GEO' in geo.name():
                sg = geo.listConnections(type='shadingEngine')
                if sg:
                    try:
                        renderLayer.addAdjustments(sg[0].surfaceShader)
                        pm.connectAttr(white.outColor, sg[0].surfaceShader, f=True)
                    except:
                        pass

            else:
                geo.motionBlur.set(0)

                sg = geo.listConnections(type='shadingEngine')

                if sg:
                    try:
                        renderLayer.addAdjustments(sg[0].surfaceShader)
                        pm.connectAttr(black.outColor, sg[0].surfaceShader, f=True)
                    except:
                        pass

    def inlineDefault(self, renderLayer):

        '''contourSwitch pluggint needed'''
        defaultRGs = pm.ls(type='renderGlobals')
        if defaultRGs:
            for drg in defaultRGs:
                try:
                    renderLayer.addAdjustments(drg.preRenderLayerMel)
                    drg.preRenderLayerMel.set('contourSwitch_v002 -st 4 -il 0.5;')
                except:
                    pass

        inLineLambert = pm.shadingNode('lambert', asShader=True, name='inlineSh')

        miOptions = pm.ls(type="mentalrayOptions")
        ''' render Settings Options'''
        for options in miOptions:

            if options.name() == "miDefaultOptions":
                try:
                    renderLayer.addAdjustments([options.contourBackground, options.contourInstance,
                                                options.enableContourColor, options.contourColor, options.miRenderUsing,
                                                options.enableContourNormal, options.contourNormal,
                                                options.maxSamples])

                    options.contourBackground.set(0)
                    options.contourInstance.set(1)
                    options.enableContourColor.set(0)
                    options.contourColor.set(0.5, 0.5, 0.5)
                    options.miRenderUsing.set(2)
                    options.enableContourNormal.set(1)
                    options.contourNormal.set(4.5)
                    options.maxSamples.set(3)

                except:
                    pass
            else:
                pass
        '''Frame buffer Options'''
        frameBuffer = pm.ls(type="mentalrayFramebuffer")[0]
        if frameBuffer:
            try:
                renderLayer.addAdjustments([frameBuffer.contourEnable, frameBuffer.contourClearImage,
                                            frameBuffer.contourSamples, frameBuffer.contourFilter])
                frameBuffer.contourEnable.set(1)
                frameBuffer.contourClearImage.set(1)
                frameBuffer.contourSamples.set(3)
                frameBuffer.contourFilter.set(2)
            except:
                pass
        else:
            pass

        '''shading Group Overrides'''

        shadingGroups = pm.ls(type="shadingEngine")
        print shadingGroups
        for sg in shadingGroups:
            try:
                renderLayer.addAdjustments(sg.surfaceShader)
                pm.connectAttr(inLineLambert.outColor, sg.surfaceShader, force=True)

            except:
                pass

    def outlineDefault(self, renderLayer):

        '''contourSwitch pluggint needed'''
        defaultRGs = pm.ls(type='renderGlobals')
        if defaultRGs:
            for drg in defaultRGs:
                try:
                    renderLayer.addAdjustments(drg.preRenderLayerMel)
                    drg.preRenderLayerMel.set('contourSwitch_v002 -st 3 -ol 0.8;')
                except:
                    pass

        outLineLambert = pm.shadingNode('lambert', asShader=True, name='outlineSh')
        miOptions = pm.ls(type="mentalrayOptions")
        ''' render Settings Options'''
        for options in miOptions:

            if options.name() == "miDefaultOptions":
                try:
                    renderLayer.addAdjustments([options.contourBackground, options.contourInstance,
                                                options.enableContourColor, options.contourColor, options.miRenderUsing,
                                                options.enableContourNormal, options.contourNormal,options.maxSamples])

                    options.contourBackground.set(1)
                    options.contourInstance.set(0)
                    options.enableContourColor.set(0)
                    options.contourColor.set(0.5, 0.5, 0.5)
                    options.miRenderUsing.set(2)
                    options.enableContourNormal.set(0)
                    options.contourNormal.set(0)
                    options.maxSamples.set(3)
                    print "maxSamples set to 3"
                except:
                    pass
            else:
                pass
        '''Frame buffer Options'''
        frameBuffer = pm.ls(type="mentalrayFramebuffer")[0]
        if frameBuffer:
            try:
                renderLayer.addAdjustments([frameBuffer.contourEnable, frameBuffer.contourClearImage,
                                            frameBuffer.contourSamples, frameBuffer.contourFilter])
                frameBuffer.contourEnable.set(1)
                frameBuffer.contourClearImage.set(1)
                frameBuffer.contourSamples.set(3)
                frameBuffer.contourFilter.set(2)

            except:
                pass
        else:
            pass

        '''shading Group Overrides'''

        shadingGroups = pm.ls(type="shadingEngine")

        for sg in shadingGroups:
            try:
                renderLayer.addAdjustments(sg.surfaceShader)
                pm.connectAttr(outLineLambert.outColor, sg.surfaceShader, force=True)
            except:
                pass

    def includeDefault(self, renderLayer):
        print 'includeCreated'

    def mvmToonRamp(self):
        rampShader = pm.shadingNode('rampShader', asShader=True)
        rampShader.rename('NGlobo_CustomTexture')
        fileNodeLight = pm.shadingNode('file', asTexture=True)
        fileNodeLight.rename('NGlobo_TextureLight')
        fileNodeLight.fileTextureName.set(
            "D:/Data/Red/Proyecto_MVM_3D/Modelos/Nave_Globo_OKAY/sourceimages/usvNglobo_tex2.png")

        fileNodeDark = pm.shadingNode('file', asTexture=True)
        fileNodeDark.rename('NGlobo_TextureDark')
        fileNodeDark.colorGain.set(pm.dt.Color(0.61, 0.61, 0.61))

        fileNodeDark.fileTextureName.set(
            "D:/Data/Red/Proyecto_MVM_3D/Modelos/Nave_Globo_OKAY/sourceimages/usvNglobo_tex2.png")
        pm.connectAttr(fileNodeDark.outColor, rampShader.color[0].color_Color, f=True)
        pm.connectAttr(fileNodeLight.outColor, rampShader.color[1].color_Color, f=True)

        rampShader.color[1].color_Position.set(0.5)
        rampShader.color[0].color_Position.set(0.46)
        rampShader.color[0].color_Interp.set(1)
        rampShader.specularity.set(0)
        rampShader.eccentricity.set(0)
        rampShader.reflectivity[0].reflectivity_FloatValue.set(0)
        rampShader.colorInput.set(2)

        return rampShader

    def getConTextura(self):

        rampShader = self.mvmToonRamp()

        rampList = pm.ls(type='surfaceShader')

        conTexturaSG = []

        for ramp in rampList:

            if not (ramp.name().find('ShaderConTextura') == -1):
                conTexturaSG.append(ramp.listConnections(type='shadingEngine')[0])

        for sg in conTexturaSG:
            pm.connectAttr(rampShader.outColor, sg.surfaceShader, f=True)

    def contourWindow(self):

        contoruUi = ContourCtrls(self.mainWindow)









