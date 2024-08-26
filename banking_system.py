import random
all_account=[]
acc_numbers=[]

valid_digits=['0','1','2','3','4','5','6','7','8','9']
class Bank_account :
    def __init__(self,acc_no,holder,balance,other_details) :
        self.acc_no=acc_no
        self.holder=holder
        self.balance=balance
        self.aadhar=other_details[0]
        self.pan=other_details[1]
        self.phone_num=other_details[2]


    def deposit(self,amount):
        self.balance+=amount 
        print(amount,"has been credited")
        print("Your Current Balance is : ",self.balance)
    
    def withdrawl(self,amount):
        self.balance-=amount
        print(amount," has been credited")
        print("Your Current Balance is : ",self.balance)
    
    def check_balance(self):
        print("Your Current Balance is :  ",self.balance)


class Savings_account(Bank_account):
    def __init__(self,acc_no,holder,balance,other_details,interest_rate=0.30 ,):
        super().__init__(acc_no,holder,balance,other_details)
        self.interest_rate=interest_rate

    def add_interest(self):
        interest=self.balance*self.interest_rate
        self.balance+=interest
        

class Business_account(Bank_account):
    def __init__(self,acc_no,holder,balance,other_details,interest_rate=0.10 ):
        super().__init__(acc_no,holder,balance,other_details)
        self.interest_rate=interest_rate

    def add_interest(self):
        interest=self.balance*self.interest_rate
        self.balance+=interest

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

def aadhar_validation(number):
    leng_check=(len(number)==12)
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

def create_account(name,other_details):
    amount=int(input("Deposit a initial amount"))
    accnumber = str(random.randint(10**9, 10**10 - 1))
    while accnumber in all_account:
        accnumber=str(random.randint(10**9, 10**10 - 1))

    typeof=input("type of account you need:\n 1)savings \n 2)business")
    if(typeof=='1'):
        account=Savings_account(accnumber,name,amount,other_details)
        all_account.append(account)
        print("account creation successful")
        print("the ccount holder_name: ",account.holder)
        print("the account number: ",account.acc_no)
        all_account.append(account.acc_no)
    else:
        account=Business_account(accnumber,name,amount,other_details)
        all_account.append(account)
        print("account creation successful\n")
        print("the account number: ",account.acc_no)
        print("the ccount holder_name: ",account.holder)
        all_account.append(account.acc_no)

        
def main():
    
    print("*****WELCOME TO XYZ BANK***** \n \n")
    print("1)NEW USER\n2)EXISTING USER\n")
    response=int(input("the type of user 1 or 2"))
    if response==1:
        print("\n\nwelcome xyz bank where safety meets trust\n\n")
        holder_name=input("Enter your full name")
        phone_num=input("enter your phone number")
        numcheck=num_validation(phone_num)
        while numcheck==False:
            phone_num=input("enter a valid phone number:\t")
            numcheck=num_validation(phone_num)
        other_details=[]
        adh=input("ENTER YOUR AADHAR NUMBER:\n")
        adh_check=aadhar_validation(adh)
        while adh_check==False:
            adh=input("enter a valid aadhar number:\t")
            adh_check=num_validation(phone_num)
        pan=input("enter your pan number :\n")
        phone=int(phone_num)
        aadhar_num=int(adh)
        other_details.append(aadhar_num)
        other_details.append(pan)
        other_details.append(phone)
        create_account(holder_name,other_details)
            

main()