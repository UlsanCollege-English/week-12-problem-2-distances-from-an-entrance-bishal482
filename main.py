from collections import deque

def bfs_distances(graph, start):
    # If start not in graph, return empty dict
    if start not in graph:
        return {}

    dist = {start: 0}
    queue = deque([start])
    visited = {start}

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                dist[neighbor] = dist[current] + 1
                queue.append(neighbor)

    return dist


if __name__ == "__main__":
    sample_graph = {
        "Gate": ["Stage1", "Stage2"],
        "Stage1": ["Gate", "Stage3"],
        "Stage2": ["Gate"],
        "Stage3": ["Stage1"],
    }
    d = bfs_distances(sample_graph, "Gate")
    print("Distances from Gate:", d)
