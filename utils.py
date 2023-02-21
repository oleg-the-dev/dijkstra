import random
from typing import Dict, List, NoReturn, Tuple

from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm


def generate_random_data(
        n: int = 10,
        m: int = 10
) -> Dict:
    """
    Generates JSON with a random board and a random target.
    :param n: number of rows.
    :param m: number of columns.
    :return: JSON (dict) object. Example:
        {
            "board": [[0, 1, 1], [10, 10, 1], [1, 1, 1]],
            "target": [0, 2]
        }
    """
    board = [[random.choice([1, 3, 10]) for _ in range(m)] for _ in range(n)]
    target = [random.randint(1, m - 1), random.randint(0, n - 1)]
    board[0][0] = 0
    print(f"Board: {board}\nTarget: {target}")
    return {
        "board": board,
        "target": target
    }


def draw_map(
        data: Dict[str, List[List[int] | int]],
        path: List[Tuple[int]]
) -> NoReturn:
    """
    Draws a matplotlib image of board and a path.
    :param data: JSON (dict) object. Example:
        {
            "board": [[0, 1, 1], [10, 10, 1], [1, 1, 1]],
            "target": [0, 2]
        }
    :param path: shortest path on a board from start to a target position
    :return: NoReturn
    """
    target = data["target"][::-1]
    board = data["board"]

    colors = ["whitesmoke", "lightgreen", "khaki", "lightsalmon"]
    values = [0, 1, 3, 10]
    cmap = ListedColormap(colors)
    norm = BoundaryNorm(values, 3)
    plt.imshow(board, cmap=cmap, norm=norm)

    # Add values to our pyplot
    for row, _ in enumerate(board):
        for column, _ in enumerate(board[0]):
            plt.text(
                column, row, board[row][column],
                ha="center", va="center", color="black"
            )

    # Add "Start" and "Target" text
    plt.text(0, 0, "\n\nStart", ha="center", va="center", color="black")
    plt.text(target[1], target[0], "\n\nTarget", ha="center", va="center", color="black")

    # Add line that shows our path
    path_xs, path_ys = zip(*path)
    plt.plot(path_ys, path_xs, color='red')

    # Add axis ticks, labels and a title
    plt.yticks(ticks=list(range(len(board))))
    plt.xticks(ticks=list(range(len(board[0]))))
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.title("Board")

    # Show pyplot in a different window
    plt.show()
