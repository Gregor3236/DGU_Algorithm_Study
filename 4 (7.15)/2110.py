import sys # sys 불러오기
input = sys.stdin.readline

# 입력
n, routers = map(int, input().split())  # n: 집의 수, routers: 공유기의 수
locations = [int(input()) for _ in range(n)]  # 집의 좌표 입력
locations.sort()  # 오름차순으로 정렬

# 초기 탐색 범위 설정
low = 1  # 최소 간격
high = locations[-1] - locations[0]  # 최대 간격

# 이진 탐색 함수
def binary_search(locations, low, high):
    while low <= high:
        mid = (low + high) // 2  # 중간값
        current = locations[0]  # 첫 번째 집에 공유기 설치
        count = 1  # 공유기 수

        # 각 집마다 공유기 설치
        for i in range(1, n):
            if locations[i] >= current + mid:
                count += 1  # 공유기 설치
                current = locations[i] 

        # 설치한 공유기 수가 충분한 경우
        if count >= routers:
            low = mid + 1  # 가능한 간격을 더 크게 설정
            result = mid  # 현재 중간값을 결과로 저장
        else:
            high = mid - 1  # 간격을 더 작게 설정

    return result  # 최대 간격 반환

# 결과 출력
print(binary_search(locations, low, high))
