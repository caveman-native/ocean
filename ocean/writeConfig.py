import io
import tempfile,os
import json
from tinydb import TinyDB,Query
import fileinput


patterndb = TinyDB('pattern.json') 
profiledb = TinyDB('profile.json')

filename = 'Scheduler.cfg'
equalsTO = '='
replaceText = '#-------------------------------------------------------------------------------'


def writeConfigFile(profiledb,patterndb):

    if os.path.exists(filename): os.remove(filename)

    with open(filename,'a') as outfile:
        outfile.write('#-------------------------------------------------------------------------------\n')
        outfile.write('# ITP schedule configuration file                                               \n')
        outfile.write('#-------------------------------------------------------------------------------\n')
        outfile.write('# Profiles List                                                                 \n')
        outfile.write('#-------------------------------------------------------------------------------\n')
        outfile.write('#-------------------------------------------------------------------------------\n')
        for profile in profiledb:
            outfile.write("\n")
            #print(profile.doc_id)
            outfile.write('#-------------------------------------------------------------------------------\n')
            outfile.write('\n  profile.start : ' + str(profile.doc_id) )
            json.dump(profile, outfile, indent=2)
            outfile.write('  profile.end  : ' + str(profile.doc_id) + '\n')
            outfile.write('#-------------------------------------------------------------------------------\n')

        outfile.write('\n#-------------------------------------------------------------------------------')
        outfile.write('\n# Patterns List                                                                 ')
        outfile.write('\n#-------------------------------------------------------------------------------')
        for pattern in patterndb:
        #json.dump(profiledb.all(), outfile, indent=2)
            outfile.write("\n")
            outfile.write('#-------------------------------------------------------------------------------\n')
            outfile.write('\n  pattern.start : ' + str(pattern.doc_id) )
            json.dump(pattern, outfile, indent=2)
            outfile.write('  pattern.end  : ' + str(pattern.doc_id) + '\n')
            outfile.write('#-------------------------------------------------------------------------------\n')
            
        
        outfile.close()
        
    
            


def updateConfigFile(filename):
    #with open(filename) as f:
       # newText=f.read().replace('}', '')
        #commentText=f.read().replace('{', replaceText)
            
    #with open(filename, "w") as f:
        #f.write(newText)
        #f.write(commentText)
        #f.close()

    with open(filename, 'U') as f:

       newText=f.read()
       while ':' in newText:
          newText=newText.replace(':', ' = ')
          
 
       while '}' in newText:
          newText=newText.replace('}', '')
 
       while '{' in newText:
          newText=newText.replace('{', '')

       while '"' in newText:
          newText=newText.replace('"', '')

       while ',' in newText:
          newText=newText.replace(',', '   ')          
 
    with open(filename, "w") as f:
       f.write(newText)    



def formatConfig(filename, equalsTO):
      
      with open(filename, 'rU') as f_in, tempfile.NamedTemporaryFile(
            'w', dir=os.path.dirname(filename), delete=False) as f_out:
         try:
               for line in f_in.readlines():
                  if equalsTO in line:
                  # Find the name and value by splitting the string
                     line.split(equalsTO)
                     print('{:25} = {}'.format(line.split(equalsTO)[0],line.split(equalsTO)[1]))
                     #print(line)
                     f_out.write('{:25} = {}'.format(line.split(equalsTO)[0],line.split(equalsTO)[1]))
                  else:
                      line = line
                      f_out.write(line)   

                
         finally:
           f_in.close()
           f_out.close()

      os.unlink(filename)

    # rename new version
      os.rename(f_out.name, filename)
             


def downloadConfigFile(profiledb,patterndb):
    writeConfigFile(profiledb,patterndb)
    updateConfigFile(filename)
    formatConfig(filename, equalsTO)



downloadConfigFile(profiledb, patterndb)