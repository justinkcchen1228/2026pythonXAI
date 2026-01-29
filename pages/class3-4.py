import random
answer = random.randrange(1,101)
min = 1
max = 100
while True:
    num = int(input(f"請輸入{min}到{max}的整數:"))
    if num > max or num < min:
        print("請不要亂輸入!!!")
    if num > answer:
        print("太大了!")
        b = num
    elif num < answer:
        print("太小了!")
        a = num
    else:
        print("答對了!")
        break
    