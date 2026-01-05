num = int(input())

for i in range(num):
    x = input()
    y = input()
    data = [
    (1, 2, "banana"),
    (2, -1, "apple"),
    (1, 2, "banana"),
    (1, 2, "apple"),
    (1, 2, "apple"),
    (5, 5, "coke"),
    (1, 2, "apple")
    ]

storage = {}

for x, y, item in data:
    pos = (x, y)
    if pos not in storage:
        storage[pos] = set()
    storage[pos].add(item)

item_counts = {pos: len(items) for pos, items in storage.items()}

storage, item_counts
