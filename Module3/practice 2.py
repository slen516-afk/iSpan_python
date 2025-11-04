import random
answer = random.randint(1, 100)

while True:
    user_input = int(input("Enter a number: "))

    if user_input > answer:
        print("請輸入更小的數字")
    elif user_input < answer:
        print("請輸入更大的數字")
    elif user_input == answer:
        print("恭喜中獎")
        break
        
        