def tower_of_hanoi(n, source, auxiliary, destination, moves):
    if n == 1:
        moves.append(
            f"Move disk 1 from {source} to {destination}"
        )
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary, moves)
    moves.append(
        f"Move disk {n} from {source} to {destination}"
    )
    tower_of_hanoi(n - 1, auxiliary, source, destination, moves)


n = 3
moves = []
tower_of_hanoi(n, 'A', 'B', 'C', moves)
print("Solution Path:")
for move in moves:
    print(move)
print("Total Moves:", len(moves))