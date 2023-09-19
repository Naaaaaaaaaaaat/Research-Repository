# -------------------->>>>> ADD New Contacts <<<<<--------------------
def addContact():
    newFName = input("Enter FIRST name: ")
    newLName = input("Enter LAST name:  ")
    newAddr = input("Enter ADDRESS:    ")
    newCity = input("Enter CITY:       ")
    newDist = input("Enter DISTRICT:   ")
    newPhone = input("Enter PHONE:      ")
    newDat = Contact(newFName, newLName, newAddr, newCity, newDist, newPhone)
    pBook.append(newDat)
    print(pBook[len(pBook) - 1])
    print("Contact Saved.")


# -------------------->>>>>   FIND Contact   <<<<<--------------------
def findContact():
    newFName = input("Enter FIRST name: ")
    newLName = input("Enter LAST name : ")


found = 0

for x in pBook:
    if x.FName == newFName and x.LName == newLName:
        found = x
        break

return found

""" 
#-------------------->>>>>   EDIT Contact   <<<<<-------------------- 
def editContact(): 


#-------------------->>>>> DELETE Contact <<<<<-------------------- 
def deleteContact(): 

"""

# -------------------->>>>>  MAIN  PROGRAM  <<<<<--------------------

from Contacts import Contact

pBook = []
# -------------------->>>>> Create Contacts <<<<<--------------------
dat11 = Contact("Harry", "Abraham", "8a Feltham Street", "Timaru", "Canterbury", "(020) 403 6704")
dat12 = Contact("Simon", "Brown", "75 Scott Street", "Blenheim", "Marlborough", "(027) 185 9643")
dat13 = Contact("Paul", "Abraham", "22 Tennyson Street", "Napier", "Hawke's Bay", "(029) 061 5554")
dat14 = Contact("Jonathan", "North", "41a Union Road", "Pukekohe", "Auckland", "(020) 632 1503")
dat15 = Contact("Theresa", "Morgan", "33a Waiouru Crescent", "Lower Hutt", "Wellington", "(021) 393 7110")
# -------------------->>>>> Load Phone Book <<<<<--------------------
pBook.append(dat11)
pBook.append(dat12)
pBook.append(dat13)
pBook.append(dat14)
pBook.append(dat15)
# -------------------->>>>>  WORKING  AREA  <<<<<--------------------

while True:
    print("\n---------->>>>> Phonebook Application <<<<<----------")
    print("\nEnter Selection Number")
    print(f"1. FIND Contact\n"
          f"2. ADD Contact\n"
          f"3. PRINT ALL Contacts\n"
          f"0. EXIT")
    choice1 = int(input("Enter Selection: "))

if choice1 == 0:
    print("\nGoodbye.")
    break

elif choice1 == 1:
    outcome = findContact()
    if outcome != 0:
        print(outcome)
    else:
        print("\nContact Not Found.")

elif choice1 == 2:
    addContact()

elif choice1 == 3:
    for x in pBook:
        print(x)

else:
    print("Number out of Range")
    continue