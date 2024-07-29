import sys
import heapq as hq

# 정수의 개수
n = int(sys.stdin.readline().strip())

# 최대 힙 리스트
max_heap = []

for _ in range(n):
  # 정수 입력
  num = int(sys.stdin.readline().strip())
  
  if num:
    # 정수가 0이 아닐 경우 최대 힙에 추가 
    hq.heappush(max_heap, (-num))
  else:
    # 입력된 정수가 0일 경우
    try:
      # 가장 큰 값 출력 
      print(-1 * hq.heappop(max_heap))
    except IndexError:
      # 힙이 비어 있는 경우 0을 출력
      print(0)
