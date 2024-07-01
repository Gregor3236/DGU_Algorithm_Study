n = int(input()) # n팩토리얼 입력
fat = 1 # 결과값

for i in range(1, n + 1): # n번 반복
  fat *= i # 시그마 

print(fat) # 출력
