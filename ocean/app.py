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
   
   return template('createProfile')

@route("/createPattern",method = "get")
def createPattern():
   
   return '''<form action='/createPattern' method='post'>
   Meta: <input name="meta" type="text" maxlength="200" required/>
   Start Date: <input name="start_dt" type="date" min="2018-04-01" max="2020-04-30" />
   End Date: <input name="end_dt" type="date" min="2018-04-01" max="2021-04-30" />
   Type: <input name="type" type="number" min="0" max= "2"/>
   Status: <input name="status" type="number" min="0" max= "1"/>
   <input value="Create Pattern" type="submit" />
   </form>'''

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
   
   return('Hellow')


run(host='localhost',port=9090)