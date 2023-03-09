hobbies = {
    "Steve": ['Fashion', 'Piano', 'Reading'],
    "Patty": ['Drama', 'Magic', 'Pets'],
    "Chad": ['Puzzles', 'Pets', 'Yoga']
}


def findNameUsingHobbies(hobbiesList, hobbies):
    names = []
    for name in hobbiesList:
        if hobbies in hobbiesList[name]:
            names.append(name)
    return names


console.log(findNameUsinghobbies("Pets"))
console.log(findNameUsinghobbies("Yoga"))
