import random
print("지금부터 updown 게임을 시작할게요~!")
print("지시에 따르지 않으면 바로 실패입니다.")
print("-------------------------------")
computer_num = random.randrange(1, 101)
try_count = 0
try:
    for num in range(5):
        player_num = int(input("1~100 사이의 수를 입력해주세요 >"))
        if player_num > 100 or player_num < 0:
            raise Exception
        elif player_num < computer_num:
            print("up")
            try_count += 1
        elif player_num > computer_num:
            print("down")
            try_count += 1
        elif player_num == computer_num:
            print("성공~! 정답입니다.")
            print("{0}번 만에 맞췄습니다.".format(str(try_count)))
            try_count += 1
except Exception as player_num:
    print("{player_num}은 숫자가 아니거나 1~100 사이의 수가 아닙니다.")
print("실패! 주어진 {0}번의 기회를 모두 소진했습니다.".format(str(try_count)))


# reset test 입니다.

