from collections import Counter

def readInput(file):
    with open(file) as f:
        lines = f.readlines()
    
    return [(x.strip()) for x in lines] 

def find_product(words):
    num_words_with_two_repeats = 0
    num_words_with_three_repeats = 0

    for word in words:
        counts = Counter(word)

        doubles = {k:v for (k,v) in counts.items() if v == 2}
        triples = {k:v for (k,v) in counts.items() if v == 3}

        if len(doubles) > 0:
            num_words_with_two_repeats += 1
        
        if len(triples) > 0:
            num_words_with_three_repeats += 1
        
    return num_words_with_three_repeats * num_words_with_two_repeats


assert find_product(['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']) == 12

print(find_product(readInput('/home/todd/code/AdventOfCode/2018/data/day02.txt')))