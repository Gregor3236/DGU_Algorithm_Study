import sys
from collections import deque
input = sys.stdin.readline

# 노드 수 입력
N = int(input())

# 리스트 초기화
vertices = [[0] for _ in range(N+1)]

# 부모 노드 저장 리스트 초기화
parent = [0] * (N+1)

# 인접 리스트 구성
for _ in range(N-1):
    a, b = map(int, input().split())
    vertices[a].append(b)
    vertices[b].append(a)
    
# 1번 노드의 부모 = 0
parent[1] = 0

# 큐 초기화
q = deque()
q.append(1)

# BFS 수행
while q:
    current = q.popleft() 
    for v in vertices[current]: 
        if parent[v] == 0:  
            parent[v] = current  
            q.append(v) 

# 2번 노드부터 N번 노드까지의 부모 노드를 출력
print('\n'.join(map(str, parent[2:])))
