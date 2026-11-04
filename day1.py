"""
我的第一个 Python 程序：大学进度条

运行方式：打开终端，进入这个文件夹，输入
    python day1.py
"""

from datetime import date

# ---------- 1. 先把三个日期定下来 ----------
START = date(2026, 9, 1)     # 入学那天
END = date(2030, 6, 30)      # 毕业那天
TODAY = date.today()         # 今天，电脑自己知道


# ---------- 2. 算数 ----------
total_days = (END - START).days      # 一共多少天
passed_days = (TODAY - START).days   # 已经过了多少天
left_days = (END - TODAY).days       # 还剩多少天
percent = passed_days / total_days   # 走了百分之几（0 到 1 之间的小数）


# ---------- 3. 定义一个小工具：把小数画成进度条 ----------
def make_bar(p, width=40):
    """输入 0~1 之间的数，返回一条进度条字符串"""
    filled = int(p * width)
    return "█" * filled + "░" * (width - filled)


# ---------- 4. 打印出来 ----------
print("=" * 52)
print("           大学四年 · 进度条")
print("=" * 52)
print()
print(f"  入学      {START}")
print(f"  今天      {TODAY}")
print(f"  毕业      {END}")
print()
print(f"  {make_bar(percent)}  {percent:>6.1%}")
print()
print(f"  已经走过  {passed_days:>6} 天")
print(f"  还剩      {left_days:>6} 天")
print()

# ---------- 5. 根据进度说一句话 ----------
if percent < 0.10:
    print("  你才走了不到十分之一。来得及，全都来得及。")
elif percent < 0.50:
    print("  路还长。现在开始，不晚。")
else:
    print("  一半过去了。该想清楚的事，得想清楚了。")

print()
