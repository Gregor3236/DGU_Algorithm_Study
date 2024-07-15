import sys
input = sys.stdin.readline


num_commands = int(input()) # 명렁 받는 수 입력
stack = [] # 스택 설정

# 명령어 처리 부분
for _ in range(num_commands):
    command = input().split()  # 명령 입력 받음

    # push 명령어 처리
    if command[0] == "push":
        stack.append(command[1])  # 스택에 값을 추가

    # pop 명령어 처리
    elif command[0] == "pop":
        if len(stack) == 0:  # 비어있는 경우
            print(-1)  # -1 출력
        else:
            print(stack.pop())  # 마지막 값을 제거하고 출력

    # size 명령어 처리
    elif command[0] == "size":
        print(len(stack))  # 스택의 크기를 출력

    # empty 명령어 처리
    elif command[0] == "empty":
        if len(stack) == 0:  # 비어있는 경우
            print(1)  # 1 출력
        else:
            print(0)  # 나머지 경우 0 출력

    # top 명령어 처리
    elif command[0] == "top":
        if len(stack) == 0:  # 비어있는 경우
            print(-1)  # -1 출력
        else:
            print(stack[-1])  # 마지막 값을 출력
