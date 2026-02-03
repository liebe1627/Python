class BackAccount:

    ROT = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Name of the Account holder: ",self.Name)
        print("Current Balance: ",self.Amount)
    
    def Deposit(self):
        No = float(input("Enter the amount to deposite: "))
        print("Total balance is: ",No+self.Amount)

    def Withdraw(self):
        No = float(input("Enter the amount of withdraw: "))
        print("Balance remanaing: ",self.Amount-No)

    def CalculateInterest(self):
        Interest = (self.Amount * BackAccount.ROT/100)
        print("Interest is: ",Interest)

obj1 = BackAccount("Samantha",100000)
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateInterest()