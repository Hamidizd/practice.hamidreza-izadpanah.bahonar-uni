menu = [
    ["mobile:", "samsung", "apple"],
    ["Laptop:", "Asus", "Lenovo"],
    ["Television:", "LG", "samsung"],
    ["Refrigerator:", "Emersan", "samsung"],
    ["Laundry:", "Bush", "LG"],
    ["Camera:", "canon", "sony"],
    ["help:","First select the desired product from the menu, then view the related products."]
]
print("***Welcome to our store***")
print("Enter the desired key to view the products")
print("If you need help, enter the help key")
print("----------------------------------------------")
def display_menu(menu):
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i][0]}")
    print("----------------------------------------------")
    choice = int(input("please enter the product number: "))
    if choice > 0 and choice <= len(menu):
        display_submenu(menu[choice-1])
    else:
        print("The menu number is wrong!")

def display_submenu(submenu):
    for i in range(1, len(submenu)):
        print(f"{i}. {submenu[i]}")

display_menu(menu)
input()
