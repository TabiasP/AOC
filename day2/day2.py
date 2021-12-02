import re

def part1(data_set):
    digits_pattern = '\d+'
    words_pattern = '[a-zA-Z]+'
    digits = re.findall(digits_pattern, data_set) 
    words = re.findall(words_pattern, data_set)

    object_build = {
    "Horizontal": 0,
    "Depth": 0,
    }

    for i in range(len(digits)):
        if words[i] == "forward":
            object_build['Horizontal'] = object_build['Horizontal'] + int(digits[i])
        elif words[i] == "up":
            object_build['Depth'] = object_build['Depth'] - int(digits[i])
        else:
            object_build['Depth'] = object_build['Depth'] + int(digits[i])

    print(object_build['Horizontal'] * object_build['Depth'])

def part2(data_set):
    digits_pattern = '\d+'
    words_pattern = '[a-zA-Z]+'
    digits = re.findall(digits_pattern, data_set) 
    words = re.findall(words_pattern, data_set)

    object_build = {
    "Horizontal": 0,
    "Depth": 0,
    "Aim": 0
    }

    for i in range(len(digits)):
        if words[i] == "forward":
            object_build['Horizontal'] = object_build['Horizontal'] + int(digits[i]) 
            object_build['Depth'] += (object_build['Aim'] * int(digits[i]))
        elif words[i] == "up":
            object_build['Aim'] = object_build['Aim'] - int(digits[i])
        else:
            object_build['Aim'] =  object_build['Aim'] + int(digits[i])

    print(object_build['Horizontal'] * object_build['Depth'])

