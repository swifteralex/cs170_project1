import heapq
from dataclasses import dataclass, field


@dataclass(order=True)
class PrioritizedItem:
    cost: int
    state: list = field(compare=False)
    blank_pos: list = field(compare=False)


def expand(node):
    list = []

    return list


def main():
    initial_node = PrioritizedItem(0, [], [])

    # Fill in initial state with user input
    print("Please provide the initial state as a space-separated list of integers. Enter 0 for a blank. Press enter with each new row.")
    while len(initial_node.state) == 0 or len(initial_node.state) < len(initial_node.state[0]):
        initial_node.state.append([int(number) for number in input().split()])

    # Find position of blank space
    for i in range(len(initial_node.state)):
        for j in range(len(initial_node.state)):
            if initial_node.state[i][j] == 0:
                initial_node.blank_pos = [i, j]

    print(initial_node.state)
    print(initial_node.blank_pos)
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
