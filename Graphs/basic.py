from collections import defaultdict
n =8
A = [[2,3],[5,7],[1,6],[4,0],[3,5],[2,1],[0,3],[1,5]]
# creation of adjacency matrix
M=[]
for i in range(n):
    M.append([0]*n)
for u,v in A:
    M[u][v] = 1
print(M)

print()
# creation of adjacency list
D = defaultdict(list)
for u,v in A:
    D[u].append(v)

print(D)
print(D[2])