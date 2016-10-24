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


        data = {'project': sgProject, 'sg_scenename': sceneName, 'sg_renderlayer': renderLayer,
                'sg_rlstatus': renderStatus, 'sg_rlpriority': rlPriority, 'sg_rlmachine': rlMachine,
                'sg_rlprojectpath': rlProjectPath, 'sg_startframe': startFrame, 'sg_endframe': endFrame,
                'sg_rlforce': rlForce, 'sg_rlrenderengine': rlEngine, 'sg_rlrenderflags': rlFlags}

        self.sg.create('CustomEntity01', data)

    def getRenderLayer(self, sgId):

        filters = [['id', 'is', sgId]]
        fields = ['project', 'sg_scenename', 'sg_renderlayer','sg_rlstatus', 'sg_rlpriority', 'sg_rlmachine',
                'sg_rlprojectpath', 'sg_startframe', 'sg_endframe','sg_rlforce', 'sg_rlrenderengine',
                  'sg_rlrenderflags']

        rl = self.sg.find_one('CustomEntity01', filters, fields)
        print rl

    def getAllRenderLayer(self, renderMachine):

        filters = [['sg_rlmachine', 'is', renderMachine]]
        #
        # fields = ['project', 'sg_scenename', 'sg_renderlayer','sg_rlstatus', 'sg_rlpriority', 'sg_rlmachine',
        #         'sg_rlprojectpath', 'sg_startframe', 'sg_endframe','sg_rlforce', 'sg_rlrenderengine',
        #           'sg_rlrenderflags']

        fields = ['sg_rlpriority']

        order = [{'field_name': 'sg_rlpriority', 'direction':'desc'}, {'field_name':'id', 'direction':'asc'}]

        rl = self.sg.find('CustomEntity01', filters, fields, order)
        print rl

    def updateSgRL(self, sgId, sgRenderStatus, sgRenderPriority):

        data = {'renderStatus': sgRenderStatus, 'renderPriority': sgRenderPriority}
        self.sg.update('CustomEntity01', sgId, data)

# testDic = {'sceneName':'test/test/test.ma', 'renderLayer': 'RenderTest', 'renderStatus': 'ready to start',
#            'renderPriority': 'NORMAL', 'rlMachine': 'Render01', 'rlProjectPath': 'test',
#            'startFrame': 1, 'endFrame': 48, 'rlForce': False, 'rlEngine': 'mr', 'rlFlags': '-v 5'}

#sgUtils = ShotgunUtils()
# for x in range(1,10):
#     sgUtils.createRenderLayer(testDic)

#sgUtils.getAllRenderLayer('Render01')