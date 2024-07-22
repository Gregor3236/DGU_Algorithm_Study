import sys
readline = sys.stdin.readline

# 타워의 수를 읽음
num_towers = int(readline())

# 높이를 읽음
heights = list(map(int, readline().split()))

# 결과 리스트 생성
result = []

# 스택 리스트 생성
stack = []

# 순회 코드
for index in range(num_towers):
  current_height = heights[index]  # 현재 타워 높이
  if stack:  # 스택이 비어있지 않을 경우
    while stack:  # 계속 처리
      if stack[-1][0] < current_height:  # 처음 타워 높이보다 작을 경우
        stack.pop()  # 맨 위 요소를 제거
        if not stack:  # 제거 후 스택이 빌 경우
          print(0, end=' ')  # 0 출력
      elif stack[-1][0] > current_height:  # 타워 높이가 클 경우
        print(stack[-1][1] + 1, end=' ')  # 타워 인덱스 + 1 출력
        break  # 탈출
      else:  # 높이가 같을 경우
        print(stack[-1][1] + 1, end=' ')  # 타워 인덱스 + 1 출력
        stack.pop()  # 스택의 맨 위 요소 제거
        break  # 탈출
    stack.append([current_height, index])  # 스택에 타워 높이와 인덱스 추가
  else:  # 스택이 빌 경우
    print(0, end=' ')  # 0 출력
    stack.append([current_height, index])  # 스택에 타워 높이와 인덱스 추가
