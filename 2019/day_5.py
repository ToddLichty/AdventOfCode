
def read_input(file):
    with open(file) as f:
        lines = f.read()
    
    return str(lines)

def Intcode(program_input, user_input=''):
    program_input = [int(x) for x in list(program_input.split(','))]
    instruction_pointer = 0
    program_output = ''
    while True:
        instruction = program_input[instruction_pointer]

        if instruction > 99:
            instruction = str(instruction)
            if len(instruction) == 4:
                instruction = '0' + instruction

            if len(instruction) == 3:
                instruction = '00' + instruction
            
            opt_code = int(instruction[3:])
            mode_param_1 = int(instruction[2])
            mode_param_2 = int(instruction[1])
            mode_param_3 = int(instruction[0])
        else:
            opt_code = instruction
            mode_param_1 = mode_param_2 = mode_param_3 = 0

        if opt_code == 99:
            break
        elif opt_code == 3:
            if user_input == '':
                user_input = int(input("Enter value: "))
            else:
                user_input = int(user_input)

            parameter_1 = program_input[instruction_pointer + 1]
            program_input[parameter_1] = user_input
            instruction_pointer += 2
        elif opt_code == 4:
            parameter_1 = program_input[instruction_pointer + 1]

            if mode_param_1 == 1:
                program_output += str(parameter_1)
            else:
                program_output += str(program_input[parameter_1])

            instruction_pointer += 2
        elif opt_code == 5:
            parameter_1 = get_instruction_value(program_input, mode_param_1, instruction_pointer)
            parameter_2 = get_instruction_value(program_input, mode_param_2, instruction_pointer + 1)
            
            if parameter_1 != 0:
                instruction_pointer = parameter_2
            else:
                instruction_pointer += 3
        elif opt_code == 6:
            parameter_1 = get_instruction_value(program_input, mode_param_1, instruction_pointer)
            parameter_2 = get_instruction_value(program_input, mode_param_2, instruction_pointer + 1)
            
            if parameter_1 == 0:
                instruction_pointer = parameter_2
            else:
                instruction_pointer += 3
        else:
            parameter_1 = get_instruction_value(program_input, mode_param_1, instruction_pointer)
            parameter_2 = get_instruction_value(program_input, mode_param_2, instruction_pointer + 1)
            output_index = get_output_index(program_input, mode_param_3, instruction_pointer + 2)

            if opt_code == 1:
                program_input[output_index] = parameter_1 + parameter_2
            elif opt_code == 2:
                program_input[output_index] = parameter_1 * parameter_2
            elif opt_code == 7:
                if parameter_1 < parameter_2:
                    program_input[output_index] = 1
                else:
                    program_input[output_index] = 0
                
            elif opt_code == 8:
                if parameter_1 == parameter_2:
                    program_input[output_index] = 1
                else:
                    program_input[output_index] = 0
                
            instruction_pointer += 4

    return program_input, program_output

def get_output_index(program_input, mode, instruction_pointer):
    if mode == 0:
        return program_input[instruction_pointer + 1]
    else:
        return program_input[instruction_pointer + 1]


def get_instruction_value(program_input, mode, instruction_pointer):
    if mode == 0:
        return program_input[program_input[instruction_pointer + 1]]
    else:
        return program_input[instruction_pointer + 1]


assert(Intcode('1002,4,3,4,33', '1')[0] == [1002, 4, 3, 4, 99])
assert(Intcode('1101,100,-1,4,0', '1')[0] == [1101, 100, -1, 4, 99])

program_input = read_input('./2019/data/day_5.in')
print("Answer to question 1: ", Intcode(program_input, '1')[1])

assert(Intcode('3,9,8,9,10,9,4,9,99,-1,8', 1)[1] == '0')
assert(Intcode('3,9,8,9,10,9,4,9,99,-1,8', 8)[1] == '1')

assert(Intcode('3,9,7,9,10,9,4,9,99,-1,8', 1)[1] == '1')
assert(Intcode('3,9,7,9,10,9,4,9,99,-1,8', 11)[1] == '0')
assert(Intcode('3,9,7,9,10,9,4,9,99,-1,8', 8)[1] == '0')

assert(Intcode('3,3,1108,-1,8,3,4,3,99', '8')[1] == '1')
assert(Intcode('3,3,1108,-1,8,3,4,3,99', '18')[1] == '0')

assert(Intcode('3,3,1107,-1,8,3,4,3,99', 1)[1] == '1')
assert(Intcode('3,3,1107,-1,8,3,4,3,99', 11)[1] == '0')
assert(Intcode('3,3,1107,-1,8,3,4,3,99', 8)[1] == '0')

assert(Intcode('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9', '0')[1] == '0')
assert(Intcode('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9', '4')[1] == '1')

assert(Intcode('3,3,1105,-1,9,1101,0,0,12,4,12,99,1', '0')[1] == '0')
assert(Intcode('3,3,1105,-1,9,1101,0,0,12,4,12,99,1', '13')[1] == '1')

assert(Intcode('3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99', '6')[1] == '999')
assert(Intcode('3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99', '8')[1] == '1000')
assert(Intcode('3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99', '111')[1] == '1001')

print("Answer to question 2: ", Intcode(program_input, '5')[1])