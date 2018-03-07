from bottle import route,run,template
import ConfigParser

config = ConfigParser.RawConfigParser()
#from readCfg import readProperties


@route("/")
def index():
    return template('viewConfig') 

@route("/",method="post")
def index():
    # Writing our configuration file to 'example.cfg'
    with open('prf_mission.cfg', 'r+') as configfile:
       config.set('supervisor.gps_interval', '15')          
       config.write(configfile)
    
    return template('viewConfig') 


@route("/editConfig")
def index():
    return template('editConfig', message= 'Please check once before saving.') 


run(host='localhost',port=9090)





