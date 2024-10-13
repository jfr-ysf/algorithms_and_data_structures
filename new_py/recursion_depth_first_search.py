def depth_first_print(graph, source):
    print(source)
    for neighbor in graph[source]:
        depth_first_print(graph, neighbor)

graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

depth_first_print(graph, 'a')  # Output: a c e b d f
