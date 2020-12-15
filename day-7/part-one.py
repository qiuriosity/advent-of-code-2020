def findancestors(child, graph):
    parents = []
    for i in graph:
        if child in graph[i]:
            parents.append(i)
    
    if len(parents) == 0:
        return parents
    
    ancestors = parents
    # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHSDASJDKFALSDKJFLAJSDFLKJASDL;FJK;AD
    for parent in parents:
        # print(parent)
        grandparents = findancestors(parent, graph)
        ancestors += grandparents
    
    return set(ancestors)

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
                children.append(c)

        # print(children)
        graph[parent] = children
    
    print(len(findancestors("shiny gold", graph)))
