cMeal = float(input('What is the price of a child\'s meal? '))
mMeal = float(input('What is the price of an adult\'s meal? '))
countChild = int(input('How many children are there? '))
countAdult = int(input('How many adults are there? '))
tax = float(input('What is the sales tax rate? '))

subtotal = cMeal * countChild + mMeal * countAdult
taxAmt = (tax / 100) * subtotal

print(f'\nSubtotal: ${subtotal:.2f}')
print(f'Sales Tax: ${taxAmt:.2f}')


def tip():
    tipOp = int(input(f'''
Would you like to offer a tip?
0 --- No Tip
1 --- 12% ({subtotal * 0.12:.2f})
2 --- 15% ({subtotal * 0.15:.2f})
3 --- 18% ({subtotal * 0.18:.2f})
\n'''))
    flag = True
    while flag:
        if tipOp == 0:
            return 0
        elif tipOp == 1:
            return subtotal * 0.12
        elif tipOp == 2:
            return subtotal * 0.15
        elif tipOp == 3:
            return subtotal * 0.18
        else:
            print('Error: Invalid Input')
            tipOp = int(input(f'''
Would you like to offer a tip?
0 --- No Tip
1 --- 12% ({subtotal * 0.12:.2f})
2 --- 15% ({subtotal * 0.15:.2f})
3 --- 18% ({subtotal * 0.18:.2f})
\n'''))


total = taxAmt + subtotal + tip()
print(f'Total: ${total:.2f}\n')

payAmt = float(input('What is the payment amount? '))
change = payAmt - total

print(f'Change: ${change:.2f}')