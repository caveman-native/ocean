from collections import OrderedDict
from constants import *

def readProperties():
   keys = OrderedDict()
   with open(CONFIG_FILE) as f:
      try:
         for line in f:
           if SEPARATOR in line:
             # Find the name and value by splitting the string
             name, value = line.split(SEPARATOR, 1)
             # Assign key value pair to dict
             # strip() removes white space from the ends of strings
             keys[name.strip()] = value.split(COMMENT, 1)[0].strip()
      finally:
          if f is not None:
             f.close()
   #print(keys)        
   return keys

   
def getProperties(prefix):
   keys = OrderedDict()
   with open(CONFIG_FILE) as f:
       try:
           for line in f:
               if SEPARATOR in line and line.startswith(prefix):
                   name, value = line.split(SEPARATOR,1)
                   keys[name.strip()] = value.split(COMMENT,1)[0].strip()
               elif not prefix:
                   name, value = line.split(SEPARATOR,1)
                   keys[name.strip()] = value.split(COMMENT,1)[0].strip()
       finally:
           if f is not None:
               f.close()
   return keys   
   
readProperties()
