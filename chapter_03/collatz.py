"""
3章 関数 
    p,77~78  練習問題
"""

# 演習プロジェクト 3.11.1 コラッツ数列

def collatz(number):
    if number % 2 == 0:
        return number / 2
    else:
        return number * 3 + 1
        
print('整数を入力してください：')
i = int(input())

while i > 1:
    i = collatz(i)
    print(i)