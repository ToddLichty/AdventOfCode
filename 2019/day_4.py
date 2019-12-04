import collections
from itertools import groupby

def is_asscending(password):
    for index, digit in enumerate(password):
        if index > 0:
            if int(digit) < int(password[index - 1]):
                return False

    return True

def is_possible_password(password):
    character_groupings = sorted([len(''.join(g)) for _, g in groupby(password)], reverse=True)
    repeat_groupsings = [x for x in character_groupings if x > 1]

    if (len(repeat_groupsings) == 0):
        return False # No repeat characters

    return is_asscending(password)

assert(is_possible_password('111111'))
assert(not is_possible_password('223450'))
assert(not is_possible_password('123789'))

possible_passwords = 0
for i in range(109165, 576724):
    if is_possible_password(str(i)):
        possible_passwords += 1

print("Answer for question 1:", possible_passwords)

###############################################################
# Question 2
###############################################################

def is_possible_password2(password):
    character_groupings = sorted([len(''.join(g)) for _, g in groupby(password)], reverse=True)
    repeat_groupsings = [x for x in character_groupings if x > 1]

    if (len(repeat_groupsings) == 0):
        return False # No repeat characters
    else:
        if len([x for x in repeat_groupsings if x > 2]) == 0:
            #We only have doubles, continue checking
            pass
        elif len([x for x in repeat_groupsings if x == 2]) == 0:
            # We only have larger than doubles
            return False

    return is_asscending(password)

assert(is_possible_password2('112233')) 
assert(not is_possible_password2('123444'))
assert(is_possible_password2('111122'))

possible_passwords = 0
for i in range(109165, 576724):
    if is_possible_password2(str(i)):
        possible_passwords += 1

print("Answer for question 2:", possible_passwords)