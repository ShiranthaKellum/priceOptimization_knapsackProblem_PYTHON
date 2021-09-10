
def minimumPrice(x, y, z):                                          # x for sacksAndContainers list, the y for sacksInContainer list and the z for containerPrice list
    unitPrice = []                                                  # list for the unit price in each container
    for i in range(3):
       unit = z[i] / y[i]                                           # calculate unit price
       unitPrice.append(unit)

    unitPrice.sort()                                                # sort unit price

    for i in range(x[1]):                                           # rearrange the sacksInContainer list according to the sorted unitPrice order
        for j in range(x[1]):
            if unitPrice[i] == z[j] / y[j]:
                tempY = y[i]
                y[i] = y[j]
                y[j] = tempY

    minPrice = 0                                                    # optimized price
    sacks = 0

    for i in range (x [1]):
        for j in range (y [i]):
            if sacks < x[0]:
                minPrice += unitPrice [i]
                sacks += 1
    
    print (int (minPrice))

sacksAndContainers = list (map (int, input().split ()))             # list containing num. of sacks piyasena have and num. of containvers farmers have

sacksInContainer = list (map (int, input ().split ()))              # num.of sacks in each container

containerPrice = list (map (int, input ().split ()))                # price of each container

minimumPrice (sacksAndContainers, sacksInContainer, containerPrice)