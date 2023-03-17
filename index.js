let graph = []
let vertices_no = 0
let vertices = []

function add_vertex(v) {
  if (!vertices.includes(v)) {
    vertices_no++
    vertices.push(v)

    if (vertices_no > 1) {
      for (let vertex of graph) {
        vertex.push(0)
      }
    }

    let graph_vertices = Array(vertices_no).fill(0)
    graph.push(graph_vertices)
  }
}

function add_edge(vertex1, vertex2, e) {
  if (vertices.includes(vertex1) && vertices.includes(vertex2)) {
    let key1 = vertices.indexOf(vertex1)
    let key2 = vertices.indexOf(vertex2)
    graph[key1][key2] = e
  }
}

function print_graph() {
  for (let i = 0; i < vertices_no; i++) {
    for (let j = 0; j < vertices_no; j++) {
      if (graph[i][j] != 0) {
        console.log(
          `${vertices[i]} connects to ${vertices[j]} edge = ${graph[i][j]}`
        )
      }
    }
  }
}

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

const list = {
  A: ["B", "D", "E"],
  B: ["A", "C"],
  C: ["B"],
  D: ["E"],
  E: ["D", "E"],
}

const visited = new Set()

function nested_depth(visited, graph, node) {
  if (!visited.has(node)) {
    console.log({ node })
    visited.add(node)
    for (const neighbour of graph[node]) {
      nested_depth(visited, graph, neighbour)
    }
  }
}

nested_depth(visited, list, "C")
