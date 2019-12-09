import itertools

def read_input(file):
    with open(file) as f:
        lines = f.read()
    
    return str(lines)

def parse_input(program_input):
    return list(map(int, program_input.split(',')))


def Intcode(program_input, user_input, is_feedback=False, instruction_pointer = 0):
    instruction_pointer = instruction_pointer
    program_output = 0

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

            parameter_1 = program_input[instruction_pointer + 1]
            program_input[parameter_1] = user_input_value
            instruction_pointer += 2
        elif opt_code == 4:
            parameter_1 = get_instruction_value(program_input, mode_param_1, instruction_pointer) # program_input[instruction_pointer + 1]

            program_output += int(parameter_1)
            instruction_pointer += 2

            if is_feedback:
                return program_output, instruction_pointer
                
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

    return program_output

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


def get_output(program_input, phase_setting):
    last_output = 0
    for phase in phase_setting:
        last_output = Intcode(parse_input(program_input), [phase,last_output])

    return int(last_output)


def get_max_output(program_input):
    phase_settings = list(itertools.permutations('01234'))
    max_output = 0

    for phase_setting in phase_settings:
        output = get_output(program_input, phase_setting)
        max_output = max(output, max_output)

    return max_output


assert(get_output('3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0', '43210') == 43210)
assert(get_output('3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0', '01234') == 54321)
assert(get_output('3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0', '10432') == 65210)

assert(get_max_output('3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0') == 43210)
assert(get_max_output('3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0') == 54321)
assert(get_max_output('3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0') == 65210)

program_input = read_input('./2019/data/day_7.in')
print('Answer to question 1: ', get_max_output((program_input)))


def get_output_with_feedback(program_input, phase_setting):
    program_input = parse_input(program_input)
    programs, pcs, inputs = [], [], []
    num_amps = len(phase_setting)
    output = 0
    for i in range(0, num_amps):
        programs.append(program_input.copy())
        pcs.append(0)
        inputs.append([phase_setting[i]])

    while pcs[0] is not None:
        for i in range(0, num_amps):
            inputs[i].append(output)
            output, pc = Intcode(programs[i], inputs[i], True, pcs[i])
            pcs[i] = pc


    return inputs[0][0]

assert(get_output_with_feedback('3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5', '98765') == 139629729)
assert(get_output_with_feedback('3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10', '97856') == 18216)

def get_max_output_with_feedback(program_input):
    phase_settings = list(itertools.permutations('56789'))
    max_output = 0

    for phase_setting in phase_settings:
        output = get_output_with_feedback(program_input, phase_setting)
        max_output = max(output, max_output)

    return max_output

print('Answer to question 2: ', get_max_output_with_feedback(program_input))