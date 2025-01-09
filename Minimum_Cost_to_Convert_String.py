class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        def adjacencyList(v, edges):
            dict = {i: [] for i in range(v)}

            for x, y, z in edges:
                dict[x].append((y, z))

            return dict


        def dijkstra(graph, source):
            distances = {i: float('inf') for i in range(26)}
            distances[source] = 0
            priority_queue = [(0, source)]

            while priority_queue:
                current_distance, current_vertex = heappop(priority_queue)
                if current_distance > distances[current_vertex]:
                    continue

                for neighbor, weight in graph[current_vertex]:
                    distance = current_distance + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heappush(priority_queue, (distance, neighbor))

            return distances

        edges = [(ord(o) - 97, ord(c) - 97, w) for o, c, w in zip(original, changed, cost)]
        graph = adjacencyList(26, edges)
        diff = [(ord(s) - 97, ord(t) - 97) for s, t in zip(source, target) if s != t]

        all_costs = []
        for i in range(26):
            distances = dijkstra(graph, i)
            all_costs.append(distances)

        total_distance = 0
        for u, v in diff:
            cost = all_costs[u][v]
            if cost == float('inf'):
                return -1
            total_distance += cost

        return total_distance
