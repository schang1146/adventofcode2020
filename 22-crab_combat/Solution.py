from collections import deque

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


def calculateScore(deck):
    score = 0
    for cardId in range(len(deck)):
        score += deck[cardId] * (cardId + 1)
    return score


def parseData(data):
    # top of deck = right
    player1 = deque()
    player2 = deque()

    addingTo = ""
    for idx in range(len(data)):
        if data[idx] == "Player 1:":
            addingTo = "player1"
        elif data[idx] == "Player 2:":
            addingTo = "player2"

        if data[idx].isdigit():
            if addingTo == "player1":
                player1.appendleft(int(data[idx]))
            elif addingTo == "player2":
                player2.appendleft(int(data[idx]))

    return [player1, player2]


def playRecursiveCombat(player1, player2, recDepth=0):
    history = {}

    while len(player1) != 0 and len(player2) != 0:
        # if game state has been seen before
        if str(player1) in history and str(player2) in history[str(player1)]:
            # player 1 wins game
            return [player1, "player1"]
        # if game state is in a new configuration
        else:
            # add round info to history
            if str(player1) in history:
                history[str(player1)].add(str(player2))
            else:
                history[str(player1)] = set([str(player2)])

            # if the value of the card drawn is <= players' card count
            if (player1[-1] <= (len(player1) - 1) and
                    player2[-1] <= (len(player2) - 1)):
                # play new game of recursive combat
                _, roundWinner = playRecursiveCombat(
                    deque([player1[i] for i in range(-1-player1[-1], -1)]),
                    deque([player2[j] for j in range(-1-player2[-1], -1)]),
                    recDepth + 1
                )
            # if someone doesn't have as many cards as the value of the card
            # drawn
            else:
                # winner of the round is player with higher value card
                if player1[-1] > player2[-1]:
                    roundWinner = "player1"
                elif player1[-1] < player2[-1]:
                    roundWinner = "player2"
                else:
                    print("Error: Both players have the same card value!")

            if roundWinner == "player1":
                player1.appendleft(player1.pop())
                player1.appendleft(player2.pop())
            elif roundWinner == "player2":
                player2.appendleft(player2.pop())
                player2.appendleft(player1.pop())

    if len(player1) == 0:
        return [player2, "player2"]
    else:
        return [player1, "player1"]


def playCombat(player1, player2):
    while len(player1) != 0 and len(player2) != 0:
        if player1[-1] > player2[-1]:
            player1.appendleft(player1.pop())
            player1.appendleft(player2.pop())
        elif player1[-1] < player2[-1]:
            player2.appendleft(player2.pop())
            player2.appendleft(player1.pop())
        else:
            print("Error: Both players have the same card value!")

    if len(player1) == 0:
        return player2
    else:
        return player1


def solution1(data):
    player1, player2 = parseData(data)
    winner = playCombat(player1, player2)
    return calculateScore(winner)


def solution2(data):
    player1, player2 = parseData(data)
    winner, _ = playRecursiveCombat(player1, player2)
    return calculateScore(winner)


if __name__ == "__main__":
    print(f'Sample 1 Part 1 Solution: {solution1(example1)} should be 306')
    print(f'Part 1 Solution: {solution1(data)}')
    print()
    print(f'Sample 1 Part 2 Solution: {solution2(example1)} should be 291')
    print(f'Part 2 Solution: {solution2(data)}')
