class Contact:

    def __init__(self, newFName, newLName, newAddr, newCity, newDist, newPhone):
        self.FName = newFName
        self.LName = newLName
        self.Addr = newAddr
        self.City = newCity
        self.Dist = newDist
        self.Phone = newPhone

    def setFName(self):
        otherFName = input("Enter NEW FIRST Name: ")
        self.FName = otherFName

    def getFName(self):
        return self.FName

    def setLName(self):
        otherLName = input("Enter NEW LAST Name: ")
        self.LName = otherLName

    def setAddr(self):
        otherAddr = input("Enter NEW ADDRESS: ")
        self.Addr = otherAddr

    def setCity(self):
        otherCity = input("Enter NEW CITY: ")
        self.City = otherCity

    def setDist(self):
        otherDist = input("Enter NEW DISTRICT: ")
        self.Dist = otherDist

    def setPhone(self):
        otherPhone = input("Enter NEW PHONE: ")
        self.Phone = otherPhone

    def __str__(self):
        return (f"\nFirst Name: {self.FName}\n"
                f"Last Name:  {self.LName}\n"
                f"Address:    {self.Addr}\n"
                f"City:       {self.City}\n"
                f"District:   {self.Dist}\n"
                f"Phone:      {self.Phone}")