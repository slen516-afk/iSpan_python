import random

answer = random.randint(1,100)

print("猜1~100之間的數字")

low = 1
high = 100

while True: 
    try:
    
        guess = int(input("請輸入數字1~100:"))
    except Exception as e:
        print("請輸入數字")
        continue
      

    if guess < low or guess > high:
        print("超出範圍，請重新輸入")
    elif guess > answer:
        print("請輸入更小的數字")
        high = guess - 1
    elif guess < answer:
        print("請輸入更大的數字")
        low = guess + 1
    else:
        print("恭喜中獎!")
        break
