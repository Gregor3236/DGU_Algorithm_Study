# 테스트 케이스 수를 입력받음
num_cases = int(input())

# 각 테스트 케이스를 순회
for _ in range(num_cases):
  stack = []  # 괄호를 추적할 스택 초기화
  parentheses = input()  # 괄호 문자열 입력받음
  for char in parentheses:  # 문자열의 각 문자를 순회
    if char == '(':  # 여는 괄호이면
      stack.append(char)  # 스택에 추가
    elif char == ')':  # 닫는 괄호이면
      if stack:  # 스택에 여는 괄호가 있으면
        stack.pop()  # 스택에서 여는 괄호 하나 제거
      else:  # 스택이 비어있으면 (즉, 매칭되는 여는 괄호가 없음)
        print("NO")  # "NO" 출력
        break  # 현재 테스트 케이스 종료
  else: 
    if not stack:  # 모든 문자를 처리한 후 스택이 비어있으면 (모든 괄호가 매칭됨)
      print("YES")  # "YES" 출력
    else:  # 스택이 비어있지 않으면 (매칭되지 않은 여는 괄호가 남아있음)
      print("NO")  # "NO" 출력
