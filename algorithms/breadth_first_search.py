def breadth_first_search(graph_object, starting_vertex):
    output_sequence = []
    visited = [False] * len(graph_object.graph)

    queue = []

    queue.append(starting_vertex)
    visited[starting_vertex] = True

    while queue:
        vertex = queue.pop(0)
        output_sequence.append(vertex)

        for index in graph_object.graph[vertex]:
            if visited[index] == False:
                queue.append(index)
                visited[index] = True
    return output_sequence
