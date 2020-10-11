plainText = input("ENTER THE TEXT:\n")
shift = int(input("SHIFT KEY:\n"))
cipherText = ""
for char in plainText:
  pos = ord(char)
  if 48<= pos<= 57:
    newpos = (pos-48+shift)%10+48
  elif 65<=pos<= 90:
    newpos = (pos-65+shift)%26+65
  elif 97<=pos<=122:
    newpos = (pos-97+shift)%26+97
  else:
    newpos = pos
  cipherText += chr(newpos)
print(cipherText)
