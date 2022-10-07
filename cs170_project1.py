import heapq
from dataclasses import dataclass, field


@dataclass(order=True)
class PrioritizedItem:
    cost: int
    state: str = field(compare=False)


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
