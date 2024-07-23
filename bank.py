class Account:
    
    def __init__(self,bel,acc):
        self.balance = bel
        self.account_no = acc
     
    #Debit method
    def debit(self , ammount):
        self.balance -= ammount
        print("Rs",ammount,"debited from your account")
        print("Your Total balance is ", self.get_balance() ,"Rs")
    #Credit method    
    def credit(self , ammount):
        self.balance += ammount
        print("Rs",ammount,"credited to your account") 
        print("Your Total balance is ", self.get_balance() ,"Rs")       
     
    def get_balance(self):
        return self.balance 
 

acc1 = Account(10000, 12)
acc1.debit(200) 
acc1.credit(20000) 
acc1.debit(3000)
acc1.credit(5000)   