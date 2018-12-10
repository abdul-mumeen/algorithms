def breadth_first_search(graph_object, starting_vertex):
    output_sequence = []
    visited = [False] * len(graph_object.graph)

    queue = []

    queue.append(starting_vertex)
    visited[starting_vertex] = True

    while queue:
        next_vertex = queue.pop(0)
        output_sequence.append(next_vertex)

        for vertex in graph_object.graph[next_vertex]:
            if visited[vertex] == False:
                queue.append(vertex)
                visited[vertex] = True
    return output_sequence
