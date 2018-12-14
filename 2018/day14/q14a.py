scoreboard = [3, 7]

elf1 = 0
elf2 = 1

def scorecard_ends_with(test):
    if len(scoreboard) < len(test):
        return False
    else:
        return scoreboard[len(scoreboard) - len(test):] == test

def print_scoreboard():
    global scoreboard
    global elf1
    global elf2

    sc_string = [str(x) for x in scoreboard]
    sc_string[elf1] = '(' + sc_string[elf1] + ')'
    sc_string[elf2] = '[' + sc_string[elf2] + ']'
    print(sc_string)

def part_a():
    global scoreboard
    global elf1
    global elf2

    num_recipies_needed = 846601
    while len(scoreboard) < 10 + num_recipies_needed:
        new_recipe = scoreboard[elf1] + scoreboard[elf2]

        if new_recipe > 9:
            scoreboard.append(int(str(new_recipe)[0]))
            scoreboard.append(int(str(new_recipe)[1]))
        else:
            scoreboard.append(new_recipe)

        elf1 = (elf1 + 1 + scoreboard[elf1]) % len(scoreboard)
        elf2 = (elf2 + 1 + scoreboard[elf2]) % len(scoreboard)

    result = [str(x) for x in scoreboard[num_recipies_needed:num_recipies_needed+10]]
    print('Part A: ' + ''.join(result))

def part_b():
    global scoreboard
    global elf1
    global elf2

    test = [8, 4, 6, 6, 0, 1]
    index = 0
    while True:
        new_recipe = scoreboard[elf1] + scoreboard[elf2]

        if new_recipe > 9:
            scoreboard.append(int(str(new_recipe)[0]))
            scoreboard.append(int(str(new_recipe)[1]))
        else:
            scoreboard.append(new_recipe)
        
        elf1 = (elf1 + 1 + scoreboard[elf1]) % len(scoreboard)
        elf2 = (elf2 + 1 + scoreboard[elf2]) % len(scoreboard)

        if scoreboard[-len(test):] == test or scoreboard[-len(test)-1:-1] == test:
            break

    print("Part B Done", len(scoreboard) - len(test))

part_b()