def traverse(graph, node, visited, log, isChanged):
    if node >= len(graph):
        return False

    if visited[node]:
        return True
    visited[node] = True
    log.append(node)

    nextNodes = graph[node]
    if len(nextNodes) == 0:
        return False
    
    if isChanged:
        if not traverse(graph, nextNodes["og"], visited, log, isChanged):
            return False
    else:
        for n in nextNodes:
            if n == "og":
                if not traverse(graph, nextNodes[n], visited, log, False):
                    return False
            else:
                if not traverse(graph, nextNodes[n], visited, log, True):
                    return False
    
    log.remove(node)
    return True

with open("input.txt", "r") as file:
    instructions = file.readlines()
    visited = []
    index = 0
    graph = {}

    for i in range(0, len(instructions)):
        current = instructions[i]
        operation = current[:3]
        argument = int(current[4:])

        if operation == "acc":
            graph[i] = {
                "og": i + 1
            }
        if operation == "jmp":
            graph[i] = {
                "og": i + argument,
                "new": i + 1
            }
        if operation == "nop":
            graph[i] = {
                "og": i + 1,
                "new": i + argument
            }
    
    # print(graph)

    visited = {}
    for i in range(0, len(graph)):
        visited[i] = False
    log = []
    # print(traverse(graph, 0, visited, log, False))
    # print(log)

    accumulator = 0

    for i in log:
        current = instructions[i]
        operation = current[:3]
        argument = int(current[4:])

        if operation == "acc":
            accumulator += argument
    
    print(accumulator)
