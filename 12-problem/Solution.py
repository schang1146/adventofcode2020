import math

# initialize problem variables
data = []
example1 = []

# populate sample data from example file(s)
filename = 'example1.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        example1.append(line.strip())

# populate data from input file
filename = 'input.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        data.append(line.strip())

# function TODO
# time complexity: TODO
# space complexity: TODO
def getManhattanDist(coords):
    return round(abs(coords[0]) + abs(coords[1]))

def N(coords, heading, magnitude):
    return [[coords[0], coords[1] + magnitude], heading]
def S(coords, heading, magnitude):
    return [[coords[0], coords[1] - magnitude], heading]
def E(coords, heading, magnitude):
    return [[coords[0] + magnitude, coords[1]], heading]
def W(coords, heading, magnitude):
    return [[coords[0] - magnitude, coords[1]], heading]
def L(coords, heading, magnitude):
    return [[coords[0], coords[1]], heading + magnitude]
def R(coords, heading, magnitude):
    return [[coords[0], coords[1]], heading - magnitude]
def F(coords, heading, magnitude):
    rad = heading * math.pi / 180
    horizontalChange = math.cos(rad) * magnitude
    verticalChange = math.sin(rad) * magnitude
    return [[coords[0] + horizontalChange, coords[1] + verticalChange], heading]
# function TODO
# time complexity: TODO
# space complexity: TODO
def travel(coords, heading, instruction):
    options = {
        'N': N,
        'S': S,
        'E': E,
        'W': W,
        'L': L,
        'R': R,
        'F': F
    }
    return options[instruction[0]](coords, heading, int(instruction[1:]))

# function TODO
# time complexity: TODO
# space complexity: TODO
def solution1(data):
    coords = [0, 0]
    heading = 0
    for instruction in data:
        coords, heading = travel(coords, heading, instruction)
    
    return getManhattanDist(coords)

def moveWaypointN(coords, waypoint, magnitude):
    return [coords, [waypoint[0], waypoint[1] + magnitude]]
def moveWaypointS(coords, waypoint, magnitude):
    return [coords, [waypoint[0], waypoint[1] - magnitude]]
def moveWaypointE(coords, waypoint, magnitude):
    return [coords, [waypoint[0] + magnitude, waypoint[1]]]
def moveWaypointW(coords, waypoint, magnitude):
    return [coords, [waypoint[0] - magnitude, waypoint[1]]]
def rotateWaypointL(coords, waypoint, magnitude):
    rad = magnitude * math.pi / 180
    x, y = waypoint
    xPrime = (x * math.cos(rad)) - (y * math.sin(rad))
    yPrime = (y * math.cos(rad)) + (x * math.sin(rad))
    return [coords, [xPrime, yPrime]]
def rotateWaypointR(coords, waypoint, magnitude):
    rad = -magnitude * math.pi / 180
    x, y = waypoint
    xPrime = (x * math.cos(rad)) - (y * math.sin(rad))
    yPrime = (y * math.cos(rad)) + (x * math.sin(rad))
    return [coords, [xPrime, yPrime]]
def moveShipToWaypoint(coords, waypoint, magnitude):
    return [[coords[0] + (waypoint[0] * magnitude), coords[1] + (waypoint[1] * magnitude)], waypoint]
# function TODO
# time complexity: TODO
# space complexity: TODO
def travelByWaypoint(coords, waypoint, instruction):
    options = {
        'N': moveWaypointN,
        'S': moveWaypointS,
        'E': moveWaypointE,
        'W': moveWaypointW,
        'L': rotateWaypointL,
        'R': rotateWaypointR,
        'F': moveShipToWaypoint
    }
    return options[instruction[0]](coords, waypoint, int(instruction[1:]))

# function TODO
# time complexity: TODO
# space complexity: TODO
def solution2(data):
    coords = [0, 0]
    waypoint = [10, 1]
    for instruction in data:
        coords, waypoint = travelByWaypoint(coords, waypoint, instruction)
    
    return getManhattanDist(coords)

if __name__ == "__main__":

    print(f'Sample 1 Part 1 Solution: {solution1(example1)} should be 25')
    print(f'Part 1 Solution: {solution1(data)}')
    print()
    print(f'Sample 1 Part 2 Solution: {solution2(example1)} should be 286')
    print(f'Part 2 Solution: {solution2(data)}')