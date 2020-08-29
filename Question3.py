def showMenu():
    print("Menu", menu)
    print("Order Something: ")
    order()

def showBill(x):
    print("\nBill", "\nItem : ", x, "\nPrice : ", menu[x], "\nTotal : ", menu[x])
    

def order():
    x = input()
    x = x.upper()
    if x in menu.keys():
        showBill(x)
    else:
        print("Product is not in the 'Menu'Please select something from Menu: ")
        showMenu()

menu = {"DAAL" : 80,
        "PANEER" : 120,
        "ROTI" : 5}

showMenu()