class Manager:
    def __init__(self, name):
        self.Cust_list = ["Aby","Johns","Nikhil"]
        self.Prem_Cust_list = ["Joseph", "Jiss","Johns"]
        self.name = name
class Clerk(Manager):
    def check_acc_status(self):
        if self.name in self.Cust_list:
            print(f"{self.name} account exists")
        else:
            print(f"{self.name} account doesn't exists")
    def check_eligibility(self):
        if self.name in self.Prem_Cust_list:
            print(f"{self.name} is eligible to apply for loans")
class Customer(Clerk):
    def __init__(self):
        name = input("Enter your name: ")
        Manager.__init__(self,name)
        

c= Customer()
c.check_acc_status()
c.check_eligibility()
