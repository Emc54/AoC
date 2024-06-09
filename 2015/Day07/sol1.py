#Problem goes here
import time

with open("input","r") as f:
    data = f.read().split("\n")

sep_data = [x.split(" ") for x in data]
sep_data = sep_data[:-1]

# parse the numbers
for idx1, instruction in enumerate(sep_data):
    for idx,part in enumerate(instruction):
        if part.isnumeric():
            sep_data[idx1][idx] = int(part)
        

operations = ["AND","OR","NOT","RSHIFT","LSHIFT"]
                
def operation_parser(instruction):
    
    output = instruction[-1]

    operation = ""
    inputs = []

    for item in instruction[:-2]:
        if item not in operations:
            inputs.append(item)
        else:
            operation = item 

    return inputs, operation, output


wires = {}
done_instructions = []

## Initialise all wires to 0
for inst in sep_data:

    inputs, _, out = operation_parser(inst)
    wires[out] = 0


# sep_data.remove([0,'->','c'])
outs = set()

while len(sep_data) != 0:
    instruction = sep_data.pop(0)
    inputs, op, output = operation_parser(instruction)
    
    # if no operation then it's just assignment
    if op == "":
        if type(inputs[0]) == int:
            wires[output] = inputs[0]
            outs.add(output)
        elif inputs[0] not in outs:
            sep_data.append(instruction)
        else:
            wires[output] = wires[inputs[0]]    
            outs.add(output)
        
        continue        
    
    #if op is NOT, there is only one input
    if op == "NOT":
        if inputs[0] not in outs:
            sep_data.append(instruction)
            continue
        else:
            wires[output] = 0xFFFF - (wires[inputs[0]] & 0xFFFF)
            outs.add(output)
            continue

    
    if type(inputs[0]) != int and inputs[0] not in outs \
        or (type(inputs[1]) != int and inputs[1] not in outs):
        sep_data.append(instruction)
        continue
        

    a = inputs[0] if type(inputs[0]) == int else wires[inputs[0]]
    b = inputs[1] if type(inputs[1]) == int else wires[inputs[1]]
    
    # It's a valid operation, perform it
    if op == "AND":
        wires[output] = (a & b) & 0xFFFF
        outs.add(output)
    if op == "OR":
        wires[output] = (a | b) & 0xFFFF
        outs.add(output)
    if op == "LSHIFT":
        wires[output] = (a << b) & 0xFFFF
        outs.add(output)
    if op == "RSHIFT":
        wires[output] = (a >> b) & 0xFFFF
        outs.add(output)

    done_instructions.append(instruction)


print(wires["a"])
