from itertools import permutations  # itertools 호출

n = int(input())  # n 입력
ary = list(map(int, input().split()))  # 공백 기준으로 리스트 ary에 저장

m = list(permutations(ary, n))
# ary의 모든 순열을 생성 후, m에 저장

def calculator(li):
    total = 0  # 총합 선언
    for i in range(len(li)-1):  # 리스트 li의 길이보다 1 작은 범위만큼 반복
        total += abs(li[i] - li[i + 1])  # total에 추가
    return total  # total 반환

x = calculator(m[0]) # 함수 호출

for li in m: # 각 반복문마다 함슈 호출
    x = max(x, calculator(li))    

print(x)  # x 출력
