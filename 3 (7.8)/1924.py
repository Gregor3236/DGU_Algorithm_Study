import calendar # calendar 가져오기
week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"] # 리스트 작성

a, b = map(int, input().split()) # 워ㄹ, 일 입력 받기

days = calendar.weekday(2007, a, b) # 2007년 요일 값 가져오기
print(week[days]) # 출력
