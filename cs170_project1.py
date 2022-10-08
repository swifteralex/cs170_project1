import heapq
from dataclasses import dataclass, field
from enum import Enum
import copy


@dataclass(order=True)
class Node:
    cost: int
    depth: int = field(compare=False)
    state: list = field(compare=False)
    blank_pos: list = field(compare=False)


class Heuristic(Enum):
    NONE = 0
    MISPLACED_TILE = 1
    MANHATTAN_DISTANCE = 2


def expand(node):
    new_node_list = []
    blank_i = node.blank_pos[0]
    blank_j = node.blank_pos[1]
    if node.blank_pos[0] > 0:  # Check if moving blank up is valid
        new_node = copy.deepcopy(node)
        new_node.depth += 1
        new_node.state[blank_i - 1][blank_j] = 0
        new_node.state[blank_i][blank_j] = node.state[blank_i - 1][blank_j]
        new_node.blank_pos[0] -= 1
        new_node.cost = new_node.depth + heuristic_score(new_node)
        new_node_list.append(new_node)
    if node.blank_pos[0] + 1 < len(node.state):  # Check if moving blank down is valid
        new_node = copy.deepcopy(node)
        new_node.depth += 1
        new_node.state[blank_i + 1][blank_j] = 0
        new_node.state[blank_i][blank_j] = node.state[blank_i + 1][blank_j]
        new_node.blank_pos[0] += 1
        new_node.cost = new_node.depth + heuristic_score(new_node)
        new_node_list.append(new_node)
    if node.blank_pos[1] > 0:  # Check if moving blank left is valid
        new_node = copy.deepcopy(node)
        new_node.depth += 1
        new_node.state[blank_i][blank_j - 1] = 0
        new_node.state[blank_i][blank_j] = node.state[blank_i][blank_j - 1]
        new_node.blank_pos[1] -= 1
        new_node.cost = new_node.depth + heuristic_score(new_node)
        new_node_list.append(new_node)
    if node.blank_pos[1] + 1 < len(node.state):  # Check if moving blank right is valid
        new_node = copy.deepcopy(node)
        new_node.depth += 1
        new_node.state[blank_i][blank_j + 1] = 0
        new_node.state[blank_i][blank_j] = node.state[blank_i][blank_j + 1]
        new_node.blank_pos[1] += 1
        new_node.cost = new_node.depth + heuristic_score(new_node)
        new_node_list.append(new_node)
    return new_node_list


def heuristic_score(node):
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


heuristic = Heuristic.MANHATTAN_DISTANCE
initial_node = Node(0, 0, [], [])


def main():
    # Fill in initial state with user input
    print("Please provide the initial state as a space-separated list of integers. Enter 0 for a blank. Press enter with each new row.")
    while len(initial_node.state) == 0 or len(initial_node.state) < len(initial_node.state[0]):
        initial_node.state.append([int(number) for number in input().split()])

    # Find position of blank space
    for i in range(len(initial_node.state)):
        for j in range(len(initial_node.state)):
            if initial_node.state[i][j] == 0:
                initial_node.blank_pos = [i, j]

    print(expand(initial_node))


if __name__ == "__main__":
    main()

# item1 = PrioritizedItem(10, "1 2 4 5")
# item2 = PrioritizedItem(15, " test")
# item3 = PrioritizedItem(5, "b 1 2 3 4")
# item4 = PrioritizedItem(5, "1 4")
# h = []
# heapq.heappush(h, item1)
# heapq.heappush(h, item2)
# heapq.heappush(h, item3)
# heapq.heappush(h, item4)
# print(heapq.heappop(h))
# print(heapq.heappop(h))
# print(heapq.heappop(h))
# print(heapq.heappop(h))
#
# found_states = {}
# found_states[item1.state] = True
# found_states[item2.state] = True
#
# print(found_states.get(item3.state))
# print(found_states.get(item2.state))
