# Need to make this less sloppy...

import re
import urllib
import sys

f = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+sys.argv[1])
n = re.search("(and the next nothing is )(\d+)", f.read())
print n.group(0)
while n:
 f = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+n.group(2))
 n = re.search("(and the next nothing is )(\d+)", f.read())
 print n.group(0)
