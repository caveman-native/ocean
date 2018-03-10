import tempfile,os
import fileinput
import re

separator = "="

def replace_key(filename, key, value):
      print(key)
      print(value)
      with open(filename, 'rU') as f_in, tempfile.NamedTemporaryFile(
            'w', dir=os.path.dirname(filename), delete=False) as f_out:
         try:
               for line in f_in.readlines():
                  if line.startswith(key):
                  # Find the name and value by splitting the string
                     name,textVal  = line.split(separator, 1)
                     updatedTxt = textVal.replace( textVal.split(' #', 1)[0], value)
                     line = '='.join((line.split('=')[0], ' {}'.format(updatedTxt)))
                  print(line)
                  f_out.write(line)
         finally:
           f_in.close()
           f_out.close()

    # remove old version
     # if os.path.isfile(filename+'.bak'):
     #  os.unlink(filename+'.bak')

      os.unlink(filename)

    # rename new version
      os.rename(f_out.name, filename)


def replace_key_1(filename, key, value):

  for line in fileinput.input(inplace=1, backup='.bak'):
    if line.startswith(key):
      oldVal= '' 
      name,textVal  = line.split(separator, 1)
      if ' #' not in textVal:
        oldVal=textVal
      else:
        oldVal = textVal.replace( textVal.split(' #', 1)[0], value)
      print('Changing old ', oldVal ,' to new value ', value)
      line = re.sub(oldVal,value)
      print(line)


  



replace_key('file.cfg','key1','value8')
