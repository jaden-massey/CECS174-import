# initialize money constant index
val = [5, 10, 25, 100, 500]

# initialize stock & change
nickels = 25
dimes = 25
quarters = 25
ones = 0
fives = 0

change = 0


# lots of functions

# prints current stock
def print_stock():
    print(f'''Stock contains: 
   {nickels} nickels
   {dimes} dimes
   {quarters} quarters
   {ones} ones
   {fives} fives
   ''')


# prints deposit menu
def print_dep_menu():
    print('''
Menu for deposits:
   'n' - deposit a nickel
   'd' - deposit a dime
   'q' - deposit a quarter
   'o' - deposit a one dollar bill
   'f' - deposit a five dollar bill
   'c' - cancel the purchase
      ''')


# takes string input, and returns appropriate denomination value
def determine_coin(deposit):
    if deposit == 'n':
        return val[0]
    elif deposit == 'd':
        return val[1]
    elif deposit == 'q':
        return val[2]
    elif deposit == 'o':
        return val[3]
    elif deposit == 'f':
        return val[4]
 

# takes string input, and iterates respective denomination
def count_coin(deposit):
    if deposit == 'n':
        global nickels
        nickels += 1
    elif deposit == 'd':
        global dimes
        dimes += 1
    elif deposit == 'q':
        global quarters
        quarters += 1
    elif deposit == 'o':
        global ones
        ones += 1
    elif deposit == 'f':
        global fives
        fives += 1


# validates deposit input to prevent errors
def validate_deposit(deposit):
    if deposit == 'n':
        return True
    elif deposit == 'd':
        return True
    elif deposit == 'q':
        return True
    elif deposit == 'o':
        return True
    elif deposit == 'f':
        return True
    else:
        return False


# checks if the inputted price is a float
def validate_price(num):
    try:  # attempts to float the value
        float(num)
        return True
    except ValueError:  # if float conversion fails, instead of crashing the program, it returns false
        return False

# handles nearly everything change related including, greedy coin algorithm, updating stock, and printing output
def change_calc(c):
    global quarters
    global dimes
    global nickels

    # greedy coin algorithm, with limited stock checks
    # min builtin function returns the lowest of the two values
    # learned how to use min to massively shorten this portion of code

    q = min(quarters, (c // 25))
    c -= 25 * q
    d = min(dimes, (c // 10))
    c -= 10 * d
    n = min(nickels, (c // 5))
    c -= 5 * n

    # update coin stock and print output, also checks if coin is dispensed to prevent display of empty values
    print('Please take the change below.')
    if q > 0:
        quarters -= q
        print('   ' + str(q) + ' quarters')
    if d > 0:
        dimes -= d
        print('   ' + str(d) + ' dimes')
    if n > 0:
        nickels -= n
        print('   ' + str(n) + ' nickels')

    # prompt user to see manager in case of not enough change
    if c > 0:  # if c > 0 that means we couldn't make change with what we had
        print('Machine is out of change.')
        print('See store manager for remaining fund')
        print('Amount due is: ', end='')  # more string concatenation to reduce redundancy

        if c >= 100:
            print(str(c // 100) + ' dollars', end=' and ')
        print(str(c % 100) + ' cents')
    print()


def payment_due(mon):
    # initialize variables
    money_paid = 0  # used to track money paid in case of cancellation of payment
    global change
    change = 0

    # count based loop for payment
    while mon > 0:
        dollars_due = int(round(mon // 100))
        cents_due = int(round(mon - dollars_due * 100))
        print('Payment due: ', end='')  # using string concatenation to make code less repetitive
        if dollars_due == 0:  # prevents empty dollar values from being printed
            print(str(cents_due) + ' cents')
        else:
            print(str(dollars_due) + ' dollar(s) and ' + str(cents_due) + ' cents')
        dep = input('Indicate your deposit: ')
        while dep != 'c':  # validates payment & keeps track of payments made
            if validate_deposit(dep):  # validate input
                mon -= determine_coin(dep)  # update money to be paid
                money_paid += determine_coin(dep)  # update total amount paid so far
                count_coin(dep)  # iterate coin count to keep track of stock
                break
            if dep == 'c':
                break
            else:
                print(f'Illegal selection: {dep}')
                if dollars_due == 0:
                    print(str(cents_due) + ' cents')
                else:
                    print(str(dollars_due) + ' dollar(s) and ' + str(cents_due) + ' cents')
                dep = input('Indicate your deposit: ')
        if dep == 'c':  # used to pay back money in case of cancellation
            change += money_paid
            mon = 0
            break
    print()
    change += abs(mon)  # update change variable with amount overpaid


def calc_total():
    total = val[0] * nickels + val[1] * dimes + val[2] * quarters + val[3] * ones + val[4] * fives
    total_dollars = int(round(total // 100))
    total_cents = int(round(total - total_dollars * 100))
    print('\nTotal: ' + str(total_dollars) + ' dollars and ' + str(total_cents) + ' cents')


# __main__
print('''Welcome to the vending machine change maker program.
Change maker initialized.''')
print_stock()

# initialize money
money = input('Enter the purchase price (xx.xx) or \'q\' to quit: ')

# initialize main sentinel loop
while money != 'q':
    if validate_price(money):  # check for float values to prevent errors
        money = int(float(money) * 100)  # convert dollars to cents to prevent rounding errors
        if money < 0 or money % 5 != 0:  # validate money input again now that we've filtered out non-numbers
            print('Illegal price: Must be a non-negative multiple of 5 cents.')
            money = input('\nEnter the purchase price (xx.xx) or \'q\' to quit: ')
            continue

        # start payment system
        print_dep_menu()
        payment_due(money)

        # check for change and deposit if there is some
        if change > 0:
            change_calc(change)
        else:
            print('No change due.\n')
        print_stock()

        # prepare for next iteration
        money = input('Enter the purchase price (xx.xx) or \'q\' to quit: ')

    else:
        print('Illegal price: Must be a non-negative multiple of 5 cents.')
        money = input('\nEnter the purchase price (xx.xx) or \'q\' to quit: ')
        continue

# calculate total money left in machine & print
calc_total()
