from queue import PriorityQueue

goal = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 0))

# Pre-calculate goal positions
goal_pos = {}
for i in range(3):
    for j in range(3):
        goal_pos[goal[i][j]] = (i, j)

def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value!= 0:
                x, y = goal_pos[value]
                distance += abs(i - x) + abs(j - y)
    return distance

def get_neighbors(state):
    neighbors = []
    state_list = [list(row) for row in state]

    # Find blank (0) position
    for i in range(3):
        for j in range(3):
            if state_list[i][j] == 0:
                x, y = i, j

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state_list]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors

def astar(start):
    pq = PriorityQueue()
    pq.put((heuristic(start), 0, start))
    visited = set()

    while not pq.empty():
        f, g, current = pq.get()

        if current == goal:
            print("Goal State Reached")
            return

        if current in visited:
            continue

        visited.add(current)

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                h = heuristic(neighbor)
                pq.put((g + 1 + h, g + 1, neighbor))

    print("No solution found")

# Start state
start = ((1, 7, 3),
         (4, 0, 6),
         (2, 5, 8))

astar(start)