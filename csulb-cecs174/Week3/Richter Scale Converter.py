# psuedocode
# start
# define function to calculate richter scale to joules, joules to TNT, and print the outputs
# call function for given richter values

# prompt float input richter values
# convert magnitude to joules
# convert joules to tons of TNT
# print richter scale value, joule & tons of tnt equivalence
# exit


def richter(mag):
    funcj = (10 ** (4.8 + (1.5 * mag)))
    functnt = funcj / (4.184 * (10 ** 9))
    print(f"{mag}         {funcj}         {functnt}")


print('Richter        Joules                        TNT')
richter(1.0)
richter(5.0)
richter(9.1)
richter(9.2)
richter(9.5)

print()

m = float(input('Please Enter a Richter Scale value: \n'))

if m <= 0:
    print('Please enter a Richter scale value greater than 0')

elif m > 20:
    print('Please enter a Richter scale value between 0 and 20, non-inclusive')
else:
    j = (10 ** (4.8 + (1.5 * m)))
    tnt = j / (4.184 * (10 ** 9))

    print(f'Richter scale value: {m}')
    print(f'Equivalence in joules: {j}')
    print(f'Equivalence in tons of TNT: {tnt}')
