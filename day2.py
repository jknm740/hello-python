"""
我的第二个 Python 程序：猜数字

运行方式（在这个文件夹里）：
    python day2.py

玩法：
    程序心里想一个 1~100 的整数，你来猜。
    每猜一次，它会告诉你"大了"还是"小了"，直到你猜中。
    输入 q 可以随时退出。
"""

import random
import sys

# ---------- 1. 生成答案 ----------
# 正常情况下是随机数；如果运行时多给了一个数字，就用它当答案（方便测试）
if len(sys.argv) > 1:
    answer = int(sys.argv[1])
else:
    answer = random.randint(1, 100)

count = 0   # 记录猜了几次

# ---------- 2. 开场白 ----------
print("=" * 44)
print("            猜数字 · 1 到 100")
print("=" * 44)
print("我心里有个数，你猜猜看。输入 q 退出。")
print()

# ---------- 3. 主循环：一直问，直到猜中或退出 ----------
while True:
    raw = input(f"第 {count + 1} 次猜，你的答案：").strip()

    # 退出
    if raw == "q":
        print(f"不玩了。答案是 {answer}。")
        break

    # 防呆：输入的不是数字
    if not raw.isdigit():
        print("  要输入数字哦。\n")
        continue

    guess = int(raw)
    count += 1

    # 判断
    if guess > answer:
        print("  大了。\n")
    elif guess < answer:
        print("  小了。\n")
    else:
        print(f"  对了！答案就是 {answer}。")
        print(f"  你一共猜了 {count} 次。")

        if count <= 5:
            print("  不错，有二分法的感觉。")
        elif count <= 8:
            print("  还行，但可以更快。")
        else:
            print("  能猜中就行。下次试试每次猜中间数。")
        break
