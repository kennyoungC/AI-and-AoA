from queue import Queue

def bfs(start, goal):
    visited = set()
    q = Queue()
    q.put((start, []))

    while not q.empty():
        (state, path) = q.get()
        if state == goal:
            return path
        visited.add(state)

        # The possible next moves
        for i in range(3):
            for j in range(3):
                if i + j < 1 or i + j > 2:
                    continue
                #postion of the boat
                if state[2] == 1:
                    next_state = (state[0] - i, state[1] - j, 0, state[3] + i, state[4] + j)
                    if next_state[0] < 0 or next_state[1] < 0 or next_state[3] < 0 or next_state[4] < 0:
                        continue
                    if (next_state[0] != 0 and next_state[0] < next_state[1]) or (next_state[3] != 0 and next_state[3] < next_state[4]):
                        continue
                    if next_state in visited:
                        continue
                    q.put((next_state, path + [(i, j, 0)]))
                else:
                    next_state = (state[0] + i, state[1] + j, 1, state[3] - i, state[4] - j)
                    if next_state[0] < 0 or next_state[1] < 0 or next_state[3] < 0 or next_state[4] < 0:
                        continue
                    if (next_state[0] != 0 and next_state[0] < next_state[1]) or (next_state[3] != 0 and next_state[3] < next_state[4]):
                        continue
                    if next_state in visited:
                        continue
                    q.put((next_state, path + [(i, j, 1)]))
    return None

# Test the function
start = (0, 0, 0, 3, 3)
goal = (3, 3, 1, 0, 0)
result = bfs(start, goal)
if result is None:
    print("No solution found")
else:
    for i, step in enumerate(result):
        print(f"Step {i+1}: Move {step[0]} missionaries and {step[1]} cannibals {'from' if step[2] == 1 else 'to'} the other side")
