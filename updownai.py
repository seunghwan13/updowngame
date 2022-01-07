num = int(input("1~100 사이의 수를 입력하세요"))

first = 25
last = 100
print(first)
val = input("up, down, answer 중 알맞은 값 하나를 입력하시오.")

while True:
    for j in range(5):
        median = int((first+last)/2)
        print(median)
        val = input("up, down, answer 중 알맞은 값 하나를 입력하시오.")

        if(val == "up"):
            first = median
        elif(val == "down"):
            last = median
        elif(val == "answer"):
            print("정답입니다")
            print("게임이 끝났습니다")
            quit()
        else:
            print("다시 입력해주세요.")
            break

# 왜 first를 25로 설정해두신거죠? 0으로 설정하는게 더 좋을 것 같은데요~