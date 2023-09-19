class Customer():
    emailSuffix = "@MyBank.co.nz"

    def __init__(self, newAcct, NewFName, NewLName):
        self.CustAcct = newAcct
        self.CustFName = NewFName
        self.CustLName = NewLName
        self.CustEMail = NewFName + "." + NewLName + Customer.emailSuffix

    def setFName(self):
        newF = input("Enter NEW FIRST name: ")
        self.CustFName = newF

    def getCurrency(self):
        balCur = "${:,.2f}".format(self.CustAcct.AccBal)
        return  balCur

    def setLName(self):
        newL = input("Enter NEW LAST name: ")
        self.CustLName = newL

    def setEMail(self):
        newMail = input("Enter NEW EMAIL: ")
        self.CustEMail = newMail

    def Deposit(self, depAmt):
        self.CustAcct.AccBal += depAmt

    def Withd(self, wdrAmt):
        self.CustAcct.AccBal -= wdrAmt

    def __str__(self):
        return (f"Account Number: {self.CustAcct.AccNum}\n"
                f"Account Name  : {self.CustFName} {self.CustLName}\n"
                f"Account EMail : {self.CustEMail}\n"
                f"Account Type  : {self.CustAcct.AccType}\n"
                f"Account Balance: {self.getCurrency().AccBal}")

