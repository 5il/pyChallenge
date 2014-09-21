import requests

page = requests.get("http://www.pythonchallenge.com/pc/def/equality.html").text

text = page.split("<!--", 1)[1]
i = 5
while( i < (len(text) - 5) ):
 if( text[i].islower() and text[i-4].islower() and text[i-3].isupper() and text[i-2].isupper() and text[i-1].isupper() and text[i+1].isupper() and text[i+2].isupper() and text[i+3].isupper() and text[i+4].islower() ):
  print text[i],
 i += 1
