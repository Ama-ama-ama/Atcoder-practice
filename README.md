# Atcoder-practice
A - Multiple of 2 and N  / 
実行時間制限: 2 sec / メモリ制限: 1024 MiB

配点 : 
100 点

問題文
正整数 
N が与えられます。 
2 と 
N のどちらでも割り切れる最小の正整数を求めてください。

制約
1≤N≤10 
9
 
入力はすべて整数である。
入力
入力は以下の形式で標準入力から与えられる。
N
出力
2 と N のどちらでも割り切れる最小の正整数を出力せよ。

import math 
N = int(input())

lcm = 2*N // math.gcd(2,N)
print(lcm)

