from collections import deque
def get_neighbors(state):
    neighbors = []
    index = state.index(0)
    row = index // 3
    col = index % 3
    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]
    for move in moves:
        new_row = row + move[0]
        new_col = col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[index], new_state[new_index] = (
                new_state[new_index],
                new_state[index]
            )
            neighbors.append(tuple(new_state))
    return neighbors


def bfs(start, goal):
    queue = deque()
    queue.append((start, []))
    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path + [current]

        for neighbour in get_neighbors(current):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, path + [current]))

    return None


initial_state = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)
goal_state = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

solution = bfs(initial_state, goal_state)
if solution is None:
    print("No solution found.")
else:
    print("Solution Path:")
    for state in solution:
        print(state)