#Reading the String which You want
print ("Enter Password which must contain atleast 8 characters with min 1 Cap letter, min 1 small letter, min 1 Special Character and min 1 digit Otherwise Your password is Invalid")
s=raw_input("Enter the Password:")
dict={'cap':('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z') , 'small':('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z') , 'digits':('0','1','2','3','4','5','6','7','8','9') , 'special':('!','@','#','$','%','^','&','*')}
LowerCaseCount=0
UpperCaseCount=0
SpecialCharCount=0
DigitCount=0
stringlength=len(s)
if stringlength==8:
   for i in s:
       if i in dict['small']:
           LowerCaseCount=LowerCaseCount+1
       elif i in dict['digits']:
           DigitCount=DigitCount+1
       elif i in dict['cap']:
           UpperCaseCount=UpperCaseCount+1
       else:
           SpecialCharCount=SpecialCharCount+1
   if LowerCaseCount==0  or UpperCaseCount==0  or SpecialCharCount==0  or DigitCount==0:
       print ("please Enter valid Password")
       exit()
   else:
       print ("Valid Password")
else:
   print ("password must have atleast 8 characters")
   exit()

