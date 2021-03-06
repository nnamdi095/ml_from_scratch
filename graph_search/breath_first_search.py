from graph import Digraph, Node, Edge

def build_city_graph(graph_type):
    providence = Node('providence')
    boston = Node('boston')
    new_york = Node('new york')
    denver = Node('denver')
    phoenix = Node('phoenix')
    chicago = Node('chicago')
    los_angeles = Node('los angeles')

    edges = []
    edges.append(Edge(providence, boston))
    edges.append(Edge(providence, new_york))
    edges.append(Edge(denver, phoenix))
    edges.append(Edge(denver, new_york))
    edges.append(Edge(new_york, chicago))
    edges.append(Edge(chicago, denver))
    edges.append(Edge(chicago, phoenix))
    edges.append(Edge(boston, providence))
    edges.append(Edge(boston, new_york))
    edges.append(Edge(los_angeles, boston))

    graph = graph_type()
    graph.add_node(providence)
    graph.add_node(boston)
    graph.add_node(new_york)
    graph.add_node(denver)
    graph.add_node(phoenix)
    graph.add_node(chicago)
    graph.add_node(los_angeles)

    for edge in edges:
        graph.add_edge(edge)

    return graph

def print_path(path):
    names=[]
    for loc in path:
        names.append(loc.get_name())
    return '->'.join(names)


def bfs(graph:Digraph, start, end, to_print=False):
    
    init_path = [start]

    # queue is a list of paths
    path_queue = [init_path]

    while len(path_queue) != 0:

        tmp_path = path_queue.pop(0)
        if to_print:
            print(f'current bfs path: {print_path(tmp_path)}')
        
        last_node = tmp_path[-1]
        if last_node == end:
            return tmp_path
        for next_node in graph.get_children(last_node):
            if next_node not in tmp_path:
                new_path = tmp_path + [next_node]
                path_queue.append(new_path)

    return None

def shortest_path(graph, start, end, to_print=False):
    return bfs(graph, start, end, to_print)

def test_bfs(source, dest):
    graph = build_city_graph(Digraph)
    sp = shortest_path(graph, graph.get_node(source), graph.get_node(dest), to_print=True)

    if sp != None:
        print(f'shortest path from {source} to {dest} is {print_path(sp)}')
    else:
        print(f'there is no path from {source} to {dest}')


if __name__ == "__main__":
    graph = build_city_graph(Digraph)
    # print(graph)
    test_bfs('boston', 'phoenix')