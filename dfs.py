import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

visited = [False] * 1000


def dfs(s):  # function for DFS
    visited[s] = True
    print(s, end=" ")
    for n in graph[s]:
        if visited[n] == False:
            dfs(n)


x = input()
n = x[0]
e = x[2]
print("Number of nodes: " + n + "\nNumber of edges: " + e)
graph = {}
for i in range(int(e)):
    s = input()
    a = int(s[0])
    b = int(s[2])
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)

for vertex in graph:
    e = []
    for edges in graph[vertex]:
        e.append(edges)
    print(vertex, "->", e)

dfs(5)
