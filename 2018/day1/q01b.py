def readInput(file):
    with open(file) as f:
        lines = f.readlines()
    
    return [int(x.strip()) for x in lines] 

def first_repeated_frequency(numbers):
    seen_frequencies = {0}
    current_frequency = 0

    while True:
        for change in numbers:
            current_frequency += change

            if current_frequency in seen_frequencies:
                return current_frequency
            else:
                seen_frequencies.add(current_frequency)


if __name__ == "__main__":
    assert first_repeated_frequency([1, -2, 3, 1]) == 2
    assert first_repeated_frequency([1, -1]) == 0
    assert first_repeated_frequency([3, 3, 4, -2, -4]) == 10
    assert first_repeated_frequency([-6, 3, 8, 5, -6]) == 5
    assert first_repeated_frequency([7, 7, -2, -7, -4]) == 14

    lines = readInput('/home/todd/code/AdventOfCode/2018/day1/data/q01a_input.txt')
    print(first_repeated_frequency(lines))
