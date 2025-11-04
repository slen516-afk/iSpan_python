answer = 25
user_input = "0"

while answer != user_input:
    user_input = int(input("請輸入1~100的數字: "))

    if user_input<1 or user_input>100:
        print("請重新輸入")

    elif user_input <answer:
        print("更小")
    
    

        
