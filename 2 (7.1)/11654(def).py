num = int(input()) # 숫자 입력

def factorial(num): # factorial 함수 정의
  if num <= 1: # num의 값이 1 이하
    return 1 # 1 반환
  else: # 나머지 경우
    return num * factorial(num - 1) # 함수 리콜

print(factorial(num))
