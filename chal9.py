# Need to clean this up, but it works...

import re, requests, turtle

source = requests.get("http://www.pythonchallenge.com/pc/return/good.html", auth=("huge", "file")).text

# So messy...
first = re.search("first:\W([\d,\n]+)", source).group(1).replace("\n", "").split(",")
second = re.search("second:\W([\d,\n]+)", source).group(1).replace("\n", "").split(",")

turtle.setup(640, 480)
turtle.up()

counter = 0

while( counter < len(first) ):
	turtle.goto( int(first[counter]) - 100, int(first[counter+1]) - 100 )
	turtle.down()
	counter += 2
	
turtle.up()
counter = 0

while( counter < len(first) ):
	turtle.goto( int(first[counter]) - 100, int(first[counter+1]) - 100 )
	turtle.down()
	counter += 2
