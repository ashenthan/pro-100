class ATM(object):
    def __init__(self, cardnumber, pinnumber, initbalance):
        self.cardnumber=cardnumber
        self.pinnumber=pinnumber
        self.initbalance=initbalance
    
    def cashwithdrawl(self):
        print("cash withdrawn")
    def balanceenquiry(self):
        print("balance is",self.initbalance)

account1=ATM("3215", "7767", 9904)
print(account1.cardnumber)
account1.balanceenquiry()