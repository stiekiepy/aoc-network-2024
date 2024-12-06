
"""
remove element, check sub lists
Iterate through a list, removing one item at a time, starting
with the first item, and creating a new list. 
Output of the code looks like this: 

[[6, 4, 4, 1], [8, 4, 4, 1], [8, 6, 4, 1], [8, 6, 4, 1], [8, 6, 4, 4]]
[[3, 6, 7, 9], [1, 6, 7, 9], [1, 3, 7, 9], [1, 3, 6, 9], [1, 3, 6, 7]]
"""
# reports = [
#     [8, 6, 4, 4, 1],
#     [1, 3, 6, 7, 9],
# ]

reports = [
    [2,3,-2,4,1],
    [-1,-2,1,-2,-2]
]
def combs(items):
    out = []
    # print(items)
    for i in range(len(items)):
        inner = []
        for j in range(len(items)):
            if j != i:
                inner.append(items[j])
        out.append(inner)
    return out

for report in reports:
    print(combs(report))