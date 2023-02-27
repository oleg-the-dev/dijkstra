import heapq
from typing import Dict, List, Tuple

from utils import draw_map, generate_random_data


class DijkstraAlgorithm:

    @classmethod
    def find_path(
            cls,
            data: Dict[str, List[List[int] | int]]
    ) -> Tuple[int, List[Tuple[int]]]:
        """
        Finds optimal path in a weighted matrix using Dijkstra algorithm.
        :param data: JSON (dict) object. Example:
            {
            "board": [[0, 1, 1], [10, 10, 1], [1, 1, 1]],
            "target": [0, 2]
        }
        :return: cost of a path and a path itself
        """
        board = data["board"]
        start = (0, 0)
        target = tuple(data["target"][::-1])

        n_rows, n_cols = len(board),  len(board[0])

        distances = {start: (0, [start])}
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current = heapq.heappop(priority_queue)

            if current == target:
                return distances[current]

            for neighbor in cls._get_neighbors(current, n_rows, n_cols):
                # Calculate the distance to the neighboring cell
                distance = current_distance + board[neighbor[0]][neighbor[1]]

                # Update the distances dictionary if we found a shorter path
                if neighbor not in distances or distance < distances[neighbor][0]:
                    # Update the distance and path to the neighboring cell
                    path = distances[current][1] + [neighbor]
                    distances[neighbor] = (distance, path)
                    heapq.heappush(priority_queue, (distance, neighbor))

    @classmethod
    def _get_neighbors(
            cls,
            node: Tuple[int, int],
            n_rows: int,
            n_cols: int
    ) -> List:
        """
        Get neighbors for current "node" for bidirectional movement
        (horizontal and vertical)
        :param node: current position on a board
        :param n_rows: number of rows of a board
        :param n_cols: number of columns of a board
        :return:
        """
        (r, c) = node
        neighbors = []
        if r > 0:
            neighbors.append((r - 1, c))
        if c > 0:
            neighbors.append((r, c - 1))
        if r < n_rows - 1:
            neighbors.append((r + 1, c))
        if c < n_cols - 1:
            neighbors.append((r, c + 1))
        return neighbors


if __name__ == "__main__":
    data = generate_random_data()
    cost, path = DijkstraAlgorithm.find_path(data)
    print(f"Path: {[(y, x) for x, y in path]}\nCost: {cost}")
    draw_map(data, path)
