
from shotgun_api3 import Shotgun

class ShotgunUtils():

    def __init__(self):


        SERVER_PATH = "https://hcpstudio.shotgunstudio.com"
        SCRIPT_NAME = 'MVMRender'
        SCRIPT_KEY = '4ea5b0d58e284b7c0bdbebbe331438b79ccf1b4e7dad3edb3930314923a127f2'

        self.sg = Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)



    def getFields(self, entityName, fieldName=None):
        squemaDic = self.sg.schema_field_read(entityName, fieldName)
        print squemaDic
        for squema in squemaDic:
            print squema

    def createRenderLayer(self, sceneDic):

        sgProject = {'type': 'Project', 'id': 94}
        sceneName = sceneDic['sceneName']
        renderLayer = sceneDic['renderLayer']
        renderStatus = sceneDic['renderStatus']
        rlPriority = sceneDic['renderPriority']
        rlMachine = sceneDic['rlMachine']
        rlProjectPath = sceneDic['rlProjectPath']
        startFrame = sceneDic['startFrame']
        endFrame = sceneDic['endFrame']
        rlForce = sceneDic['rlForce']
        rlEngine = sceneDic['rlEngine']
        rlFlags = sceneDic['rlFlags']
        code = sceneDic['code']


        data = {'project': sgProject, 'sg_scenename': sceneName, 'sg_renderlayer': renderLayer,
                'sg_rlstatus': renderStatus, 'sg_rlpriority': rlPriority, 'sg_rlmachine': rlMachine,
                'sg_rlprojectpath': rlProjectPath, 'sg_startframe': startFrame, 'sg_endframe': endFrame,
                'sg_rlforce': rlForce, 'sg_rlrenderengine': rlEngine, 'sg_rlrenderflags': rlFlags, 'code': code}

        self.sg.create('CustomEntity01', data)

    def getRenderLayer(self, sgId):

        filters = [['id', 'is', sgId]]
        fields = ['project', 'sg_scenename', 'sg_renderlayer','sg_rlstatus', 'sg_rlpriority', 'sg_rlmachine',
                'sg_rlprojectpath', 'sg_startframe', 'sg_endframe','sg_rlforce', 'sg_rlrenderengine',
                  'sg_rlrenderflags', 'code']

        rl = self.sg.find_one('CustomEntity01', filters, fields)
        print rl

    def getAllRenderLayer(self, renderMachine=None):

        filters = [['sg_rlmachine', 'is', renderMachine]]

        fields = ['project', 'sg_scenename', 'sg_renderlayer','sg_rlstatus', 'sg_rlpriority', 'sg_rlmachine',
                'sg_rlprojectpath', 'sg_startframe', 'sg_endframe','sg_rlforce', 'sg_rlrenderengine',
                  'sg_rlrenderflags', 'code']



        order = [{'field_name': 'sg_rlpriority', 'direction':'desc'}, {'field_name':'id', 'direction':'asc'}]

        if renderMachine:
            rl = self.sg.find('CustomEntity01', filters, fields, order)
            return rl

        else:
            rl = self.sg.find('CustomEntity01', [], fields, order)
            return rl

    def getAllRlReady(self, renderMachine):
        filters = [['sg_rlmachine', 'is', renderMachine], ['sg_rlstatus', 'is', 'ready to start']]

        fields = ['project', 'sg_scenename', 'sg_renderlayer','sg_rlstatus', 'sg_rlpriority', 'sg_rlmachine',
                'sg_rlprojectpath', 'sg_startframe', 'sg_endframe','sg_rlforce', 'sg_rlrenderengine',
                  'sg_rlrenderflags', 'code']
        order = [{'field_name': 'sg_rlpriority', 'direction': 'desc'}, {'field_name': 'id', 'direction': 'asc'}]

        rl = self.sg.find('CustomEntity01', filters, fields, order)
        return rl

    def updateSgRL(self, sgId, sgRenderStatus, sgRenderPriority, sgRenderMachine, sgProjectPath, renderEngine,
                   renderFlags, startFrame, endFrame, force):

        data = {'renderStatus': sgRenderStatus, 'renderPriority': sgRenderPriority, 'sg_rlmachine': sgRenderMachine,
                'sg_rlprojectpath': sgProjectPath, 'sg_rlrenderengine': renderEngine, 'sg_rlrenderflags': renderFlags,
                'sg_startframe': startFrame, 'sg_endframe': endFrame, 'sg_rlforce': force}
        self.sg.update('CustomEntity01', sgId, data)

