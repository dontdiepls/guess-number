# 让user重复猜数字游戏
# 猜对的话印出猜对了
#　错的话告诉他比答案大 / 小
import random
r = random.randint(1, 100)
count = 0
while True:
    user_input = int(input("请输入数字: "))
    count += 1
    if user_input == r:
        print("恭喜，你猜对了")
        print(f"您目前输入的次数为{count}次.")
        break
    elif user_input > r:
        print("您输入的数字比答案大")
    elif user_input < r:
        print("您输入的数字比答案小")
    print(f"您目前输入的次数为{count}次.")
