def countchildren(parent, graph):
    children = graph[parent]
    
    if len(children) == 0:
        return 0
    
    total = 0
    for child in children:
        name = child[0]
        count = child[1]
        # print(name, count)
        total += count + count * countchildren(name, graph)
        # print(child, total)
    
    return total

with open("input.txt", "r") as file:
    rules = file.readlines()
    graph = {}

    for rule in rules:
        content = rule.split(" contain ")
        end = content[0].find("bag")
        parent = content[0][:end - 1]
        children = []

        childcontent = content[1].split(", ")
        
        for child in childcontent:
            if child[0].isdigit():
                e = child.find("bag")
                c = child[2:e - 1]
                n = int(child[0])
                children.append((c,n))

        graph[parent] = children
        # print(graph)
    
    print(countchildren("shiny gold", graph))
