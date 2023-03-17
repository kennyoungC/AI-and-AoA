def add_vertex(v):
    global graph
    global vertices_no
    global vertices

    if v not in vertices:
        vertices_no = vertices_no + 1
        vertices.append(v)

        if vertices_no > 1:
            for vertex in graph:
                vertex.append(0)

        grapth_vertices = []
        for i in range (vertices_no) :
            grapth_vertices.append(0)
        graph.append(grapth_vertices)
        

def add_edge(vertex1, vertex2, e):
    global graph
    global vertices_no
    global vertices

    if vertex1  in vertices and vertex2 in vertices: 
        key1 = vertices.index(vertex1)
        key2 = vertices.index(vertex2)
        graph[key1][key2] = e

def print_graph():
    global graph
    global vertices_no
    for i in range(vertices_no):
        for j in range(vertices_no):
            if graph[i][j] != 0:
                print(vertices[i], "connects to", vertices[j],"edge =", graph[i][j] )

vertices = []
vertices_no = 0
graph = []

add_vertex("A")
add_vertex("B")
add_vertex("C")
add_vertex("D")
add_vertex("E")

add_edge("A", "B", 2)
add_edge("A", "D", 1)
add_edge("A", "E", 4)
add_edge("B", "A", 1)
add_edge("B", "C", 3)
add_edge("D", "E", 5)

print_graph()
list = {
    'A' : ['B', 'D', 'E'],
    'B' : ['A', 'C'],
    'C' : ['B'],
    'D' : ['E'],
    'E' : ['D', 'E']
}
visited = set() 

def depth_first_search(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            depth_first_search(visited, graph, neighbour)

depth_first_search(visited, list, 'B')