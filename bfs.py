import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


def bfs(s):  # function for BFS
    visited = [False] * 1000
    queue = []
    queue.append(s)
    visited[s] = True

    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")
        for n in graph[m]:
            if visited[n] == False:
                visited[n] = True
                queue.append(n)


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

bfs(5)
