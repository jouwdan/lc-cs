"""Original constrained-state puzzle; a small breadth-first-search self-check."""
from collections import deque


def safe(state):
    robot, a, b, c = state
    return not (a == b != robot or b == c != robot)


def successors(state):
    robot = state[0]
    for cargo in [None, 1, 2, 3]:
        if cargo is not None and state[cargo] != robot:
            continue
        result = list(state)
        result[0] = 1 - robot
        if cargo is not None:
            result[cargo] = 1 - result[cargo]
        result = tuple(result)
        if safe(result):
            yield result


def shortest_path():
    start, goal = (0, 0, 0, 0), (1, 1, 1, 1)
    pending = deque([[start]])
    visited = {start}
    while pending:
        path = pending.popleft()
        if path[-1] == goal:
            return path
        for state in successors(path[-1]):
            if state not in visited:
                visited.add(state)
                pending.append(path + [state])
    return None


def winning_piles(piles):
    """Normal play: remove a positive number from exactly one pile."""
    if any(type(size) is not int or size < 0 for size in piles):
        raise ValueError("Pile sizes must be non-negative integers")
    # shortcut: repeated subgames are fine here, memoise or use Nim theory for larger inputs.
    for index, size in enumerate(piles):
        for removed in range(1, size + 1):
            following = list(piles)
            following[index] -= removed
            if not winning_piles(tuple(following)):
                return True
    return False


def self_check():
    expected = [(0,0,0,0), (1,0,1,0), (0,0,1,0), (1,1,1,0),
                (0,1,0,0), (1,1,0,1), (0,1,0,1), (1,1,1,1)]
    assert all(safe(state) for state in expected)
    assert not safe((1, 1, 0, 0))
    for first, second in zip(expected, expected[1:]):
        assert second in successors(first)
    path = shortest_path()
    assert path is not None and len(path) - 1 == 7
    assert not winning_piles((0, 0))
    assert not winning_piles((1, 1))
    assert not winning_piles((2, 2))
    assert winning_piles((1, 3)) and winning_piles((2, 4))
    assert [winning_piles(state) for state in [(0, 3), (1, 2), (1, 1), (1, 0)]] == [True, True, False, True]
    assert winning_piles((2, 2, 2)) and not winning_piles((0, 2, 2))
    print("State-space and pile-game checks passed: shortest crossing solution is 7 trips")


if __name__ == "__main__":
    self_check()
