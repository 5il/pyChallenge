import re
import requests
import sys

page = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+sys.argv[1]).text
n = re.search("(and the next nothing is )(\d+)", page)
print page
while n:
 page = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+n.group(2)).text
 n = re.search("(and the next nothing is )(\d+)", page)
 print page
