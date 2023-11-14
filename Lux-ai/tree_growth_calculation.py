from math import ceil

tree = 481
regrowthRate = 1.035

for turn in range(1,3):
    tree *= regrowthRate
    tree = ceil(tree)
    tree = min(500, tree)
    print(tree)