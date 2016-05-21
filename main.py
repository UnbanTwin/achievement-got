import random

with open('verbs.txt') as f:
    verbs = f.readlines()

with open('nouns.txt') as f:
    nouns = f.readlines()
print("Achievement got: " + random.choice(verbs).replace('\n', '') + " " + random.choice(nouns).replace('\n', ''))
