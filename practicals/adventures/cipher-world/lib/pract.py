import os

path = os.path.realpath(__file__)
#print(os.path.dirname(path))

dir = "/Users/liamcoles/Projects/skills_workshops/practicals/adventures/cipher-world/char_sets"

os.chdir(dir)
f = open("character_set1.txt")
new_dict = {}

for line in f:
    print(line.replace('\n','')[3:5])
    if 'character' not in line:
        new_dict[line[0]] = line.replace('\n','')[3:5]


print(new_dict)

