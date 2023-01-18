routeNum = int(input('Please enter a US Interstate Highway Route number: '))

route = ''
routeSize = ''
routeOrientation = ''
routeParent = ''
routeType = ''

while routeNum != 0:
    if 0 < routeNum <= 999:
        if routeNum // 100 == 0:
            route = 'primary'
            if routeNum % 2 == 0:
                routeOrientation = 'east-west'
            else:
                routeOrientation = 'north-south'

            if routeNum % 5 == 0:
                routeSize = 'a long-distance arterial highway'
            else:
                routeSize = ''

            print(f'Interstate {routeNum} is {routeSize} oriented {routeOrientation}.')

        else:
            route = 'auxiliary'
            if (routeNum // 100) % 2 == 0:
                routeType = 'loop'
            else:
                routeType = 'spur'

            routeParent = routeNum % 100
            print(f'Interstate {routeNum} is a {routeType} highway of Interstate {routeParent}.')
    routeNum = int(input('Please enter a US Interstate Highway Route number:'))