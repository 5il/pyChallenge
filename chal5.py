# Make sure your terminal is full screen when running this

import pickle
import requests

pickled = requests.get( "http://www.pythonchallenge.com/pc/def/banner.p" )
unpickled = pickle.loads( pickled.text )

for row in unpickled:
	line = ""
	for chunk in row:
	  line = line + ( chunk[0]*chunk[1] )
	print line+"\n"
