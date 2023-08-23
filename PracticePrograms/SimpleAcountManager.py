class Account():
    def __init__(self,name, num,amt):
        self.name = name
        self.num = num
        self.amt = amt

    def Deposit(self):
        print("Deposit")
        amt = int(input("Enter the amount to be deposited:"))
        self.amt = self.amt + amt
        print("The current balance after deposit is ",self.amt)

    def Withdraw(self):
            amt = int(input("Enter the amount withdrawed: "))
            self.amt = self.amt - amt
            if self.amt <0:
                print("Insufficent Balance.")
            else:
                print("The current balance after withdraw ",self.amt)

    def check_balance(self):
        print("Check your balance")

    def acc_details(self):
        print("Account Details")
        print("Name: ",self.name, "\nAccount Number: ",self.num)
        
print()
print("Welcome to Personalized Account Manager")
name = input("Enter the account holders name: ")
num = int(input("Enter the account number: "))
amt = int(input("Enter your current balance: "))
p1 = Account(name,num,amt)
print("Your account details: ")
p1.acc_details()
while True:
    print("Enter a choice")
    print("Click 1 to Deposit Amount"+ "\nClick 2 to Withdraw the money" + "\nClick 3 to Quit")
    ch = 0
    ch = int(input("Enter your choice: "))
    if ch == 1:
        p1.Deposit()
    elif ch ==2:
        p1.Withdraw()
    else:
        break
