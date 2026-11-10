"""随机动物名 + 植物名 —— 用来练 Git 的小文件"""

import random

animals = ["猫", "狗", "兔子", "狐狸", "熊猫", "企鹅", "海豚", "猫头鹰"]
plants = ["竹子", "向日葵", "仙人掌", "银杏", "芦苇", "兰花"]

print(f"今天的动物：{random.choice(animals)}")
print(f"今天的植物：{random.choice(plants)}")
