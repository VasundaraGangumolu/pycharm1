dict=[{'FirstName':'vasundara','LastName':'devi','contact':'7386218379'}]
def search():
    name=raw_input("Enter your name/contact: ")
    #for name in dict['First Name'] or dict['Last Name'] or dict['contact']
    for i in dict:
        if name in i.values():
            print ('{}:{}'.format(i.keys(),i.values()))
            #print('{} : {}'.format(attribute, value))
    else:
     print "You entered wrong information."
    select()
def add():
        contact=raw_input("Enter your contact number")
        FirstName=raw_input("Enter your FirstName: ")
        LastName=raw_input("Enter  your LastName")
        print contact
        if (len(contact)<10) and (contact.startswith('9') or contact.startswith('8') or contact.startswith('7')):
             print ("contact number should have 10 numbers")
             add()
        for i in dict:
            if (FirstName,LastName) in (i['FirstName'],i['LastName']):
                print ("Name already exist please select another name")
                add()
            else:
                dict.append({'FirstName': FirstName, 'LastName': LastName, 'contact': contact})
                #print dict
def dele():
    delet=int(raw_input("Remove a contact: "))
    if any(dict['FirstName']==delet or dict['LastName']==delet or dict['contact']==delet):
      # if delet.isalpha():
                #dict.remove(delet)
            del dict[delet]
            print "deleted"
    else:
        print "contact doesn't exist's"
#def exit():
 #   exit()
def select():
 print ("Please select one of the following: ")
 print ("1. Search (User can enter Phone number/First  Name/ Last Name)")
 print ("2. Add a contact (should throw error if user tries to enter duplicate contacts)")
 print("3. Remove a contact")
 print ("4. Exit")
 s=int(raw_input("Enter your option: "))
 if s==1:
           search()
 elif s==2:
           add()
 elif s==3:
           dele()
 else:
        s==4
        exit()
 select()
select()