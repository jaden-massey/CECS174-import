# get code input, remove case sensitivity, and store case to convert output back to original input

code = input('Please enter r for residential, c for commercial, or i for industrial: ')

identifier = 0

if code == 'R':
    code = 'r'
    identifier = 1
elif code == 'C':
    code = 'c'
    identifier = 2
elif code == 'I':
    code = 'i'
    identifier = 3

# get reading inputs

perStart = int(input("Enter the customer's beginning meter reading: "))
perEnd = int(input("Enter the customer's ending meter reading:    "))

# check for invalid entries

print()

if perStart > 999_999_999 or perEnd > 999_999_999:
    print('Invalid entry: Please enter a reading between 000000000 and 999999999')

# calculate gallons used

if perStart > perEnd:
    gallonsUsed = (999_999_999 - perStart) + perEnd + 1
else:
    gallonsUsed = perEnd - perStart

gallonsUsed /= 10

# calculate cost

amtBilled = 0

if code == 'r':
    amtBilled = 5.00 + gallonsUsed * 0.0005
elif code == 'c':
    if gallonsUsed <= 4_000_000:
        amtBilled = 1000.00
    else:
        amtBilled = 1000.00 + 0.00025 * (gallonsUsed - 4_000_000)
elif code == 'i':
    if gallonsUsed <= 4_000_000:
        amtBilled = 1000.00
    elif gallonsUsed <= 10_000_000:
        amtBilled = 2000.00
    else:
        amtBilled = 2000.00 + 0.00025 * (gallonsUsed - 10_000_000)
else:
    print('Invalid Entry: incorrect code used, please enter r for residential, c for commercial, or i for industrial')

# print formatted results, replace original casing if necessary

if identifier == 1:
    code = 'R'
elif identifier == 2:
    code = 'C'
elif identifier == 3:
    code = 'I'

print()

print(f'Customer code: {code}')
print('Beginning meter reading: {:0>9}'.format(perStart))
print('Ending meter reading:    {:0>9}'.format(perEnd))
print(f'Gallons of water used: {gallonsUsed}')
print('Amount billed: ${:,.2f}'.format(amtBilled))
