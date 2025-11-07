immutable_set = frozenset([1, 2, 3, 3, 4, 4, 5])
print(immutable_set)  # frozenset({1, 2, 3, 4, 5})
# immutable_set.add(6)  # This will raise an error because frozensets are immutable
# immutable_set.remove(3)  # This will also raise an error because frozensets are immutable
print(len(immutable_set))  # 5
for num in immutable_set:
    print(num)