from category import Category
from categories import Categories
from product import Product
from products import Products
from order import Order
from orders import Orders
from json import JSONDecodeError

def addCategory():
    catName = input("[>] What should the category be called?: ")
    newCat = Category(catName)
    existedAlready = Categories.addCategory(newCat)
    if existedAlready:
        print(f'[<] Category "{catName}" already exists!')
    else:
        print(f'[<] Category "{catName}" has been added!')
    print(f'====================================')

def deleteCategory():
    catName = input("[>] What category you want to remove?: ")
    newCat = Category(catName)
    existed = Categories.removeCategory(newCat)
    if existed:
        print(f'[<] Category "{catName}" has been removed!')
    else:
        print(f'[<] Category "{catName}" does not exist!')
    print(f'====================================')

def listCategories():
    # display the existing categories
    print('[<] Now showing available categories: ')
    try:
        categories = Categories.loadCategories()
        for cat in categories:
            print(cat.name)
    except JSONDecodeError as _:
        pass
    print(f'====================================')

def addProduct():
    cat = input("[>] In which category should it be placed?: ")

    categories = Categories.loadCategories()
    catObj = Category(cat)
    if catObj not in categories:
        print(f'Category "{cat}" does not exist!')
        return

    name = input("[>] What should the product be called?: ")
    qty = int(input("[>] Input available product quantity: "))
    print("[>] Input product attributes one by one in the format -> attr:value")
    print("[>] Type 'exit' to finish inputting values")

    attrs = {"name" : name, "cat" : cat, "qty" : qty}

    while True:
        inp = input("[>] attribute:value -> ")

        if inp == 'name' or inp == 'cat' or inp == 'qty':
            print(f'[<] Attribute name "{inp}" is reserved!')
            continue
        if inp == 'exit':
            break
        try:
            splitInput = inp.split(':')
            attrs[splitInput[0]] = splitInput[1]
        except IndexError as _:
            print('[<] Invalid input! Try again')

    newProd = Product(attrs)
    existedAlready = Products.addProduct(newProd)
    if existedAlready:
        print(f'[<] Product "{name}" already exists!')
    else:
        print(f'[<] Product "{name}" has been added!')
    print(f'====================================')

def deleteProduct():
    prodName = input("[>] What product you want to remove?: ")
    newProd = Product({"name" : prodName})
    existed = Products.removeProduct(newProd)
    if existed:
        print(f'[<] Product "{prodName}" has been removed!')
    else:
        print(f'[<] Product "{prodName}" does not exist!')
    print(f'====================================')

def listProducts():
    print('[<] Now showing available products: ')
    try:
        products = Products.loadProducts()
        for prod in products:
            print(prod)
    except JSONDecodeError as _:
        pass
    print(f'====================================')

def placeOrder():
    products = Products.loadProducts()
    productsToBuy = []

    print("[<] Use 'done' to stop appending to this order!")
    while True:
        prod = input("[>] Which item do you want to buy?: ")

        if prod == 'done':
            break

        prodObj = Product({"name": prod})
        if prodObj not in products:
            print(f'[<] Product "{prod}" does not exist in any category!')
            continue

        qty = int(input("[>] How many do you want?: "))
        prodObj = Products.getProduct(prodObj)
        prodQty = prodObj.attrs.get('qty')

        if qty > prodQty:
            print(f'[<] Cannot order such quantity! Available qty {prodQty}')
            continue

        prodObj.attrs.update({"qty" : prodQty - qty})
        Products.setProduct(prodObj)
        productsToBuy.append((prod, qty))

    if len(productsToBuy):
        shipAddress = input("[>] Finally, please input shipping address: ")
        order = Order(shipAddress,productsToBuy)
        orderId = Orders.addOrder(order)
        print(f'[<] Order with id={orderId} has been placed!')
    else:
        print('[<] No items added to order, nothing to order!')
    print(f'====================================')


def listOrders():
    print('[<] Now showing stored orders: ')
    try:
        orders = Orders.loadOrders()
        for order in orders:
            print(order)
    except JSONDecodeError as _:
        pass
    print(f'====================================')


def exitApp():
    print("[<] Bye bye!")
    exit()

def unrecognizedOption():
    print("[<] This option does not exist")

def printMenu():
    print(f'========== JEWELLERY SHOP ==========')
    print(f'=       1. Add a category          =')
    print(f'=       2. Remove a category       =')
    print(f'=       3. List all categories     =')
    print(f'=       4. Add a product           =')
    print(f'=       5. Remove a product        =')
    print(f'=       6. List all products       =')
    print(f'=       7. Place an order          =')
    print(f'=       8. List all orders         =')
    print(f'=       9. Exit                    =')
    print(f'====================================')
    print()

if __name__ == "__main__":

    menus = {
        1 : addCategory,
        2 : deleteCategory,
        3 : listCategories,
        4 : addProduct,
        5 : deleteProduct,
        6 : listProducts,
        7 : placeOrder,
        8 : listOrders,
        9 : exitApp
    }

    printMenu()

    # main loop
    while True:
        userChoice = int(input("[>] Please enter your choice: "))
        func = menus.get(userChoice,unrecognizedOption)
        printMenu()
        func()
