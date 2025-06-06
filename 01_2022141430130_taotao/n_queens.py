# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mhpKxQQ7rLpseP8CDyZUSTpCPJ8kVBIw
"""



import time

# 冲突检测函数，检查当前放置的皇后是否与之前的皇后冲突
def pd(k):
    for i in range(1, k):
        # 如果在同一列或同一对角线上，则冲突
        if abs(k - i) == abs(x[k] - x[i]) or x[k] == x[i]:
            return False
    return True

# 深度优先搜索函数，用于递归放置皇后并寻找所有解
def dfs(a):
    global n, count, solutions
    # 如果已经放置完所有皇后，则记录解
    if a > n:
        count += 1
        solution = []
        for i in range(1, n+1):
            row = ['.'] * n
            row[x[i]-1] = 'Q'
            solution.append(' '.join(row))
        solutions.append(solution)
        return
    # 尝试在当前行的每一列放置皇后
    for i in range(1, n + 1):
        x[a] = i
        if pd(a):
            dfs(a + 1)

# 输入处理函数，确保输入合法
def input_handler():
    while True:
        try:
            n = int(input("请输入正整数N（N≥4）："))
            if n < 4:
                print("输入的N必须大于等于4，请重新输入！")
                continue
            break
        except ValueError:
            print("输入非法，请重新输入！")
    return n

# 输出所有解的函数
def print_all_solutions(solutions):
    for idx, solution in enumerate(solutions, 1):
        print(f"解 {idx}:")
        for row in solution:
            print(row)
        print()

# 输出单个解的函数
def print_one_solution(solutions):
    if solutions:
        print("解 1:")
        for row in solutions[0]:
            print(row)
        print()

if __name__ == '__main__':
    # 输入处理
    n = input_handler()

    # 初始化皇后的位置数组，x[k]表示第k行皇后所在的列
    x = [0] * (n + 1)
    count = 0
    solutions = []
    start_time = time.time()  # 开始计时

    # 进行深度优先搜索
    dfs(1)

    end_time = time.time()  # 结束计时

    # 输出解的总数
    print(f"N={n}时，共有{count}种解法。")

    # 提供用户交互，选择输出全部解或仅一个解
    while True:
        choice = input("请输入选择（1: 输出全部解，2: 输出一个解）：")
        if choice == '1':
            print_all_solutions(solutions)
            break
        elif choice == '2':
            print_one_solution(solutions)
            break
        else:
            print("输入无效，请重新输入！")

    # 输出运行时间
    print(f"运行时间：{end_time - start_time:.6f}秒")