year = int(input()) # 연도를 입력 받고 정수형으로 전환

if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)): # 4의 배수이면서 100의 배수가 아닐때 또는 400의 배수일 경우
  print(1) # 1 출력
else:
  print(0) # 나머지 경우 0 출력
