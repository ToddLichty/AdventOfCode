###############################################################
# Question 1
###############################################################
def read_input(file):
    with open(file) as f:
        lines = f.read()
    
    return str(lines)


def Intcode(program_input):
    program_input = [int(x) for x in list(program_input.split(','))]
    instruction_pointer = 0

    while True:
        opt_code = program_input[instruction_pointer]

        if opt_code == 99:
            break

        input_1 = program_input[program_input[instruction_pointer + 1]]
        input_2 = program_input[program_input[instruction_pointer + 2]]
        output_index = program_input[instruction_pointer + 3]

        if opt_code == 1:
            program_input[output_index] = input_1 + input_2
        elif opt_code == 2:
            program_input[output_index] = input_1 * input_2

        instruction_pointer += 4

    return program_input


assert(Intcode('1,9,10,3,2,3,11,0,99,30,40,50') == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50])
assert(Intcode('1,0,0,0,99') == [2,0,0,0,99])
assert(Intcode('2,3,0,3,99') == [2,3,0,6,99])
assert(Intcode('2,4,4,5,99,0') == [2,4,4,5,99,9801])
assert(Intcode('1,1,1,4,99,5,6,0,99') == [30,1,1,4,2,5,6,0,99])

initial_memory_input = list(read_input('./2019/data/day_2.in').split(','))
program_input = initial_memory_input
program_input[1] = '12'
program_input[2] = '2'

print("Answer to question 1: ", Intcode(','.join(program_input))[0])


###############################################################
# Question 2
###############################################################

for noun in range(0, 100):
    for verb in range(0, 100):
        program_input = initial_memory_input
        program_input[1] = str(noun)
        program_input[2] = str(verb)

        output = Intcode(','.join(program_input))[0]

        if output == 19690720:
            print("Answer to question 2: ", 100 * noun + verb)

