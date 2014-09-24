import zipfile
import re

archive = zipfile.ZipFile("channel.zip")
number = re.search( "Next nothing is (\d+)", archive.read("90052.txt") )
message = ""

while number:
	message = message + archive.getinfo(number.group(1)+".txt").comment
	number = re.search( "Next nothing is (\d+)", archive.read(number.group(1)+".txt") )

print message
