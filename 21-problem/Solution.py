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


def parseData(data):
    parsedData = []
    for line in data:
        ingredients, allergens = line.split(' (')
        ingredients = ingredients.split(' ')
        allergens = allergens[9:-1].split(', ')
        parsedData.append({
            'ingredients': ingredients,
            'allergens': allergens
        })
    return parsedData


def getPossibleTranslations(parsedData):
    possibleTranslations = {}
    ingredientsDeciphered = set()
    for data in parsedData:
        for allergen in data['allergens']:
            if allergen in possibleTranslations:
                newPossibilities = set()
                for ingredient in data['ingredients']:
                    if ingredient in possibleTranslations[allergen]:
                        newPossibilities.add(ingredient)
                possibleTranslations[allergen] = newPossibilities
            else:
                possibleTranslations[allergen] = set(data['ingredients'])
                for ingredient in ingredientsDeciphered:
                    if ingredient in possibleTranslations[allergen]:
                        possibleTranslations[allergen].remove(ingredient)

            if len(possibleTranslations[allergen]) == 1:
                ingredientDeciphered = list(possibleTranslations[allergen])[0]
                ingredientsDeciphered.add(ingredientDeciphered)

                for otherAllergen in possibleTranslations:
                    if otherAllergen != allergen:
                        if ingredientDeciphered in possibleTranslations[otherAllergen]:
                            possibleTranslations[otherAllergen].remove(
                                ingredientDeciphered)

    print(f'ingredientsDeciphered = {ingredientsDeciphered}')

    return possibleTranslations


def formatIngredientsForPart2(ingredients):
    pass


def solution1(data):
    parsedData = parseData(data)
    # print(f'parsedData = {parsedData}')

    possibleTranslations = getPossibleTranslations(parsedData)
    # print(f'possibleTranslations = {possibleTranslations}')

    possibleAllergicIngredients = set()
    for allergen in possibleTranslations:
        possibleAllergicIngredients = possibleAllergicIngredients.union(
            possibleTranslations[allergen])
    # print(f'possibleAllergicIngredients = {possibleAllergicIngredients}')

    output = 0
    for recipe in parsedData:
        for ingredient in recipe['ingredients']:
            if ingredient not in possibleAllergicIngredients:
                output += 1
    return output


def solution2(data):
    parsedData = parseData(data)
    # print(f'parsedData = {parsedData}')

    possibleTranslations = getPossibleTranslations(parsedData)
    print(f'possibleTranslations = {possibleTranslations}')

    possibleAllergicIngredients = set()
    for allergen in possibleTranslations:
        possibleAllergicIngredients = possibleAllergicIngredients.union(
            possibleTranslations[allergen])
    print(f'possibleAllergicIngredients = {possibleAllergicIngredients}')

    return formatIngredientsForPart2(possibleAllergicIngredients)


if __name__ == "__main__":

    print(f'Sample 1 Part 1 Solution: {solution1(example1)} should be 5')
    print(f'Part 1 Solution: {solution1(data)}')
    print()
    print(
        f'Sample 1 Part 2 Solution: {solution2(example1)} should be mxmxvkd,sqjhc,fvjkl')
    print()
    print(f'Part 2 Solution: {solution2(data)}')
