# initialize problem variables
data = []

# populate data from input file
filename = 'input.txt'
file = open(filename, 'r')
lines = file.readlines()
for line in lines:
    data.append(line)

#
def parseData(data):
    containers = set()
    rules = {}
    for line in data:
        container, contents = line.split('contain')
        container = container.strip()[:-5]
        contents = contents.split(',')

        containers.add(container)
        rules[container] = {}
        for content in contents:
            if content.strip()[:2] != 'no':
                numBags, bag = content.strip().split(' ', 1)
                contentDescription = bag.rstrip('.').rsplit(' ', 1)[0]
                rules[container][contentDescription] = int(numBags)

    return [containers, rules]

containers, rules = parseData(data)

def dfs(rules):
    seen = set()
    stack = [[color] for color in rules.keys()]
    canContainGold = set()
    while len(stack) > 0:
        currentPath = stack.pop(-1)
        currentColor = currentPath[-1]
        seen.add(currentColor)

        for color in rules[currentColor].keys():
            if color == 'shiny gold':
                for history in currentPath:
                    canContainGold.add(history)
            
            elif color not in seen:
                stack.append(currentPath + [color])

            else:
                if color in canContainGold:
                    for history in currentPath:
                        canContainGold.add(history)

    return canContainGold

def totalBags(rules):
    total = 0
    stack = [('shiny gold', 1)]
    while len(stack) > 0:
        currentColor, currentMultiplier = stack.pop()

        for color in rules[currentColor].keys():
            total += rules[currentColor][color] * currentMultiplier
            stack.append((color, currentMultiplier * rules[currentColor][color]))

    return total



# print(len(dfs(rules)))

print(totalBags(rules))