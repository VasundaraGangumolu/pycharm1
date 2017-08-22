#Reading the String which You want
s=raw_input("Enter the String:")
dict={'cap':('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'),'small':('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z') , 'special':('!','@','#','$','%','^','&','*')}
dict['digits']='0123456789'
LowerCaseCount=UpperCaseCount=SpecialCharCount=DigitCount=0
LowerCaseLetters=UpperCaseLetters=Digits=SpecialCharacters=""
for i in s:
   if i in dict['small']:
       LowerCaseLetters+=i
       LowerCaseCount += 1
   elif i in dict['digits']:
       Digits+=i
       DigitCount+=1
   elif i in dict['cap']:
       UpperCaseLetters+=i
       UpperCaseCount+=1
   else:
       SpecialCharacters+=i
       SpecialCharCount+=1
print ("lowerCase Letters Count:%d              lowercase letters:%s" %(LowerCaseCount,LowerCaseLetters))
print ("upperCase Letters Count:%d                uppercase letters:%s" %(UpperCaseCount,UpperCaseLetters))
print ("digits Count:%d                  digits:%s" %(DigitCount,Digits))
print ("specialChar Count:%d             special Characters:%s" %(SpecialCharCount,SpecialCharacters))