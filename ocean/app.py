from bottle import route,run,template,request,static_file
from readCfg import readProperties,getProperties
from updateKey import replace_key
from constants import *
#config = ConfigParser.RawConfigParser()
#from readCfg import readProperties

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

#@route("/static/font/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>")
#def font(filepath):
#    return static_file(filepath, root="static/font")


@route("/")
def index():
    return template('viewConfig',
    supervisors = getProperties(SUPERVISOR),
    imm = getProperties(IMM),
    hosts = getProperties(HOST))


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
        print('No config values updated.')
    
    return template('viewConfig',
    supervisors = getProperties(SUPERVISOR),
    imm = getProperties(IMM),
    hosts = getProperties(HOST)) 


@route("/editConfig")
def index():
    return template('editConfig',
    supervisors = getProperties(SUPERVISOR),
    imm = getProperties(IMM),
    hosts = getProperties(HOST),
    message = 'Please check once before saving.')

run(host='localhost',port=9090)

if __name__ == "__main__":
    run(reloader=True)
