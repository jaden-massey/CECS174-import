
car_mpg = float(input('Enter your car\'s milegage in miles per gallon'))
gas_dpg = float(input('Enter the price of gas in dollars per gallon'))

gasCost10 = (car_mpg / gas_dpg) * 10
gasCost50 = (car_mpg / gas_dpg) * 50
gasCost400 = (car_mpg / gas_dpg) * 400

print(gasCost10)
print(gasCost50)
print(gasCost400)