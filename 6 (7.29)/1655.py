import heapq as hq
import sys

input = sys.stdin.readline

# 정수의 개수 입력
n = int(input().strip())
# 결과 저장 리스트
res = []
# 최대 힙과 최소 힙
l = []
r = []

for _ in range(n):
  # 정수 입력
  num = int(input().strip())
  
  if len(l) == len(r):
    # 최대 힙에 저장
    hq.heappush(l, (-num, num))
  else:
    # 최소 힙에 저장
    hq.heappush(r, (num, num))
  
  # 최대 힙 최대값이 최소 힙 최소값보다 큰 경우 두 값을 교환
  if r and l[0][1] > r[0][0]:
    min_val = hq.heappop(r)[0]
    max_val = hq.heappop(l)[1]
    
    hq.heappush(l, (-min_val, min_val))
    hq.heappush(r, (max_val, max_val))
  
  # 현재 중간값을 결과 리스트에 추가
  res.append(l[0][1])

# 결과 출력
for val in res:
  print(val)
