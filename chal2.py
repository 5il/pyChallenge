# This assumes "rare characters" are alphabetic based off
#    previous experience with this challenge

import requests

page = requests.get("http://www.pythonchallenge.com/pc/def/ocr.html").text

for char in page.split("%%", 1)[1]:
 if char.isalnum():
  print char,
