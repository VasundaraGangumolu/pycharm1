#Reading the String which You want
print ("Enter Password which must contain atleast 8 characters with min 1 Cap letter, min 1 small letter, min 1 Special Character and min 1 digit Otherwise Your password is Invalid")
s=raw_input("Enter your Password:")
LowerCaseCount=0
UpperCaseCount=0
SpecialCharCount=0
DigitCount=0
stringlength=len(s)
if stringlength==8:
  for i in s:
      if i.islower():
          LowerCaseCount=LowerCaseCount+1
      elif i.isdigit():
          DigitCount=DigitCount+1
      elif i.isupper():
          UpperCaseCount=UpperCaseCount+1
      else:
          SpecialCharCount=SpecialCharCount+1
      #print(LowerCaseCount,DigitCount,UpperCaseCount,SpecialCharCount)
  if LowerCaseCount==0  or UpperCaseCount==0  or SpecialCharCount==0  or DigitCount==0:
    print ("please Enter valid Password")
    exit()
  else:
    print ("Valid Password")
else:
  print ("password must have atleast 8 characters")
  exit()
