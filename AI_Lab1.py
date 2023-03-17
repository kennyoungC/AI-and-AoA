# 8 queen problem (breadth first search)

from collections import deque
# incremental state. The initial state has no queens on the board., 
initial_state = [None for _ in range(8)]

def get_successors(state):
    successors = []
    # looping through the board.
    for col in reversed(range(8)): 
        if state[col] is None:
            for row in reversed(range(8)):
                if all(state[c] != row and abs(col - c) != abs(row - state[c])
                       for c in (range(8)) if state[c] is not None):
                    successor = state.copy()
                    successor[col] = row
                    successors.append(successor)
            break
    return successors

def is_goal(state):
    # checks in the state, that the range 0-7 is not none. 
    # if it has no two queens on the same row, column, or diagonal
    # if yes, it will return true. that the goal is reached. otherwise false. 
    return all(state[c] is not None for c in range(8))


def breadth_first_search():
    queue = deque([initial_state])
    while queue:
        state = queue.popleft()
        print(state)
        if is_goal(state):
            return state
        queue.extend(get_successors(state))

solution = breadth_first_search()

if solution:
    print("Solution found:", solution)
    for row in range(8):
        for col in range(8):
            if solution[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution found")
