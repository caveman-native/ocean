from bottle import route,run,template,request,static_file
from readCfg import readProperties,getProperties
from updateKey import replace_key
from constants import *
from tinydb import TinyDB,Query
import json
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
    return template('viewConfig')


@route("/test",method = "get")
def index():
    return template('testConfig', supervisors = getProperties(SUPERVISOR), imm = getProperties(IMM),hosts = getProperties(HOST))

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
           profiledb.insert({'meta':request.forms.get('meta'),
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
           return "<p> Profile added successfully.</p>"               
        else:
            return "<p> Profile already exists with same description(meta). Please change the meta description(meta).</p>"   

    else:
        return "<p> Please enter profile description(meta).</p>"

@route("/createPattern",method = "get")
def createPattern():

   return '''<form id="create-pattern-form" action='/createPattern' method='post'>
    Meta: <input id="meta" name="meta" type="text" maxlength="200" required/>
    Start Date: <input id="start-date" name="start_dt" type="date" min="2018-04-01" max="2020-04-30" />
    End Date: <input id="end-dt" name="end_dt" type="date" min="2018-04-01" max="2021-04-30" />
    Type: <input id="type" name="type" type="number" min="0" max= "2"/>
    Status: <input id="status" name="status" type="number" min="0" max= "1"/>
    <input id="pattern-submit" value="Create Pattern" type="submit" /> </form>'''


@route("/createPattern",method = "post")
def createPattern():
    meta = request.forms.get('meta')
    start_dt = request.forms.get('start_dt')
    end_dt = request.forms.get('end_dt')
    type = request.forms.get('type')
    status = request.forms.get('status')
    
    #check if meta is null or not
    if meta:
        #check if meta exists 
        if not patterndb.search(query.meta == meta):
           #insert data
           patterndb.insert({'meta':meta,
                            'type':type,
                            'start_dt':start_dt,
                            'end_dt':end_dt,
                            'status':status
                           })
           return "<p> Pattern added successfully.</p>"               
        else:
            return "<p> Pattern already exists with same description. Please change the meta description.</p>"   

    else:
        return "<p> Please enter pattern description.</p>"




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
            return '<p>Pattern with ' + key + ' removed successfully </p>'     
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
            return '<p>Profile with' + key +'removed successfully </p>'     
        else:
            return '<p>No value found with passed document id.</p>'     
    else:
        return '<p>Please pass document id to delete the element.</p>' 





@route("/updatePattern/<pattern>",method = "post")
def updatePattern(pattern):

    meta = request.forms.get('meta')
    start_dt = request.forms.get('start_dt')
    end_dt = request.forms.get('end_dt')
    type = request.forms.get('type')
    status = request.forms.get('status')

   #check if meta is null or not
    if pattern:
        if patterndb.search(query.meta == pattern):
            #el = patterndb.get(query.name == pattern)
            if meta:
                patterndb.upsert({'meta':meta,
                            'type':type,
                            'start_dt':start_dt,
                            'end_dt':end_dt,
                            'status':status
                           }, query.meta == meta)
            else:
               return "<p>Meta description is mandatory.</p>"         
        else:
            return "<p>Sorry, no record found, please check the pattern.</p>"    

    else:
        return "<p> Please pass Pattern to update.</p>"



@route("/editProfile",method = "get")
def profiles():
   
   return('Hello')


run(host='localhost',port=9090)