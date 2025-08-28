from collections import defaultdict
D = defaultdict(list)
n =8
A = [[2,3],[5,7],[1,6],[4,0],[3,5],[2,1],[0,3],[1,5],[2,4],[7,7]]
for u,v in A:
    D[v].append(u)
print(D)


def dfs_recursive(node):
    print(node)
    for neighbour in D[node]:
        if neighbour not in seen:
            seen.add(neighbour)
            dfs_recursive(neighbour)
def iterative (stack):
    while stack:
        node = stack.pop()
        print(node)
        for neighbour in D[node]:
            if neighbour not in seen:
                seen.add(neighbour)
                stack.append(neighbour)
source = 0
seen = set()
seen.add(source)
stack = [source]
dfs_recursive(source)
print()
iterative(stack)