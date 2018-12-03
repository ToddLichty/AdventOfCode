n = 1000
m = 1000

cloth = [['.'] * m for i in range(n)]

clean_claims = []

def readInput(file):
    with open(file) as f:
        lines = f.readlines()
    
    return [(x.strip()) for x in lines] 


def count_overlaps():
    num = 0
    for i in range(len(cloth)):
        for j in range(len(cloth[i])):
            if cloth[i][j] == 'X':
                num += 1
    
    return num


def print_cloth(cloth):
    for i in range(len(cloth)):
        for j in range(len(cloth[i])):
            print(cloth[i][j], end=' ')
        print()


def mark_area(claim_id, row, column, width, height):
    max_width = row + width
    intact = True
    for r in range(row,max_width):
        for c in range(column, (column + height)):
            if cloth[c][r] == '.':
                cloth[c][r] = claim_id
            else:
                if cloth[c][r] in clean_claims:
                    clean_claims.remove(cloth[c][r])
                    
                intact = False

                cloth[c][r] = 'X'

    if intact:
        clean_claims.append(claim_id)

def run_instruction(instruction):
    '''
    Input is of the form: claim_id @ row,col: widthxheight

    i.e.    #1 @ 1,3: 4x4
            #2 @ 3,1: 4x4
            #3 @ 5,5: 2x2
    '''
    claim_id = int(instruction.split("@")[0].strip()[1:])
    coordinates = instruction.split(":")[0]
    coordinates = coordinates.split("@")[1].strip().split(",")
    width_height_values = instruction.split(":")[1].strip().split("x")

    mark_area(claim_id, int(coordinates[0]), int(coordinates[1]), int(width_height_values[0]), int(width_height_values[1]))


def test():

    run_instruction("#1 @ 1,3: 4x4")
    run_instruction("#2 @ 3,1: 4x4")
    run_instruction("#3 @ 5,5: 2x2")

    assert cloth[3][3] == 'X'
    assert cloth[3][4] == 'X'
    assert cloth[4][3] == 'X'
    assert cloth[4][4] == 'X'

    assert count_overlaps() == 4

    assert 3 in clean_claims
    print(clean_claims)


instructions = readInput('/home/todd/code/AdventOfCode/2018/data/day03.txt')
for instruction in instructions:
    run_instruction(instruction)

print(count_overlaps())
print(clean_claims)

