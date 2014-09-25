import Image

values = Image.open("oxygen.png").getdata()

# pixelNum was found by taking the number of pixels in the file (629x95 = 59755)
#  and dividing by two since the grayscale bar starts roughly in the middle.
#  From there, pixelNum was decremented to find the start of the grayscale bar.
pixelNum = 27047
message = ""

while( values[pixelNum][0] == values[pixelNum][1] ):
	message = message + chr( values[pixelNum][0] )
	pixelNum += 7 # Gray blocks are 7px wide
	
print message
