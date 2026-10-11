import random
distance = [
[0, 10, 15, 20],
[10, 0, 35, 25],
[15, 35, 0, 30],
[20, 25, 30, 0]
]
cities = [0, 1, 2, 3]
def calculate_distance(route):
	total = 0
	for i in range(len(route)-1):
		total += distance[route[i]][route[i+1]]
	total += distance[route[-1]][route[0]]
	return total
def generate_neighbors(route):
	neighbors = []
	for i in range(len(route)):
		for j in range(i+1, len(route)):
			new_route = route.copy()
			new_route[i], new_route[j] = (new_route[j], new_route[i])
			neighbors.append(new_route)
	return neighbors
def local_beam_search(k, iterations):
	beam = []
	for i in range(k):
		route = cities.copy()
		random.shuffle(route)
		beam.append(route)
	for _ in range(iterations):
		candidates = []
		for route in beam:
			candidates.extend(generate_neighbors(route))
		candidates.sort(key=calculate_distance)
		beam = candidates[:k]
	best_route = beam[0]
	return best_route, calculate_distance(best_route)
route, cost = local_beam_search(3,10)
print("Best Route:", route)
print("Minimum Distance:", cost)