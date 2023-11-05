#10 list
lists = [[] for _ in range(10)]

for i in range(10):
    for j in range(50):
        lists[i].append(j)

for lst in lists:
    print(lst)
