'''
Find the fuel cell's rack ID, which is its X coordinate plus 10.
Begin with a power level of the rack ID times the Y coordinate.
Increase the power level by the value of the grid serial number (your puzzle input).
Set the power level to itself multiplied by the rack ID.
Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
Subtract 5 from the power level.
'''

grid = [[0 for i in range(1,302)] for j in range(1,302)]

def calculate_power_level(x, y, serial_number):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    power_level = ((power_level // 100)%10) - 5
    return power_level

def calc_square_level(x, y):
    sum_ = 0
    for row in range(x, x+3):
        for col in range(y, y+3):
            sum_ += grid[row][col]

    return sum_

def populate_grid(serial_number):
    for col in range(1, 301):
        for row in range(1, 301):
            grid[col][row] = calculate_power_level(col, row, serial_number)

def get_max_power_square():
    max_power = 0
    coords = ()

    for col in range(1, 299):
        for row in range(1, 299):
            power = calc_square_level(col, row)
            if power > max_power:
                max_power = power
                coords = (col, row)

    return (max_power, coords[0], coords[1])

assert calculate_power_level(3, 5, 8) ==  4
assert calculate_power_level(217, 196, 39) == 0
assert calculate_power_level(122, 79, 57) == -5
assert calculate_power_level(101, 153, 71) == 4

populate_grid(18)
assert get_max_power_square() == (29, 33, 45)

populate_grid(42)
assert get_max_power_square() == (30, 21, 61)

populate_grid(1723)
print(get_max_power_square())