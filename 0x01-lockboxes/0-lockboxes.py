#!/usr/bin/python3
"""Method to determine if all boxes can be opened"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened
    """
    if not boxes or not boxes[0]:
        return False

    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if 0 <= key < num_boxes and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
