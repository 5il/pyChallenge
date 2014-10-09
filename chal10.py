import sys

currentString = '1'
r = 1
rounds = int( sys.argv[1] )

while( r <= rounds ):
	index = counter = 0
	currentNum = '0'
	nextString = ''
	while( index < len( currentString ) ):
		if( currentNum == currentString[index] ):
			counter += 1
		else:
			if( counter != 0):
				nextString = nextString + str( counter ) + currentNum
			counter = 1
			currentNum = currentString[index]
		index += 1
	
	nextString = nextString + str( counter ) + currentNum
	print nextString
	currentString = nextString
	
	r += 1
	
print len(nextString)
