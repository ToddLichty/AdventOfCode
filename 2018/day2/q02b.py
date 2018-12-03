
def readInput(file):
    with open(file) as f:
        lines = f.readlines()
    
    return [(x.strip()) for x in lines] 


def words_differ_by_one_character(word1, word2):
    differences = 0

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            if differences > 0:
                return False
            else:
                differences += 1
    
    return (differences == 1)

def find_words_that_differ_by_one_character(words):
    for i in range(len(words)):
        word1 = words[i]
        rest = words[i:]
        
        for word2 in rest:
            if words_differ_by_one_character(word1, word2):
                return find_common_characters(word1, word2)

def find_common_characters(word1, word2):
    common = ''
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            common += word1[i]

    return common

words = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
assert(find_words_that_differ_by_one_character(words) == 'fgij')

words = readInput('/home/todd/code/AdventOfCode/2018/day2/data/input.txt')
print(find_words_that_differ_by_one_character(words))