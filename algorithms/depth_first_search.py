def visit(graph, starting_vertex, visited_list):
    visited_list[starting_vertex] = True
    output_sequence = [starting_vertex]

    for vertex in graph[starting_vertex]:
        if visited_list[vertex] == False:
            output_sequence += visit(graph, vertex, visited_list)
    return output_sequence


def depth_first_search(graph_object, starting_vertex):
    visited = [False] * len(graph_object.graph)

    return visit(graph_object.graph, starting_vertex, visited)
