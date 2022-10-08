import heapq
from dataclasses import dataclass, field
import problem


@dataclass(order=True)
class Node:
    cost: int
    depth: int = field(compare=False)
    state: field(compare=False)


def expand(node, operators):
    new_node_list = []
    for operator in operators:
        new_node = operator(node)
        if new_node is not None:
            new_node_list.append(new_node)
    return new_node_list


def add_to_priority_queue(nodes, new_nodes):
    for node in new_nodes:
        heapq.heappush(nodes, node)
    return nodes


def general_search(queueing_function):
    nodes = [Node(0, 0, problem.initial_state)]

    expansions = 0
    while True:
        if len(nodes) == 0:
            return None, expansions
        node = heapq.heappop(nodes)

        # print("Next best node has depth " + str(node.depth) + " and heuristic score " + str(node.cost - node.depth) + " with state:")
        # for row in node.state:
        #     print(row)

        if problem.goal_test(node.state):
            return node, expansions
        nodes = queueing_function(nodes, expand(node, problem.operators))
        expansions += 1


def main():
    # Fill in initial state with user input
    print("Please provide the initial state as a space-separated list of integers. Enter 0 for a blank. Press enter with each new row.")
    while len(problem.initial_state) == 0 or len(problem.initial_state) < len(problem.initial_state[0]):
        problem.initial_state.append([int(number) for number in input().split()])

    # Get algorithm from user input
    text = input("Select an algorithm. Choices are Uniform Cost Search (1), Misplaced Tile (2), or Manhattan Distance (3).\n")
    if text == '1':
        problem.heuristic = problem.Heuristic.NONE
    elif text == '2':
        problem.heuristic = problem.Heuristic.MISPLACED_TILE
    elif text == '3':
        problem.heuristic = problem.Heuristic.MANHATTAN_DISTANCE

    goal_node, expansions = general_search(add_to_priority_queue)
    print("Solution found! Depth was " + str(goal_node.depth) + " and " + str(expansions) + " nodes were expanded.")


if __name__ == "__main__":
    main()
