from collections import OrderedDict

def readProperties():
   separator = "="
   keys = OrderedDict()

   with open('prf_mission.cfg') as f:

    for line in f:
        if separator in line:

            # Find the name and value by splitting the string
            name, value = line.split(separator, 1)

            # Assign key value pair to dict
            # strip() removes white space from the ends of strings
            keys[name.strip()] = value.split(' #', 1)[0].strip()
            

   print(keys)        
   return keys         
    
readProperties()
