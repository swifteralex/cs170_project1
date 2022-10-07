import heapq
from dataclasses import dataclass, field


@dataclass(order=True)
class PrioritizedItem:
    cost: int
    state: str = field(compare=False)


def main():
    puzzle_size = 0  # Length of each side of the puzzle
    found_states = {}  # Dictionary of seen states; used to avoid loops
    initial_state = ""  # Initial state; stored as a string of integers
    text = input("Please provide the initial state as a non-separated list of integers."
                 "Enter 0 for a blank. Press enter with each new row.\n")
    puzzle_size = len(text)
    for i in range(0, puzzle_size - 1):
        initial_state += input()
    print(initial_state)
    print(puzzle_size)


if __name__ == "__main__":
    main()

item1 = PrioritizedItem(10, "1 2 4 5")
item2 = PrioritizedItem(15, " test")
item3 = PrioritizedItem(5, "b 1 2 3 4")
item4 = PrioritizedItem(5, "1 4")
h = []
heapq.heappush(h, item1)
heapq.heappush(h, item2)
heapq.heappush(h, item3)
heapq.heappush(h, item4)
print(heapq.heappop(h))
print(heapq.heappop(h))
print(heapq.heappop(h))
print(heapq.heappop(h))

found_states = {}
found_states[item1.state] = True
found_states[item2.state] = True

print(found_states.get(item3.state))
print(found_states.get(item2.state))
