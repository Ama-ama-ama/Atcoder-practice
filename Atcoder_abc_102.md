# ABC102 A - Multiple of 2 and N

 [問題リンク](https://atcoder.jp/contests/abc102/tasks/abc102_a)  
 配点：100点  
 実行時間制限：2 sec / メモリ制限：1024 MiB

---

## 問題文

正整数 N が与えられます。2 と N のどちらでも割り切れる最小の正整数を求めてください。

---

## 解法

- 2 と N の最小公倍数（LCM）を求めれば良い
- Pythonでは `math.lcm(2, N)`（または `2*N` if N is even）
---

## 自己分析

- import math の使い方
- lcm と　gcd　の使い方
- 
---

## 入力例
import math
N = int(input())
lcm = 2*N // math.gcd(2,N)

print(lcm)

