def alpha_beta(depth, node_index, maximizing_player, values, alpha, beta):
    if depth == 3:
        return values[node_index]
    if maximizing_player:
        best = -9999
        for i in range(2):
            value = alpha_beta(depth + 1,
                               node_index * 2 + i,
                               False,
                               values,
                               alpha,
                               beta)
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 9999
        for i in range(2):
            value = alpha_beta(depth + 1,
                               node_index * 2 + i,
                               True,
                               values,
                               alpha,
                               beta)
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
values = [3, 4, 9, 9, 1, 7, 0, -1]
result = alpha_beta(0, 0, True, values, -9999, 9999)
print("Optimal Value:", result)