answer = 25

while True:
    user_input = int(input("請輸入1~100的數字: "))
    print(user_input)
    if user_input < 1 or user_input >100:
        print("超出範圍請重新輸入")
    elif user_input < answer:
        print("請出入更大的數字")
    elif user_input > answer:
        print("請輸入更小的數字")
    else:
        print("恭喜中獎")
        break

        




