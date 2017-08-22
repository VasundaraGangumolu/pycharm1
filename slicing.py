#Reading the String which You want
s=raw_input("Enter the String:")
LowerCaseCount=0
UpperCaseCount=0
SpecialCharCount=0
DigitCount=0
lowerCaseletters=""
UpperCaseletters=""
SpecialCharletters=""
Digitcharletters=""
for i in s:
   if i.islower():
       #print (i)
       lowerCaseletters=lowerCaseletters+i
       LowerCaseCount=LowerCaseCount+1
   elif i.isdigit():
       Digitcharletters=Digitcharletters+i
       DigitCount=DigitCount+1
   elif i.isupper():
       UpperCaseletters=UpperCaseletters+i
       UpperCaseCount=UpperCaseCount+1
   else:
       SpecialCharletters=SpecialCharletters+i
       SpecialCharCount=SpecialCharCount+1
print ("lowerCase Letters Count:%d              lowercase letters:%s" %(LowerCaseCount,lowerCaseletters))
print ("upperCase Letters Count:%d                uppercase letters:%s" %(UpperCaseCount,UpperCaseletters))
print ("digits Count:%d                  digits:%s" %(DigitCount,Digitcharletters))
print ("specialChar Count:%d             special Characters:%s" %(SpecialCharCount,SpecialCharletters))