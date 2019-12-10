def read_input(file):
    with open(file) as f:
        lines = f.read()
    
    return str(lines)

def parse_input(program_input):
    l = list(map(int, program_input.split(',')))
    
    l.extend([0 for i in range(1000)])
    return l

def Intcode(program_input, user_input, is_feedback=False, instruction_pointer = 0, relative_base = 0):
    instruction_pointer = instruction_pointer
    relative_base = relative_base
    program_output = 0

    def get_data(index, mode):
        return program_input[get_index(index, mode)]

    def get_index(index, mode):
        if mode == 0:
            return program_input[index]
        elif mode == 1:
            return index
        elif mode == 2:
            return relative_base + program_input[index]
        else:
            return ValueError


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
            if is_feedback:
                return program_output, None
            break
        elif opt_code == 3:
            if len(user_input) == 0:
                raise Exception('no input!')

            user_input_value = int(user_input.pop(0))
            parameter_1 = get_index(instruction_pointer + 1, mode_param_1)

            program_input[parameter_1] = user_input_value
            instruction_pointer += 2
        elif opt_code == 4:
            value_1 = get_data(instruction_pointer + 1, mode_param_1) # program_input[instruction_pointer + 1]
            print(value_1)
            program_output = value_1
            instruction_pointer += 2

            if is_feedback:
                return program_output, instruction_pointer
                
        elif opt_code == 5:
            parameter_1 = get_data(instruction_pointer + 1, mode_param_1)
            parameter_2 = get_data(instruction_pointer + 2, mode_param_2)
            
            if parameter_1 != 0:
                instruction_pointer = parameter_2
            else:
                instruction_pointer += 3
        elif opt_code == 6:
            parameter_1 = get_data(instruction_pointer + 1, mode_param_1)
            parameter_2 = get_data(instruction_pointer + 2, mode_param_2)
            
            if parameter_1 == 0:
                instruction_pointer = parameter_2
            else:
                instruction_pointer += 3
        elif opt_code == 9:
            parameter_1 = get_data(instruction_pointer + 1, mode_param_1)
            relative_base += parameter_1

            instruction_pointer += 2
        else:
            parameter_1 = get_data(instruction_pointer + 1, mode_param_1)
            parameter_2 = get_data(instruction_pointer + 2, mode_param_2)
            output_index = get_index(instruction_pointer + 3, mode_param_3)

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

    return program_output


assert(Intcode(parse_input('1102,34915192,34915192,7,4,7,99,0'), []) == 1219070632396864)
assert(Intcode(parse_input('104,1125899906842624,99'), []) == 1125899906842624)

program_input = read_input('./2019/data/day_9.in')
print("Answer to question 1: ", Intcode(parse_input(program_input), [1]))

print("Answer to question 2: ", Intcode(parse_input(program_input), [2]))