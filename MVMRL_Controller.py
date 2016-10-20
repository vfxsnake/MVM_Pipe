import sys
from PySide import QtGui
from PySide import QtCore

import pymel.core as pm

from RenderLayerDockW import Ui_renderLayerDockWidget
from CastShadow import Ui_CastShadowsDockWidget
from Contour import Ui_ContourCtrls

class ContoruCtrls(QtGui.QDockWidget, Ui_ContourCtrls):
    def __init__(self, parent=None):
        super(ContoruCtrls, self).__init__(parent)
        self.setupUi(self)
        self.setAllowedAreas(QtCore.Qt.RightDockWidgetArea)
        self.setFloating(True)

        '''Connections'''
        self.setSettings_pushButton.clicked.connect(self.setContourSettings)

        self.show()

    def setContourSettings(self):
        contourWidth = self.contourWidth_spinBox.value()
        normalContrast = self.normalContrast_spinBox.value()

        shadingGroups = pm.ls(type="shadingEngine")
        for sg in shadingGroups:
            try:
                sg.miContourWidth.set(contourWidth)
            except:
                pass

        miOptions = pm.ls(type="mentalrayOptions")

        for options in miOptions:

            if options.name() == "miDefaultOptions":
                try:
                    options.contourNormal.set(normalContrast)
                except:
                    pass

        self.close()


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
                self.inlineDefault(rlInclude)
                print 'Render Layer {0} created and Overrides Applied'.format(rlInclude.name())

        pm.select(clear=True)

    def setZDepth(self):
        pm.select(clear=True)


    def submit2Stack(self):
        print 'Submitting'

    def openStack(self):
        print 'opening RenderStack'

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

        miOptions = pm.ls(type="mentalrayOptions")
        ''' render Settings Options'''
        for options in miOptions:

            if options.name() == "miDefaultOptions":
                try:
                    renderLayer.addAdjustments([options.contourBackground, options.contourInstance,
                                                options.enableContourColor, options.contourColor, options.miRenderUsing,
                                                options.enableContourNormal, options.contourNormal])

                    options.contourBackground.set(0)
                    options.contourInstance.set(1)
                    options.enableContourColor.set(0)
                    options.contourColor.set(0.5, 0.5, 0.5)
                    options.miRenderUsing.set(2)
                    options.enableContourNormal.set(1)
                    options.contourNormal.set(0.45)
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
                renderLayer.addAdjustments([sg.miContourEnable, sg.miContourWidth, sg.miContourColor])
                sg.miContourEnable.set(1)
                sg.miContourWidth.set(0.5)
                sg.miContourColor.set(0, 0, 0)
            except:
                pass

    def outlineDefault(self, renderLayer):

        miOptions = pm.ls(type="mentalrayOptions")
        ''' render Settings Options'''
        for options in miOptions:

            if options.name() == "miDefaultOptions":
                try:
                    renderLayer.addAdjustments([options.contourBackground, options.contourInstance,
                                                options.enableContourColor, options.contourColor, options.miRenderUsing,
                                                options.enableContourNormal, options.contourNormal])

                    options.contourBackground.set(1)
                    options.contourInstance.set(0)
                    options.enableContourColor.set(0)
                    options.contourColor.set(0.5, 0.5, 0.5)
                    options.miRenderUsing.set(2)
                    options.enableContourNormal.set(0)
                    options.contourNormal.set(0)
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
                renderLayer.addAdjustments([sg.miContourEnable, sg.miContourWidth, sg.miContourColor])
                sg.miContourEnable.set(1)
                sg.miContourWidth.set(0.85)
                sg.miContourColor.set(0, 0, 0)
            except:
                pass

    def includeDefault(self, renderLayer):

        miOptions = pm.ls(type="mentalrayOptions")
        ''' render Settings Options'''
        for options in miOptions:

            if options.name() == "miDefaultOptions":
                try:
                    renderLayer.addAdjustments([options.contourBackground, options.contourInstance,
                                                options.enableContourColor, options.contourColor, options.miRenderUsing,
                                                options.enableContourNormal, options.contourNormal])

                    options.contourBackground.set(0)
                    options.contourInstance.set(1)
                    options.enableContourColor.set(0)
                    options.contourColor.set(0.5, 0.5, 0.5)
                    options.miRenderUsing.set(2)
                    options.enableContourNormal.set(1)
                    options.contourNormal.set(0.45)
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
                frameBuffer.contourClearImage.set(0)
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
                renderLayer.addAdjustments([sg.miContourEnable, sg.miContourWidth, sg.miContourColor])
                sg.miContourEnable.set(1)
                sg.miContourWidth.set(0.5)
                sg.miContourColor.set(0, 0, 0)
            except:
                pass

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

        contoruUi = ContoruCtrls(self.mainWindow)









