def calculate(item_list, item_find):
    item_price = float(item_list[item_find + 1])
    item_amount = int(input(f"How many {item_list[item_find]} do you want: "))
    item_cost = item_price * item_amount
    items = item_list[item_find] + "(" + str(item_amount) + ")"
    cartitems.append(item_list[item_find])
    return item_cost

fruit = ["bananas", 2.00, "avocados", 1.50, "oranges", 1.50, "apples", 2.00, "kiwis", 1.50]
vege = ["onions", 2.50, "cucumbers", 5.25, "potatoes", 3.50, "lettuce heads", 4.50, "salad mixes", 4.00]
deli = ["ham", 4.00, "salmon", 8.00, "sausages", 8.00, "salami", 5.50, "mussels", 8.00]

cartprice = 0
cartitems = []

while True:
    print("\nSelect Area to Shop")
    print("(F)ruit Section")
    print("(V)egetable Section")
    print("(D)elicatessan")
    print("E(x)it")
    area = input("Enter letter of area to shop: ").lower()

    if len(area) > 1:
        area = area[0]

    if area == "f":
        print("Fruit Section")
        print("(A)pples")
        print("A(v)ocado")
        print("(B)anana")
        print("(K)iwifruit")
        print("(O)ranges")
        print("(G)o Back")
        fruit_choice = input("Enter Fruit letter: ").lower()

        if len(fruit_choice) > 1:
            fruit_choice = fruit_choice[0]

        choices = ["a", "v", "b", "k", "o", "g"]

        if fruit_choice not in choices:
            print("Selection Error")
            continue
        elif fruit_choice == "a":
            fruit_find = fruit.index("apples")
        elif fruit_choice == "v":
            fruit_find = fruit.index("avocados")
        elif fruit_choice == "b":
            fruit_find = fruit.index("bananas")
        elif fruit_choice == "k":
            fruit_find = fruit.index("kiwis")
        elif fruit_choice == "o":
            fruit_find = fruit.index("oranges")
        else:
            continue

        fruit_cost = calculate(fruit, fruit_find)
        cartprice += fruit_cost

        money = "{$:,.sf}".format(cartprice)
        print(f"cost so far = {money}")
        print(f"cart items = {cartitems}")

    elif area == "v":
        print("Vegetable Section")
        print("(O)nions")
        print("(C)ucumber")
        print("(P)otatoes")
        print("(L)ettuice")
        print("(S)alad mix")
        print("(G)o Back")
        vege_choice = input("Enter vege letter: ").lower()

        if len(vege_choice) > 1:
            vege_choice = vege_choice[0]

        choices = ["o", "c", "p", "l", "s", "g"]

        if vege_choice not in choices:
            print("Selection Error")
            continue
        elif vege_choice == "o":
            vege_find = vege.index("onions")
        elif vege_choice == "c":
            vege_find = vege.index("cucumbers")
        elif vege_choice == "p":
            vege_find = vege.index("potatoes")
        elif vege_choice == "l":
            vege_find = vege.index("lettuce heads")
        elif vege_choice == "s":
            vege_find = vege.index("salad mixes")
        else:
            continue

        vege_cost = calculate(vege, vege_find)
        cartprice += vege_cost

        money = "{$:,.sf}".format(cartprice)
        print(f"cost so far = {money}")
        print(f"cart items = {cartitems}")

    elif area == "d":
        print("Delicatessen")
        print("(H)am")
        print("(S)almon")
        print("s(A)usages")
        print("sa(L)ami")
        print("(M)ussels")
        print("(G)o Back")
        deli_choice = input("Enter deli letter: ").lower()

        if len(deli_choice) > 1:
            deli_choice = deli_choice[0]

        choices = ["h", "s", "a", "n", "m", "g"]

        if deli_choice not in choices:
            print("Selection Error")
            continue
        elif deli_choice == "h":
            deli_find = deli.index("ham")
        elif deli_choice == "s":
            deli_find = deli.index("salmon")
        elif deli_choice == "a":
            deli_find = deli.index("sausages")
        elif deli_choice == "l":
            deli_find = deli.index("salami")
        elif deli_choice == "m":
            deli_find = deli.index("mussels")
        else:
            continue

        deli_cost = calculate(deli, deli_find)
        cartprice += deli_cost

        money = "{$:,.sf}".format(cartprice)
        print(f"cost so far = {money}")
        print(f"cart items = {cartitems}")


print("Thank you for shopping with us.")
print(f"Total cost - {cartprice}")
print(f"items bought: {cartitems}")

