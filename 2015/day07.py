# PART ONE
import sys
import re

def process(pins, instruction, pin_list, numbers):
    if instruction:
        if instruction[0] == 'AND':
            if len(pin_list) == 3:  
                pins[pin_list[2]] = (pins[pin_list[0]] & pins[pin_list[1]]) & 0xFFFF
            else:
                pins[pin_list[1]] = (pins[pin_list[0]] & numbers[0]) & 0xFFFF

        elif instruction[0] == 'OR':
            pins[pin_list[2]] = (pins[pin_list[0]] | pins[pin_list[1]]) & 0xFFFF

        elif instruction[0] == 'NOT':
            pins[pin_list[1]] = (~pins[pin_list[0]]) & 0xFFFF

        elif instruction[0] == 'LSHIFT':
            pins[pin_list[1]] = (pins[pin_list[0]] << numbers[0]) & 0xFFFF

        elif instruction[0] == 'RSHIFT':
            pins[pin_list[1]] = (pins[pin_list[0]] >> numbers[0]) & 0xFFFF

    else: # assign
        if len(pin_list) == 2:
            pins[pin_list[1]] = pins[pin_list[0]]
        else:
            pins[pin_list[0]] = numbers[0]

def parse(line):
    pin_list = re.findall(r'[a-z]+', line)
    numbers = list(map(int, re.findall(r'\d+', line)))
    instruction = re.findall(r'[A-Z]+', line)
    return pin_list, numbers, instruction

pins = {}
backlog = []

with open(sys.argv[1], "r") as f:
    for line in f: 
        pin_list, numbers, instruction = parse(line)
        runnable = True
        for pin in pin_list[:-1]:
            if pin not in pins.keys():
                runnable = False
                break
        if runnable:
            process(pins, instruction, pin_list, numbers) 

        for b in backlog:
            pin_list, numbers, instruction = parse(b)
            runnable = True
            for pin in pin_list[:-1]:
                if pin not in pins.keys():
                    runnable = False
                    break
            if runnable:
                process(pins, instruction, pin_list, numbers)




print(pins)

print(pins['a']) 