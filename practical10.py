def minimax(depth, is_maximizing):
    if depth == 0:
        return 0

    if is_maximizing:
        best = -1000
        for i in range(2):
            score = minimax(depth - 1, False)
            best = max(best, score)
        return best
    else:
        best = 1000
        for i in range(2):
            score = minimax(depth - 1, True)
            best = min(best, score)
        return best


depth = 3
result = minimax(depth, True)
print("Optimal Utility Value:", result)