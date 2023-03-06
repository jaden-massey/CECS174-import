items = []
prices = []


def print_menu():
    print('''
Please select one of the following:
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit''')


def add_item():
    global items
    global prices

    item = input('What item would you like to add? ')

    if item == '' or item == 'back':
        return None

    while True:
        price = input(f'What is the price of \'{item}\'? ')

        if price == '' or price == 'back':
            return None

        try:
            price = float(price)
        except ValueError:
            print('Invalid input, please enter a valid price!')
            continue
        else:
            break

    items.append(item)
    prices.append(price)

    print(f'\'{item}\' has been added to the cart.')


def view_cart():
    print('The contents of the shopping cart are:')

    if len(items) == 0:
        print('<list empty>')
    else:
        for i in range(len(items)):
            print(f'{i+1}. {items[i]} - ${(prices[i]):.2f}')


def remove_item():
    global items
    global prices

    while True:
        rem = input('Which item would you like to remove? ')

        if rem == '' or rem == 'back':
            return None

        try:
            rem = int(rem)
        except ValueError:
            print('Invalid input, please enter the number of the item you want removed!')
            continue
        
        if rem > 0 and rem < (len(items)+1):
            break
        else:
            print(f'Invalid input, please enter a number between 1 and {len(items)}!')
            continue
    
    del items[rem-1]
    del prices[rem-1]

    print('Item removed.')


def compute_total():
    total = 0

    for i in range(len(items)):
        total += prices[i]
    
    print(f'The total price of the items in the shopping cart is ${total:.2f}')


def shopping_cart_program():
    print('Welcome to the Shopping Cart Program!')

    while True:
        print_menu()
        
        # get and validate input from main menu
        while True:
            selection = input('Please enter an action: ')
            try:
                selection = int(selection)
            except ValueError:
                print('Invalid input, please select an item from the menu and enter its number!')
                continue
            
            if selection > 0 and selection < 6:
                break
            else:
                print('Invalid input, please enter a whole number between 1 and 5')
                continue

        # pass request onto appropiate function
        if selection == 1:
            add_item()
        elif selection == 2:
            view_cart()
        elif selection == 3:
            remove_item()
        elif selection == 4:
            compute_total()
        elif selection == 5:
            break
    
    print('Thank you. Goodbye.')


shopping_cart_program()