import re
list=[{"FirstName":"vasundara","LastName":"devi","contact":"7075238685","Email":"vasundara@gmail.com"},{"FirstName":"gangumolu","LastName":"vasu","contact":"7386218379","Email":"vasu@gmail.com"}]
def options():
    print ("Please select one of the following: ")
    print ("1. Search (User can enter Email/FirstName/ LastName)")
    print ("2. Add a contact (should throw error if user tries to enter duplicate contacts)")
    print("3. Remove a contact")
    print ("4. Exit")
    option = int(raw_input("Enter your option: "))
    if option==1:
       search()
    elif option==2:
       signup()
    elif option==3:
        remove()
    else:
        exit()
def search():
    try:
        name = raw_input("Enter your Firstname/contact/Email: ")
        # for name in dict['First Name'] or dict['Last Name'] or dict['contact']
        if len(list) == 0:
            print "no contact to Search"
        try:
            index=next(index for index,d in enumerate(list) if d['FirstName'] == name or ['LastName'] == name or d['Email'] == name)
            print list[index]
        except (StopIteration,Exception) as e:
            print "You entered wrong information or No such Record for given Information."
        options()
    except Exception as e:
        print (e)
def remove():
    try:
        name = raw_input("Enter your Firstname/contact/Email: ")
        if len(list)==0:
            print "no Conatct to remove"
        try:
            index = next(index for index, d in enumerate(list) if d['FirstName'] == name or ['LastName'] == name or d['Email'] == name)
            del list[index]
            print "Record is Deleted"
        except (StopIteration,Exception) as e:
            print "You entered wrong information or No such Record for given Information"
        options()
    except Exception as e:
        print (e)
def signup():
    FirstName = raw_input("Enter your FirstName: ")
    LastName = raw_input("Enter  your LastName")
    contact = raw_input("Enter your contact number")
    Email =raw_input("Enter Email-Id")
    details={'FirstName':FirstName,'LastName':LastName,'contact':contact,"Email":Email}
    if not any((d['Email']==details['Email'] or  (d['FirstName']==details['FirstName'] and
                        ['LastName'] == details['LastName'])) for d in list ):
        if (len(contact) == 10 and re.match(r'[789]\d{9}$', contact) and re.match(r'^.*@.*.com$',Email)):
                list.append(details)
                print ("details added")
                print list
        else:
            if  LastName.isdigit():
                print "Name must contain only characters"
                print "please enter correct Details again"
                signup()
            if contact.isalpha() or contact.isupper() or contact.islower():
                print "contact must contain numbers only"
                print "please enter correct Details again"
                signup()
            if len(contact) < 10 and contact.isdigit():
                print "contact must be digits and exactly 10 number"
                print "please enter correct Details again"
                signup()
            if not re.match(r'^.*@.*.com$',Email):
                print ("Please provide proper format of Email")
                print "please enter correct Details again"
                signup()
    else:
        print ("contact already exists")
        print ("please enter details again")
        signup()
    options()
options()
