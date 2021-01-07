# initialize problem variables
data = []
example1 = []
example2 = []

# populate sample data from example file(s)
filename = 'example1.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        example1.append(line.strip())
filename = 'example2.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        example2.append(line.strip())

# populate data from input file
filename = 'input.txt'
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        data.append(line.strip())


def addParenthesisOld(expression, op):
    newExpression = ""
    left = ""

    currentExpression = ""
    pointer = 0
    while pointer < len(expression):
        if expression[pointer] == "(":
            start = pointer
            parenthesesLevel = 1
            while parenthesesLevel != 0:
                pointer += 1
                if expression[pointer] == "(":
                    parenthesesLevel += 1
                elif expression[pointer] == ")":
                    parenthesesLevel -= 1
            currentExpression = "(" + \
                addParenthesis(expression[start+1:pointer]) + ")"
        elif expression[pointer] == "+":
            newExpression += f"({left}+"
            left = ""

            # add next until "*" is seen
            flag = True
            while flag:
                if expression[pointer+2].isdigit():
                    if expression[pointer+4] == "+":
                        newExpression += expression[pointer:pointer+5]
                        pointer += 5
                    elif expression[pointer+4] == "*":
                        newExpression += f"{expression[pointer:pointer+3]}*"
                        pointer += 3
                elif expression[pointer+2] == "(":
                    start = pointer
                    parenthesesLevel = 1
                    while parenthesesLevel != 0:
                        pointer += 1
                        if expression[pointer] == "(":
                            parenthesesLevel += 1
                        elif expression[pointer] == ")":
                            parenthesesLevel -= 1
                    currentExpression = "(" + \
                        addParenthesis(expression[start+1:pointer]) + ")"

        elif expression[pointer] == "*":
            newExpression += f"{left}*"
            left = ""
        elif expression[pointer].isdigit():
            currentExpression = expression[pointer]

        if currentExpression != "":
            if left == "":
                left = currentExpression
            currentExpression = ""

        pointer += 1

    return newExpression


def addParenthesis(expression, op):
    newExpression = ""
    left = ""

    pointer = 0
    while pointer < len(expression):
        if expression[pointer] == "(":
            start = pointer
            parenthesesLevel = 1
            while parenthesesLevel > 0:
                pointer += 1
                if expression[pointer] == "(":
                    parenthesesLevel += 1
                elif expression[pointer] == ")":
                    parenthesesLevel -= 1
            left += f"({addParenthesis(expression[start+1:pointer], op)})"
        elif expression[pointer] == "+":
            opChanged = False
            while not opChanged and pointer < len(expression):
                if expression[pointer] == "(":
                    start = pointer
                    parenthesesLevel = 1
                    while parenthesesLevel > 0:
                        pointer += 1
                        if expression[pointer] == "(":
                            parenthesesLevel += 1
                        elif expression[pointer] == ")":
                            parenthesesLevel -= 1
                    left += f"({addParenthesis(expression[start+1:pointer], op)})"
                elif expression[pointer] == "+":
                    left += expression[pointer]
                elif expression[pointer] == "*":
                    newExpression += f"({left})*"
                    left = ""
                    opChanged = True
                elif expression[pointer].isdigit():
                    left += expression[pointer]

                pointer += 1

            if pointer == len(expression):
                newExpression += f"({left})"
                left = ""
        elif expression[pointer] == "*":
            newExpression += f"{left}*"
            left = ""
        elif expression[pointer].isdigit():
            left += expression[pointer]

        pointer += 1

    newExpression += left

    return newExpression


def eval(expression, opPriority=[]):
    output = 0
    currentOp = "+"

    for op in opPriority:
        expression = addParenthesis(expression, op)

    pointer = 0
    while pointer < len(expression):
        if expression[pointer] == "(":
            start = pointer
            parenthesesLevel = 1
            while parenthesesLevel != 0:
                pointer += 1
                if expression[pointer] == "(":
                    parenthesesLevel += 1
                elif expression[pointer] == ")":
                    parenthesesLevel -= 1
            output = evalOp(output, eval(
                expression[start+1:pointer]), currentOp)
        elif expression[pointer] == "+":
            currentOp = "+"
        elif expression[pointer] == "*":
            currentOp = "*"
        elif expression[pointer].isdigit():
            output = evalOp(output, expression[pointer], currentOp)
        pointer += 1

    return output


def evalOp(n1, n2, op):
    # takes in two numbers (n1, n2) and an operator (op) all as strings
    # returns the result from evaluating the operator with the two numbers
    def add(n1, n2):
        return int(n1) + int(n2)

    def multiply(n1, n2):
        return int(n1) * int(n2)

    switchTable = {
        '+': add,
        '*': multiply,
    }
    return switchTable[op](n1, n2)


def solution1(data):
    output = 0
    for line in data:
        output += eval(line)
    return output


def solution2(data):
    output = 0
    for line in data:
        output += eval(line, ["+"])
    return output


if __name__ == "__main__":

    print(f'Sample 1 Part 1 Solution: {solution1(example1)} should be 26335')
    print(f'Part 1 Solution: {solution1(data)}')
    print()
    print(f'Sample 1 Part 2 Solution: {solution2(example2)} should be 693942')
    print(f'Part 2 Solution: {solution2(data)}')
