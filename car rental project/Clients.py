class Client():
    cIdNum = int(1000)

    cRecNum = int(100000)

    def __init__(self, newcFName, newcLName, newcPhone, newcEmail):
        self.cID = Client.cIdNum

        Client.cIdNum += 10

        self.cFName = newcFName

        self.cLName = newcLName

        self.cPhone = newcPhone

        self.cEmail = newcEmail

        self.cOwing = float(0)  # how much to pay for rental

        self.cReciepts = []  # list of all rentals for client

        self.prevRentals = []  # list of all previous vehicles

        self.currRental = None  # current rental vehicle

    def GetMoney(self):
        print("$[:,.2f}".format(self.cOwing))

    def GetVMoney(self):
        print("$[:,.2f}".format(self.cOwing))

    def setPhone(self, newPhone):
        self.cPhone = newPhone

    def setEmail(self, newEmail):
        self.cEmail = newEmail

    def __str__(self):
        return (f"Name:    {self.cFName} {self.cLName}\n"

                f"Phone:   {self.cPhone}\n"

                f"Email:   {self.cEmail}\n"

                f"Owing:   {self.cOwing}\n"

                f"Current: {self.currRental}\n")