encrypted = raw_input('Enter string: ')
for char in encrypted:
 if char.isalpha():
  print chr((((ord(char) + 2) - 97 ) % 26 ) + 97 ),
 else:
  print char,
