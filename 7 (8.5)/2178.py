from collections import deque
import sys

# 행열 수 입력
N, M = map(int, sys.stdin.readline().split())

# 미로 정보를 입력
pan = [list(str(sys.stdin.readline().strip())) for _ in range(N)]

# 방문 여부를 저장할 2차원 리스트
visited = [[False for _ in range(M)] for i in range(N)]

# 거리 저장할 2차원 리스트 
distance = [[1 for _ in range(M)] for i in range(N)]

# 방향 벡터
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    queue = deque()
    queue.append((0, 0))  # 시작점을 큐에 추가
    while queue:
        x, y = queue.popleft()  # 큐에서 현재 위치 꺼내기
        for i in range(4):  # 상하좌우 네 방향으로 탐색
            nx = x + dx[i]  # 다음 이동할 x좌표
            ny = y + dy[i]  # 다음 이동할 y좌표
            # 다음 이동이 미로를 벗어나는 경우는 무시
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            # 다음 위치가 방문하지 않은 길인 경우
            if visited[nx][ny] == False and pan[nx][ny] == '1':
                queue.append((nx, ny))  # 큐에 추가하여 다음 탐색 대상으로 설정
                visited[nx][ny] = True  # 방문 체크
                # 현재 위치의 거리에 1을 더해 다음 위치의 거리로 설정
                distance[nx][ny] += distance[x][y]

# BFS 함수 호출
bfs()

# 목표 지점(N-1, M-1)의 최단 거리 출력
print(distance[N-1][M-1])
