# This assumes "rare characters" are alphabetic based off
#    previous experience with this challenge

import httplib

httpHandle = httplib.HTTPConnection("www.pythonchallenge.com")
httpHandle.request("GET", "/pc/def/ocr.html")
response = httpHandle.getresponse()
page = response.read()

for char in page.split("%%", 1)[1]:
 if char.isalnum():
  print char,
