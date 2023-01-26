cMeal = float(input('What is the price of a child\'s meal? '))
mMeal = float(input('What is the price of an adult\'s meal? '))
countChild = int(input('How many children are there? '))
countAdult = int(input('How many adults are there? '))
tax = float(input('What is the sales tax rate? '))

subtotal = cMeal * countChild + mMeal * countAdult
taxAmt = (tax / 100) * subtotal
total = taxAmt + subtotal

print(f'{subtotal:.2f}')