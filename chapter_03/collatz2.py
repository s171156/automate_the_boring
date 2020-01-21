"""
3章 関数 
    p,77~78  練習問題
"""

# 演習プロジェクト 3.11.2 コラッツ数列
# 入力の整合性を確認

def collatz(number):
    if number % 2 == 0:
        return number / 2
    else:
        return number * 3 + 1
        
while True:
    try:
        print('整数を入力してください：')
        i = int(input())
        break
    except ValueError:
        print('エラー：整数を入力してください')

while i > 1:
    i = collatz(i)
    print(i)