import heapq
def dijkstra(matrix, start):
    n = len(matrix)
    # Initialize distances
    distances = [float('inf')] * n
    distances[start] = 0
    # Track visited nodes
    visited = [False] * n
    # Priority queue
    queue = [(0, start)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Skip if already visited
        if visited[current_node]:
            continue

        visited[current_node] = True

        # Check neighbors
        for neighbor in range(n):
            weight = matrix[current_node][neighbor]

            # Ignore same node (0 distance)
            if weight > 0:
                new_distance = current_distance + weight

                # Update distance if shorter path found
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(queue, (new_distance, neighbor))
    return distances
# Example 5x5 distance matrix
matrix = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 17],
    [15, 35, 0, 30, 28],
    [20, 25, 30, 0, 23],
    [25, 17, 28, 23, 0]
]
# Run the algorithm
result = dijkstra(matrix, 0)
# Print results
print("Shortest distances from location 0:")
for i, d in enumerate(result):
    print("To location", i, ":", d)

