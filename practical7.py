def water_jug_dfs():
    stack = [((0, 0), [])]
    visited = set()

    while stack:
        (jug1, jug2), path = stack.pop()
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        path = path + [(jug1, jug2)]

        if jug1 == 2:
            return path

        next_states = [
            (4, jug2),
            (jug1, 3),
            (0, jug2),
            (jug1, 0),
            (jug1 - min(jug1, 3 - jug2), jug2 + min(jug1, 3 - jug2)),
            (jug1 + min(jug2, 4 - jug1), jug2 - min(jug2, 4 - jug1))
        ]

        for state in next_states:
            if state not in visited:
                stack.append((state, path))

    return None


solution = water_jug_dfs()
print("Solution Path:")
if solution is not None:
    for step in solution:
        print(step)
else:
    print("No solution found")