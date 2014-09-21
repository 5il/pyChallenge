for char in raw_input('Enter string: '):
 if char.isalpha():
  print chr(((ord(char) - 95 ) % 26 ) + 97 ),
 else:
  print char,
