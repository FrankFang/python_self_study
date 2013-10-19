__metaclass__ = type

import sys
from sys import argv

script, from_file, to_file = argv
print ("Copying from %s to %s" %(from_file, to_file))

in_file = open(from_file)
in_data = in_file.read()

open(to_file,'w').write(in_data)
in_file.close()

sys.exit()
