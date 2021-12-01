def part1(data_set):
    to_int = convertToInt(data_set)

    positive = 0
    for i in range(len(to_int) - 1):
        if to_int[i + 1] - to_int[i] > 0:
            positive = positive + 1

    print(positive)

def convertToInt(data):
    data_array = data.split()
    to_int = []

    for i in data_array:
        to_int.append(int(i))

    return to_int

def part2(data_set):
    to_int = convertToInt(data_set)
    
    positive = 0
    sum_array = []
    for i in range(len(to_int) - 2):
        sum = to_int[i] + to_int[i + 1] + to_int[i + 2]
        print(sum)
        sum_array.append(sum)
    
    for i in range(len(sum_array) - 1):
        if sum_array[i + 1] - sum_array[i] > 0:
            positive = positive + 1
    
    print(positive)