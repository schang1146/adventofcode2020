# initialize problem variables
data = []
example1 = []

# populate sample data from example file(s)
filename = 'example1.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        example1 = line.split(',')

# populate data from input file
filename = 'input.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        data = line.split(',')


def solution1(data, target):
    db = {}
    prev = int(data[-1])
    for turn in range(1, len(data)+1):
        db[int(data[turn-1])] = [turn]
        # print(f'{turn} | {data[turn-1]}')

    for turn in range(len(data)+1, target+1):
        if len(db[prev]) < 2:  # number is new, return 0 for the turn
            if 0 in db:
                db[0].append(turn)
            else:
                db[0] = [turn]
            prev = 0
        else:
            turnNum = db[prev][1] - db[prev][0]
            if turnNum in db:
                db[turnNum].append(turn)
            else:
                db[turnNum] = [turn]
            prev = turnNum

        if len(db[prev]) > 2:
            db[prev].pop(0)

        # print(f'{turn} | {prev}')
    return prev


if __name__ == "__main__":

    solution1(data, 10)
    solution1(data, 100)
    solution1(data, 1000)
    solution1(data, 10000)
    solution1(data, 100000)
    solution1(data, 1000000)
    # solution1(data, 10000000)
    # solution1(data, 30000000)
    # print(
    #     f'Sample 1 Part 1 Solution: {solution1(example1, 2020)} should be 436')
    # print(f'Part 1 Solution: {solution1(data, 2020)}')
    # print()
    # print(
    #     f'Sample 1 Part 2 Solution: {solution1(example1, 30000000)} should be 175594')
    # print(f'Part 2 Solution: {solution1(data, 30000000)}')
