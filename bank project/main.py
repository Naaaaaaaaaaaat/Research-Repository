

#--------Menu Loader-------------------------------------------
def menuLoad(menu):
    count = 1

    for z in menu:
        print(f"{count}. {z}")
        count += 1

    print(f"0. RETURN")

    choice = input("Enter Number:")

    if choice.isnumeric():
        choice = int(choice)
        if choice in range (0, count):
            Back = choice

        else:
            print("Put the number in a valid range")
            Back = 99

    else:
        print("Put in a valid number")
        Back = 99

    return Back

#----------------------------------------------------------------

def custFind():
    found = 0

    print("------------FIND CUSTOMER------------")
    findMenu = ["By NAME", "By NUMBER"]
    selection = menuLoad(findMenu)

    if selection == 1:
        findFname = input("Enter FIRST name: ").lower()
        findLname = input("Enter LAST name: ").lower()

        found = 0
        for x in custList:
            if x.CustFName.lower() == findFname and x.CustLName.lower() == findLname:
                found = x
            print("Customer FOUND")
            break

    elif selection == 2:
        findAccNum = input("Enter ACCOUNT number: ")
        if findAccNum.isnumeric():
            findAccNum = int(findAccNum)

        for y in custList:
            if y.CustAcct.AccNum == findAccNum:
                found = y

    return found


#-------Cust Edit Menu
def custEdit():
    fileEdit = custFind()

    if fileEdit != 0:
        editMenu = ["FIRST NAME", "LAST NAME", "EMAIL", "ACCOUNT TYPE"]
        editPick = menuLoad(editMenu)

        if editPick == 1:
            fileEdit.setFName()
        elif editPick == 2:
            fileEdit.setLName()
        elif editPick == 3:
            fileEdit.setEMail()
        elif editPick == 4:
            fileEdit.CustAcct.SetType()
        else:
            print("Error")
#-------Add cust
#def custAdd


from Account import acct
from Customers import Customer
custList = []

dat01 = Customer(acct("Savings"), "Kylie", "Mackay")
dat02 = Customer(acct("Cheque"), "Donna", "Underwood")
dat03 = Customer(acct("Business"), "Anthony", "Hudson")

custList.extend([dat01, dat02, dat03])

menu1 = ["DEPOSIT", "WITHDRAW", "CUSTOMER MENU"]
menu2 = ["FIND CUSTOMER", "ADD CUSTOMER", "EDIT CUSTOMER", "SHOW ALL"]

while True:
    choice1 = menuLoad(menu1)

    if choice1 == 0:
        print("Goodbye")
        break

    elif choice1 == 1:
        depositFind = custFind()


        if depositFind != 0:
            print(f"Current Balance: {depositFind.getCurrency()}")
            depAmount = input("ENTER DEPOSIT AMOUNT: ")
            if depAmount.isnumeric():
                depAmount = float(depAmount)
                depositFind.Deposit(depAmount)
                print(f"New Balance: {depositFind.getCurrency()}")
            else:
                print("Please enter a valid number")

    elif choice1 == 2:
        withdrawFind = custFind()

        if withdrawFind != 0:
            CurrentBal = withdrawFind.getCurrency()
            print(f"Current Balance: {CurrentBal}")
            WithAmount = input("ENTER WITHDRAW AMOUNT: ")
            if WithAmount.isnumeric():
                WithAmount = float(WithAmount)
                if WithAmount > CurrentBal:
                    print("Insufficient Funds.")

                else:
                    withdrawFind.Withd(WithAmount)
                    print(f"New Balance: {withdrawFind.getCurrency()}")
            else:
                print("Please enter a valid number")

    elif choice1 == 3:

        choice2 = menuLoad(menu2)
        if choice2 == 1:
            found = custFind()

            if found != 0:
                print(found)
            else:
                print("Customer NOT FOUND")
                continue

        elif choice2 == 2:
            print("add function here")

        elif choice2 == 3:
            custEdit()

        elif choice2 == 4:
            for x in custList:
                print(x)

        else:
            continue
            
    else:
        continue
