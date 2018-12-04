from collections import Counter

guard_sleep_times = {}

def readInput(file):
    with open(file) as f:
        lines = f.readlines()
    lines.sort()
    return [(x.strip()) for x in lines] 


def record_asleep_time(guard_id, minute_asleep, minute_awake):
    asleep = list(range(minute_asleep,minute_awake))

    if guard_id in guard_sleep_times:
        guard_sleep_times[guard_id] = asleep + guard_sleep_times[guard_id]
    else:
        guard_sleep_times[guard_id] = asleep 


def get_guard_most_asleep() -> int:
    guard_id = int(sorted(guard_sleep_times, key=lambda k: len(guard_sleep_times[k]), reverse=True)[0])
    guard_minutes_asleep = guard_sleep_times[guard_id]
    most_common_minute = int(Counter(guard_minutes_asleep).most_common(1)[0][0])
    return guard_id * most_common_minute


def parse_time(instruction):
    words = instruction.split()
    time = words[1][:-1]
    return int(time.split(':')[1])

def parse_instructions(instructions):
    current_guard = -1
    asleep = 0

    for instruction in instructions:
        time = parse_time(instruction)

        if 'Guard' in instruction:
            current_guard = int(instruction.split()[3][1:])
        elif 'asleep' in instruction:
            asleep = time
        elif 'wakes' in instruction:
            record_asleep_time(current_guard, asleep, time)

def test():
    parse_instructions(
        [
            '[1518-11-01 00:00] Guard #10 begins shift',
            '[1518-11-01 00:05] falls asleep',
            '[1518-11-01 00:25] wakes up',
            '[1518-11-01 00:30] falls asleep',
            '[1518-11-01 00:55] wakes up',
            '[1518-11-01 23:58] Guard #99 begins shift',
            '[1518-11-02 00:40] falls asleep',
            '[1518-11-02 00:50] wakes up',
            '[1518-11-03 00:05] Guard #10 begins shift',
            '[1518-11-03 00:24] falls asleep',
            '[1518-11-03 00:29] wakes up',
            '[1518-11-04 00:02] Guard #99 begins shift',
            '[1518-11-04 00:36] falls asleep',
            '[1518-11-04 00:46] wakes up',
            '[1518-11-05 00:03] Guard #99 begins shift',
            '[1518-11-05 00:45] falls asleep',
            '[1518-11-05 00:55] wakes up',
        ]
    )

    assert get_guard_most_asleep() == 240
    assert (get_minute_most_asleep() == 4455)

def get_minute_most_asleep():
    best_count = None
    best_minute = None
    best_guard = None

    for guard, minutes in guard_sleep_times.items():
        entry = Counter(minutes).most_common(1)[0]

        if best_count is None or int(entry[1]) > best_count:
            best_guard = guard
            best_minute = int(entry[0])
            best_count = int(entry[1])
        
    return (best_minute * best_guard)

#test()

parse_instructions(readInput('/home/todd/code/AdventOfCode/2018/data/day04.txt'))
print(get_guard_most_asleep())
print(get_minute_most_asleep())
