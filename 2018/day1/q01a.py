def readInput(file):
    with open(file) as f:
        lines = f.readlines()
    
    return [int(x.strip()) for x in lines] 

if __name__ == "__main__":
    lines = readInput('/home/todd/code/AdventOfCode/2018/data/day01.txt')
    print(sum(lines))
