"""Advent of code 2019 day 2"""

def memory():
    return list(map(int, open("data.txt").read().split(",")))

def intcode(data):
    for i in range(0, len(data)-4, 4):
        opcode = data[i]
        input1 = data[data[i+1]]
        input2 = data[data[i+2]]    
        if opcode == 1:
            data[data[i+3]] = input1 + input2
        elif opcode == 2:
            data[data[i+3]] = input1*input2
        else:
            break
    return data[0]

def replace(data, replacements):
    data[1] = replacements[0]
    data[2] = replacements[1]

def program_1202():
    data = memory()
    replace(data, [12,2])
    return intcode(data)

print(program_1202())

def find_replacements(output):
    for noun in range(100):
        for verb in range(100):
            data = memory()
            replace(data, [noun, verb])
            if intcode(data) == output:
                result = 100 * noun + verb
    return result

print(find_replacements(19690720))
