import math

###############################################################
# Question 1
###############################################################
def read_input(file):
    with open(file) as f:
        lines = f.readlines()
    
    return sum([fuel_required(int((x.strip()))) for x in lines])


def fuel_required(mass):
    # Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
    return math.floor(mass / 3) - 2

assert(fuel_required(12) == 2)
assert(fuel_required(14) == 2)
assert(fuel_required(1969) == 654)
assert(fuel_required(100756) == 33583)

print("Answer to question 1:", read_input('./2019/data/day_1.in'))


###############################################################
# Question 2
###############################################################
def fuel_required_recursive(mass):
    fuel = fuel_required(mass)

    if fuel <= 0:
        return 0
    else:
        return fuel + fuel_required_recursive(fuel)

assert(fuel_required_recursive(14) == 2)
assert(fuel_required_recursive(1969) == 966)
assert(fuel_required_recursive(100756) == 50346)

def read_input2(file):
    with open(file) as f:
        lines = f.readlines()
    
    return sum([fuel_required_recursive(int((x.strip()))) for x in lines])

print("Answer to question 2: ", read_input2('./2019/data/day_1.in'))
