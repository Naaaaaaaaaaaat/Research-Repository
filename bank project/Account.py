class acct():
    count = 1000000

    def __init__(self, newType):
        acct.count += 1000
        self.AccNum = acct.count
        self.AccType = newType
        self.AccBal = 0.00

    def getnum(self):
        return self.AccNum

    def getType(self):
        return self.AccType

    def setType(self):
        print(f"Current Account Type: {self.AccType}")
        print("SAVINGS", "CHEQUE", "BUSINESS")
        newType = input("ENTER NEW ACCOUNT TYPE: ")
        self.AccType = newType

    def getBal(self):
        return self.AccBal