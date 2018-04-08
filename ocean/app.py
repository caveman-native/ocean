from bottle import route,run,template,request,static_file
from readCfg import readProperties,getProperties
from updateKey import replace_key
from constants import *
from tinydb import TinyDB,Query
import json
from writeConfig import downloadConfigFile
#config = ConfigParser.RawConfigParser()
#from readCfg import readProperties

patterndb = TinyDB('pattern.json') 
profiledb = TinyDB('profile.json')
query = Query()

def compareProperties(request):
    data = {}
    keys=readProperties()
    for key, value in keys.items():
       if value == request.forms.get(key):
         print(key,'not changed.')
       else:
         print(key,'changed.')
         data.update({key : request.forms.get(key)})
        
    print(data)
    return data
     
# Static Routes
@route("/static/css/<filepath:re:.*\.css>")
def css(filepath):
   return static_file(filepath, root="static/css")

@route("/static/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="static/js")

@route("/static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
   return static_file(filepath, root="static/img")


@route("/")
def index():
    return template('viewConfig',
    supervisors = getProperties(SUPERVISOR),
    imm = getProperties(IMM),
    hosts = getProperties(HOST))


@route("/profile",method = "get")
def profile():
    return template('profile', meta = '',
                           type = '',
                           direction = '',
                           interval = '',
                           stopCheck = '',
                           shallowWindow = '',
                           shallowDepth = '',
                           deepDepth = '',
                           deepWindow = '',
                           rampTime = '',
                           maxTime = '',
                           backtrackTimes = '',
                           stallTimeout = '',
                           ctdWrapupTime = '',
                           backtrackCount = '',
                           dpdt = '')

@route("/profile",method = "post")
def profile():
    return template('profile', meta='',
                    type='',
                    direction='',
                    interval='',
                    stopCheck='',
                    shallowWindow='',
                    shallowDepth='',
                    deepDepth='',
                    deepWindow='',
                    rampTime='',
                    maxTime='',
                    backtrackTimes='',
                    stallTimeout='',
                    ctdWrapupTime='',
                    backtrackCount='',
                    dpdt='')

@route("/pattern",method = "get")
def profile():
    return template('pattern', meta = '',
                           type = '',
                           sequence = '',
                           status = '',
                           start_dt = '',
                           stop_dt = ''
            )

@route("/pattern",method = "post")
def profile():
    return template('pattern', meta = '',
                           type = '',
                           sequence = '',
                           status = '',
                           start_dt = '',
                           stop_dt = ''
            )


@route("/",method="post")
def test():
    gps_interval = request.forms.get('supervisor.gps_interval')
    wake_mode = request.forms.get('supervisor.wake_mode')
    alarm_interval = request.forms.get('supervisor.alarm_interval')
    print(wake_mode)
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print(gps_interval)
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print(alarm_interval)
    updatedProps = compareProperties(request)
    updatedVals = {}
    if (len(updatedProps.keys()) > 0):
            
             # Writing our configuration file 
              with open(CONFIG_FILE, 'r+') as configfile:
                 try:   
                    for key, value in updatedProps.items():
                       print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                       print('updating', key)
                       print('value', value)
                       print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
                       #updatedVals.update({key,value})
                       updatedVals[key]= value
                       #replace_key(configFile,key, value)
                 finally:
                    if configfile is not None:
                      configfile.close()

              if(len(updatedVals) > 0): 
                 for k,v in updatedVals.items():
                    replace_key(CONFIG_FILE,k,v)
    else:
        print('No Config values updated.')
    
    return template('viewConfig',
                     supervisors = getProperties(SUPERVISOR),
                     imm = getProperties(IMM),
                     hosts = getProperties(HOST)) 


@route("/editConfig")
def index():
    return template('editConfig',  supervisors = getProperties(SUPERVISOR),
                     imm = getProperties(IMM),
                     hosts = getProperties(HOST))
                     
@route("/viewChart")
def index():
    return template('viewChart')                     


@route("/profilepatterns",method = "post")
def profiles():
  
   profiledb.insert({'description':request.forms.get('description'),
   'type':request.forms.get('type'),
   'direction':request.forms.get('direction'),
   'interval':request.forms.get('interval'),
   'stopCheck':request.forms.get('stopcheck'),
   'shallowWindow':request.forms.get('shallowWindow'),
   'shallowDepth':request.forms.get('shallowDepth'),
   'deepDepth':request.forms.get('deepDepth'),
   'deepWindow':request.forms.get('deepWindow'),
   'rampTime':request.forms.get('rampTime'),
   'maxTime':request.forms.get('maxTime'),
   'backtrackTimes':request.forms.get('backtrackTimes'),
   'stallTimeout':request.forms.get('stallTimeout'),
   'ctdWrapupTime':request.forms.get('ctdWrapupTime'),
   'backtrackTimes':request.forms.get('backtrackTimes'),
   'backtrackCount':request.forms.get('backtrackCount'),
   'dpdt':request.forms.get('dpdt')
   })
   
   print(profiledb.all())
 
   return template('profilePatterns' , profile_rows = profiledb.all())



@route("/profilepatterns",method = "get")
def profiles():
   #profiledb = TinyDB('profile.json')
   #print(profiledb)
   return template('profilePatterns', profile_rows = profiledb.all() )

@route("/createProfile",method = "get")
def createProfile():
   return '''<form action='/createProfile' id="create-profile" method='post'>
   meta : <input name="meta" id="meta" type="text" maxlength="200" required/>
   type : <input name="type" type="number" id="type" max="200" min="0"/>
   direction : <input name="direction" type="number" id="direction" max="200" min="0" />
   interval: <input name="interval" type="number" id="meta" max="200" min="0" />
   stopCheck:<input name="stopCheck" type="number" id="stopCheck" max="200" min="0" />
   shallowWindow:<input name="shallowWindow" type="number" id="shallowWindow" max="200" min="0" />
   shallowDepth:<input name="shallowDepth" type="number" id="shallowDepth" max="200" min="0" />
   deepDepth:<input name="deepDepth" type="number" id="deepDepth" max="200" min="0" />
   deepWindow:<input name="deepWindow" type="number" id="deepWindow" max="200" min="0" />
   rampTime:<input name="rampTime" type="number" id="rampTime" max="200" min="0" />
   maxTime:<input name="maxTime" type="number" id="maxTime" max="200" min="0" />
   backtrackTimes:<input name="backtrackTimes" type="number" id="backtrackTimes" max="200" min="0" />
   stallTimeout:<input name="stallTimeout" type="number" id="stallTimeout" max="200" min="0" />
   ctdWrapupTime:<input name="ctdWrapupTime" type="number" id="ctdWrapupTime" max="200" min="0" />
   backtrackTimes:<input name="backtrackTimes" type="number" id="backtrackTimes" max="200" min="0" />
   backtrackCount:<input name="backtrackCount" type="number" id="backtrackCount" max="200" min="0" />
   dpdt:<input name="dpdt" type="number" maxlength="200" id="dpdt" max="200" min="0"/>
   <input value="Create Profile"  id="profile-submit" type="submit"  />
   </form>'''


@route("/createProfile",method = "post")
def createProfile():
    meta = request.forms.get('meta')
    
    #check if meta is null or not
    if meta:
        #check if meta exists 
        if not profiledb.search(query.meta == meta):
           #insert data
           profiledb.insert({'profile.meta':request.forms.get('meta'),
            'profile.type':request.forms.get('type'),
            'profile.direction':request.forms.get('direction'),
            'profile.interval':request.forms.get('interval'),
            'profile.stopCheck':request.forms.get('stop_check'),
            'profile.shallowWindow':request.forms.get('shallow_window'),
            'profile.shallowDepth':request.forms.get('shallow_depth'),
            'profile.deepDepth':request.forms.get('deep_depth'),
            'profile.deepWindow':request.forms.get('deep_window'),
            'profile.rampTime':request.forms.get('ramp_time'),
            'profile.maxTime':request.forms.get('max_time'),
            'profile.backtrackTimes':request.forms.get('backtrack_time'),
            'profile.stallTimeout':request.forms.get('stall_timeout'),
            'profile.ctdWrapupTime':request.forms.get('ctd_warmup_time'),
            'profile.backtrackCount':request.forms.get('backtrack_count'),
            'profile.dpdt':request.forms.get('dpdt_threshold')
            })
           return " Profile added successfully."
        else:
            return " Profile already exists with same description(meta). Please change the meta description(meta)."

    else:
        return " Please enter profile description(meta)."

@route("/createPattern",method = "get")
def createPattern():

   return '''<form id="create-pattern-form" action='/createPattern' method='post'>
    Meta: <input id="meta" name="meta" type="text" maxlength="200" required/>
    Start Date: <input id="start-date" name="start_dt" type="date" min="2018-04-01" max="2020-04-30" />
    Stop Date: <input id="end-dt" name="stop_dt" type="date" min="2018-04-01" max="2021-04-30" />
    Type: <input id="type" name="type" type="number" min="0" max= "2"/>
    Status: <input id="status" name="status" type="number" min="0" max= "1"/>
    <input id="pattern-submit" value="Create Pattern" type="submit" /> </form>'''


@route("/createPattern",method = "post")
def createPattern():
    meta = request.forms.get('meta')
    start_dt = request.forms.get('start_dt')
    stop_dt = request.forms.get('stop_dt')
    type = request.forms.get('type')
    status = request.forms.get('status')
    sequence = request.forms.get('sequence')
    #check if meta is null or not
    if meta:
        #check if meta exists 
        if not patterndb.search(query.meta == meta):
           #insert data
           patterndb.insert({'pattern.meta':meta,
                            'pattern.type':type,
                            'pattern.start_dt':start_dt,
                            'pattern.stop_dt':stop_dt,
                            'pattern.sequence' : sequence,
                            'pattern.status':status
                           })
           return " Pattern added successfully. "
        else:
            return " Pattern already exists with same description. Please change the meta description. "

    else:
        return " Please enter pattern description. "




@route("/viewPatterns",method = "get")
def viewPatterns():
    data = {}
    for pattern in patterndb:
        data[pattern.doc_id] = pattern
    
    #print(data)
    # Need Json or Map?
    return data

@route("/viewProfiles",method = "get")
def viewProfiles():
    data = {}
    for profile in profiledb:
        data[profile.doc_id] = profile
    
    #print(data)
    return data


@route("/deletePattern/<key>",method = "get")
def deletePattern(key):
    if key:
        documentId = int(key)
        pattern = patterndb.contains(doc_ids=[documentId])

        print(pattern)
        #check if pattern id exists 
        if pattern:
            print('Remove Item : Found item with doc id: ', key)
            patterndb.remove(doc_ids=[documentId]) 
            return '<p>Pattern removed successfully </p>'
        else:
            return '<p>No value found with passed document id.</p>'     
    else:
        return '<p> Please pass document id to delete the element. </p> ' 



@route("/deleteProfile/<key>",method = "get")
def deleteProfile(key):
    #print('key is:' ,int(key))
    if key:
        documentId = int(key)
        profile = profiledb.contains(doc_ids=[documentId])

        print(profile)
        #check if profile id exists 
        if profile:
            print('Remove Item : Found item with doc id: ', key)
            profiledb.remove(doc_ids=[documentId]) 
            return '<p>Profile removed successfully </p>'
        else:
            return '<p>No value found with passed document id.</p>'     
    else:
        return '<p>Please pass document id to delete the element.</p>' 





@route("/pattern/edit/<pattern>",method = "post")
def updatePattern(pattern):

    meta = request.forms.get('meta')
    start_dt = request.forms.get('start_dt')
    stop_dt = request.forms.get('stop_dt')
    type = request.forms.get('type')
    status = request.forms.get('status')
    if pattern:
        if patterndb.contains(doc_ids=[(int(pattern))]):
            #el = patterndb.get(query.name == pattern)
                patterndb.update({'pattern.meta':meta,
                            'pattern.type':type,
                            'pattern.start_dt':start_dt,
                            'pattern.stop_dt':stop_dt,
                            'pattern.status':status
                            }, doc_ids=[int(pattern)])
        else:
               return "No pattern found with given id."

    else:
        return " Please pass Pattern to update."


@route("/pattern/edit/<pattern>",method = "get")
def editPattern(pattern):
   if pattern:
       documentId = int(pattern)
       patternItem = patterndb.contains(doc_ids=[documentId])
       print(patternItem)
       item = patterndb.get(doc_id=documentId)
       # check if profile id exists
       if patternItem:
           return template('pattern', meta = item['pattern.meta'],
                           type = item['pattern.type'],
                           sequence = item['pattern.sequence'],
                           status = item['pattern.status'],
                           start_dt = item['pattern.start_dt'],
                           stop_dt = item['pattern.stop_dt']
            )

       else:
           return 'No Profile found with given ID. Please refresh the page.'
   else:
       return 'Profile need to be passed'




@route("/profile/edit/<profile>",method = "get")
def editProfile(profile):
   if profile:
       documentId = int(profile)
       profileItem = profiledb.contains(doc_ids=[documentId])
       print(profileItem)
       item = profiledb.get(doc_id=documentId)
       # check if profile id exists
       if profileItem:
           return template('profile', meta = item['profile.meta'],
                           type = item['profile.type'],
                           direction = item['profile.direction'],
                           interval = item['profile.interval'],
                           stopCheck = item['profile.stopCheck'],
                           shallowWindow = item['profile.shallowWindow'],
                           shallowDepth = item['profile.shallowDepth'],
                           deepDepth = item['profile.deepDepth'],
                           deepWindow = item['profile.deepWindow'],
                           rampTime = item['profile.rampTime'],
                           maxTime = item['profile.maxTime'],
                           backtrackTimes = item['profile.backtrackTimes'],
                           stallTimeout = item['profile.stallTimeout'],
                           ctdWrapupTime = item['profile.ctdWrapupTime'],
                           backtrackCount = item['profile.backtrackCount'],
                           dpdt = item['profile.dpdt']
            )

       else:
           return 'No Profile found with given ID. Please refresh the page.'
   else:
       return 'Profile need to be passed'


@route("/profile/edit/<profile>", method="post")
def saveProfile(profile):
    meta = request.forms.get('meta')
    print('############')
    print(meta)
    print('*************')
    print(request.path)

    # check if meta is null or not
    if profile:
        # check if meta exists
        if profiledb.contains(doc_ids=[(int(profile))]):
            # insert data
            profiledb.update({'profile.meta': request.forms.get('meta'),
                              'profile.type': request.forms.get('type'),
                              'profile.direction': request.forms.get('direction'),
                              'profile.interval': request.forms.get('interval'),
                              'profile.stopCheck': request.forms.get('stop_check'),
                              'profile.shallowWindow': request.forms.get('shallow_window'),
                              'profile.shallowDepth': request.forms.get('shallow_depth'),
                              'profile.deepDepth': request.forms.get('deep_depth'),
                              'profile.deepWindow': request.forms.get('deep_window'),
                              'profile.rampTime': request.forms.get('ramp_time'),
                              'profile.maxTime': request.forms.get('max_time'),
                              'profile.backtrackTimes': request.forms.get('backtrack_time'),
                              'profile.stallTimeout': request.forms.get('stall_timeout'),
                              'profile.ctdWrapupTime': request.forms.get('ctd_warmup_time'),
                              'profile.backtrackCount': request.forms.get('backtrack_count'),
                              'profile.dpdt': request.forms.get('dpdt_threshold')
                              },  doc_ids=[int(profile)])

            return " Profile updated successfully."

        else:
            return " Profile already exists with same profile id."

    else:
        return " Please enter profile number."


   

@route('/download/getConfig',method = 'get')
def download():
    
    downloadConfigFile(profiledb,patterndb)
    return static_file('Scheduler.cfg', root='.', download='Scheduler.cfg')
    #return static_file('Scheduler.cfg', root='.',)   

@route('/download/missionConfig', method='get')
def downloadMissionConfig():
    return static_file(CONFIG_FILE, root='.', download=CONFIG_FILE)





run(host='localhost',port=9090)