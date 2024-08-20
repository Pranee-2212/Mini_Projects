contacts=[]
phone_book=[]
temp=[]
temp_loc=0

valid_digits=['0','1','2','3','4','5','6','7','8','9']

def create_contact(name,number,email):
    i=[name,number,email]
    j={'name':name,'number':number,'email':email}
    contacts.append(i)
    phone_book.append(j)
    print("contact created")

def display():
    print(contacts)

def search():
    search_based =input("search using name or number: ")
    
    if(search_based[0] not in valid_digits):
        #element=input("enter the name to be searched: ")
        serch=search_based.upper()
        for i in range(0,len(contacts)):
            if contacts[i][0]==serch :
                print("CONTACT_FOUND")
                print(contacts[i])
                temp=contacts[i]
                return temp
                
               
                
    elif(search_based[0] in valid_digits):
        value=int(search_based)
        #element=input("enter the number to be searched: ")
        for i in range(0,len(contacts)):
            if contacts[i][1]==value :
                print("CONTACT_FOUND")
                print(contacts[i])
                temp=contacts[i]
                return temp
    else:
        print("enter a vlaid value")
        search()


def num_validation(number):
    leng_check=(len(number)==10)
    digi_check=True

    for i in number :
        if i in valid_digits :
            digi_check=True
        else:
           digi_check=False
           break
    if(leng_check and digi_check):
        return True
    else:
        return False

def Update():
    data=search()
    index=contacts.index(data)
    
    up_type=input("what do you need to update: ")
    if up_type=='name':
        nn=input("Enter the new name: ")
        new_value=nn.upper()
        contacts[index][0]=new_value

    elif up_type=='number':
        nn=input("Enter the new number: ")
        new_value=int(nn)
        ver=num_validation(new_value)
        if ver==True:
            contacts[index][1]=new_value
        else:
            new_value=int(input("enter a proper number"))

    else:
        new_value=input("enter the email : ")
        contacts[index][2]=new_value

    print('')

def delete_contact():
    search()
    print("Deleting Contact....")
    del contacts[temp_loc]
    print("Contact Deleted")
    print("Updated List: \n")
    display()

def main(): 
    
    while True:
        print(".........THE CONTACT BOOK APPLICATION .......")
        print("1.Create a contact \n 2.find a contact \n 3.Update a contact \n 4.Delete a contact \n 5.Display the contacts \n 6.to exit(close the program)") 
        ch=int(input())
        if(ch==6):
            break 

        elif ch==1:
            name=input("enter the name of the contact:")
            if name=='':
               print("name cannot be empty")
               name=input()
            name=name.upper()
            num=input("enter the mobile number(10 numbers): ")
            num_check=num_validation(num)
            if(num_check==False):
                print("Enter a valid number")
                num=input()
            number=int(num)
            
            email=input("Enter the email:")
            create_contact(name,number,email)
        elif ch==2:
            search()
            temp=[]
            temp_loc=0
        elif ch==3:
           Update()

        elif ch==4:
            delete_contact() 
        elif ch==5:
            display()
        else:
            print("enter a valid iniput()")



main()
