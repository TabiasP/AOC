data_set = """"""

data = data_set.split("\n")

def part1(data_set):
    gamma = ""
    epsilon = ""

    length = len(data[0])

    for i in range(length):
        x1 = 0
        x0 = 0
        for k in range(len(data_set)):
            if int(data_set[k][i]) == 1:
                x1+=1
            else:
                x0+=1
        if x0 > x1:
            gamma += "0"
            epsilon += "1"
        else :
            gamma += "1"
            epsilon += "0"
    return gamma, epsilon

part1_result = part1(data)

gamma_decimal = int(part1_result[0], 2)
epsilon_decimal = int(part1_result[1], 2)
total = gamma_decimal * epsilon_decimal

print("Gamma:", gamma_decimal, "Epsilon:", epsilon_decimal, "Total:", total)

############ Part 2 ############
def findOxygen(data_set, n):
    x0 = 0
    x1 = 0
    oxygen_generator = []
    for i in range(len(data_set)):
        if int(data_set[i][n]) == 1:
            x1+=1
        else:
            x0+=1
        
    if x1 > x0:
        for i in range(len(data_set)):
            if int(data_set[i][n]) == 1:
                oxygen_generator.append(data_set[i])
    elif x0 > x1:
        for i in range(len(data_set)):
            if int(data_set[i][n]) == 0:
                oxygen_generator.append(data_set[i])
    else:
        for i in range(len(data_set)):
            if int(data_set[i][n]) == 1:
                oxygen_generator.append(data_set[i])
    
    return oxygen_generator

def findCO2(data_set, n):
    x0 = 0
    x1 = 0
    oxygen_generator = []
    for i in range(len(data_set)):
        if int(data_set[i][n]) == 1:
            x1+=1
        else:
            x0+=1
        
    if x1 < x0:
        for i in range(len(data_set)):
            if int(data_set[i][n]) == 1:
                oxygen_generator.append(data_set[i])
    elif x0 < x1:
        for i in range(len(data_set)):
            if int(data_set[i][n]) == 0:
                oxygen_generator.append(data_set[i])
    else:
        for i in range(len(data_set)):
            if int(data_set[i][n]) == 0:
                oxygen_generator.append(data_set[i])
    return oxygen_generator

def gamma(data_set):
    n = 0
    while len(data_set) != 1:
        data_set = findOxygen(data_set, n)
        n+=1

    return data_set

def epsilon(data_set):
    n = 0
    while len(data_set) != 1:
        data_set = findCO2(data_set, n)
        n+=1

    return data_set

gamma_result = int(gamma(data)[0], 2)
epsilon_result = int(epsilon(data)[0], 2)

print("Gamma: ", gamma_result, "Epsilon:", epsilon_result, "Total:", epsilon_result * gamma_result)