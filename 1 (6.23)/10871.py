N, X = map(int, input().split()) # N, X의 값을 정수형으로 받음
A = list(map(int, input().split()))  # A의 값을 받을 때 정수형으로 받은 뒤 list 처리

for i in range(N): # N번 반복문 수행
  if A[i] < X: # 리스트 안의 숫자와 X의 값 비교
    print(A[i], end=" ") # 조건에 맞는 리스트 값 출력 
