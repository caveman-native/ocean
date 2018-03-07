import tempfile,os

separator = "="

def replace_key(filename, key, value):
    with open(filename, 'rU') as f_in, tempfile.NamedTemporaryFile(
            'w', dir=os.path.dirname(filename), delete=False) as f_out:
        for line in f_in.readlines():
            if line.startswith(key):
                # Find the name and value by splitting the string
                name,textVal  = line.split(separator, 1)
                updatedTxt = textVal.replace( textVal.split(' #', 1)[0], value)
               
                line = '='.join((line.split('=')[0], ' {}'.format(updatedTxt)))
            f_out.write(line)

    # remove old version
    os.unlink(filename)

    # rename new version
    os.rename(f_out.name, filename)


replace_key('file.cfg','key1','value2')
