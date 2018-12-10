import re, collections, numpy

#468 players; last marble is worth 71843 points


players = 468
last_marble = 71843

def play(players, last_marble):
    marbles = range(1, last_marble+1)

    circle = collections.deque([0])
    scores = numpy.zeros(players, dtype=numpy.int64)
    for marble in marbles:
        player = (marble-1) % players
        
        # first marble in circle = current marble!
        if marble % 23 == 0:
            circle.rotate(7)
            scores[player] += marble + circle.popleft()
        else:
            circle.rotate(-2)
            circle.appendleft(marble)

    return max(scores)

print(play(players, last_marble))

# part 2
print(play(players, last_marble * 100))