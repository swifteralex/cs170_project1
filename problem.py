import copy
from enum import Enum


class Heuristic(Enum):
    NONE = 0
    MISPLACED_TILE = 1
    MANHATTAN_DISTANCE = 2


def __heuristic_score(node):
    score = 0
    if heuristic == Heuristic.NONE:
        return score
    elif heuristic == Heuristic.MISPLACED_TILE:
        for i in range(len(node.state)):
            for j in range(len(node.state)):
                if node.state[i][j] == 0:
                    continue
                if node.state[i][j] != i * len(node.state) + j + 1:
                    score += 1
        return score
    elif heuristic == Heuristic.MANHATTAN_DISTANCE:
        for i in range(len(node.state)):
            for j in range(len(node.state)):
                if node.state[i][j] == 0:
                    continue
                goal_i = (node.state[i][j] - 1) // len(node.state)
                goal_j = (node.state[i][j] - 1) % len(node.state)
                score += abs(goal_i - i) + abs(goal_j - j)
        return score


def __find_blank(node):
    for i in range(len(node.state)):
        for j in range(len(node.state)):
            if node.state[i][j] == 0:
                return i, j


def __up_op(node):
    blank_i, blank_j = __find_blank(node)
    if blank_i == 0:
        return None
    new_node = copy.deepcopy(node)
    new_node.depth += 1
    new_node.state[blank_i - 1][blank_j] = 0
    new_node.state[blank_i][blank_j] = node.state[blank_i - 1][blank_j]
    new_node.cost = new_node.depth + __heuristic_score(new_node)
    return new_node


def __down_op(node):
    blank_i, blank_j = __find_blank(node)
    if blank_i + 1 >= len(node.state):
        return None
    new_node = copy.deepcopy(node)
    new_node.depth += 1
    new_node.state[blank_i + 1][blank_j] = 0
    new_node.state[blank_i][blank_j] = node.state[blank_i + 1][blank_j]
    new_node.cost = new_node.depth + __heuristic_score(new_node)
    return new_node


def __left_op(node):
    blank_i, blank_j = __find_blank(node)
    if blank_j == 0:
        return None
    new_node = copy.deepcopy(node)
    new_node.depth += 1
    new_node.state[blank_i][blank_j - 1] = 0
    new_node.state[blank_i][blank_j] = node.state[blank_i][blank_j - 1]
    new_node.cost = new_node.depth + __heuristic_score(new_node)
    return new_node


def __right_op(node):
    blank_i, blank_j = __find_blank(node)
    if blank_j >= len(node.state):
        return None
    new_node = copy.deepcopy(node)
    new_node.depth += 1
    new_node.state[blank_i][blank_j + 1] = 0
    new_node.state[blank_i][blank_j] = node.state[blank_i][blank_j + 1]
    new_node.cost = new_node.depth + __heuristic_score(new_node)
    return new_node


def goal_test(state):
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] == 0:
                continue
            if state[i][j] != i * len(state) + j + 1:
                return False
    return True


initial_state = []
heuristic = Heuristic.NONE
operators = [__up_op, __down_op, __left_op, __right_op]
