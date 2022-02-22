import pprint as pp

with open('e_elaborate.in.txt', 'r') as a_file:
    a_example = a_file.read().splitlines()

C = a_example[0]

liked = {}
disliked = {}

for liked_preference in a_example[1::2]:
    ingredients = liked_preference.split()[1:]
    for ingredient in ingredients:
        if ingredient not in liked:
            liked[ingredient] = 1
        else:
            liked[ingredient] += 1

for disliked_preference in a_example[2::2]:
    ingredients = disliked_preference.split()[1:]
    for ingredient in ingredients:
        if ingredient not in disliked:
            disliked[ingredient] = 1
        else:
            disliked[ingredient] += 1

pp.pprint(liked)
pp.pprint(disliked)
