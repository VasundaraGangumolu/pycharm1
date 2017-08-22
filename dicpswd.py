#Reading the String which You want
print ("Enter Password which must contain atleast 8 characters with min 1 Cap letter, min 1 small letter, min 1 Special Character and min 1 digit Otherwise Your password is Invalid")
def password():
 s = raw_input("Enter the Password:")
 LowerCaseCount=UpperCaseCount=SpecialCharCount=DigitCount=0
 stringlength=len(s)
 if stringlength==8:
   for i in s:
       if i in dict['cap'].lower():
           LowerCaseCount=LowerCaseCount+1
       elif i in dict['digits']:
           DigitCount=DigitCount+1
       elif i in dict['cap']:
           UpperCaseCount=UpperCaseCount+1
       else:
           SpecialCharCount=SpecialCharCount+1
   if LowerCaseCount==0  or UpperCaseCount==0  or SpecialCharCount==0  or DigitCount==0:
       print ("please Enter valid Password")
   else:
       print "valid password"
 else:
     print "Please enter atleast 8 characters"
 return;
dict={'cap':'ABCDEFGHIJKLMNOPQRSTUVWXYZ','digits':'0123456789', 'special':('!','@','#','$','%','^','&','*')}
password()