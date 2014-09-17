import httplib

httpHandle = httplib.HTTPConnection("www.pythonchallenge.com")
httpHandle.request("GET", "/pc/def/equality.html")
response = httpHandle.getresponse()
page = response.read()

text = page.split("<!--", 1)[1]
i = 5
while( i < (len(text) - 5) ):
 if( text[i].islower() and text[i-4].islower() and text[i-3].isupper() and text[i-2].isupper() and text[i-1].isupper() and text[i+1].isupper() and text[i+2].isupper() and text[i+3].isupper() and text[i+4].islower() ):
  print text[i],
 i += 1
