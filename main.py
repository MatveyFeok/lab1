import json

file = open("pokemon_full.json")
pokemon_full = file.read()
print("Общее количество символов в файле:", len(pokemon_full))
file.close()

counter = 0
for symbol in pokemon_full:
    if symbol.isalnum():
        counter += 1
print("Общее количесто символов без пробелов и знаков препинания:", counter)

objects = json.loads(pokemon_full)
max_description = 0
max_words = 0
pokemon_name = ""
abilities = ""
for profile in objects:
    description = profile["description"]
    for skills in profile["abilities"]:
        if len(skills.split()) > max_words:
            max_words = len(skills.split())
            abilities = skills
    if len(description) > max_description:
        max_description = len(description)
        pokemon_name = profile["name"]
print("Наиболее длинное описание у: ", pokemon_name)
print("Больше всего слов содержит умение:", abilities)