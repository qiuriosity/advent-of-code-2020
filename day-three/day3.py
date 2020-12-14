import math

def find_trees(r, d):
    with open("input.txt", "r") as file:
        lines = file.readlines()[d:]

        start = 0
        trees = 0

        for i in range(0, len(lines), d):
            line = lines[i]
            start = (start + r) % 31
            if line[start] == "#":
                trees += 1

        return trees

results = [find_trees(1, 1), find_trees(3, 1), find_trees(5, 1), find_trees(7, 1), find_trees(1, 2)]
print(math.prod(results))

# R1D1
# R3D1
# R5D1
# R7D1
# R1D2
