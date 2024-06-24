num1 = 0 # 전공과목별의 합
num2 = 0 # 학점의 총합

# 등급표 
grdChart = { 
  "A+" : 4.5, "A0" : 4,
  "B+" : 3.5, "B0" : 3,
  "C+" : 2.5, "C0" : 2,
  "D+" : 1.5, "D0" : 1,
  "F" : 0
}


for i in range(1, 21): # 20번 반복 가능
  sub, crd, grd = input().split() # 과목, 학점, 등급 
  if grd == "P": # 등급이 P일 경우
    continue # 계산에서 제외
  num1 += grdChart[grd] * float(crd) # 전공과목별의 합 계산 
  num2 += float(crd) # 학점의 총합 계산
  
print(num1 / num2) # 전공평점 출력
