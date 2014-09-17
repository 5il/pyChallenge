import string

encrypted = raw_input("Enter string: ")

print string.translate(encrypted, string.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"))

