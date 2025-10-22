# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」
import random

answer = random.randint(1,100)

print("猜1~100之間的數字")

low = 1
high = 100

while True:
    guess = int(input("請輸入數字1~100:"))

    if guess < low or guess > high:
        print("超出範圍，請重新輸入")
        continue
    if guess > answer:
        print("請輸入更小的數字")
        high = guess - 1
    elif guess < answer:
        print("請輸入更大的數字")
        low = guess + 1
    else:
        print("恭喜中獎!")
        break












