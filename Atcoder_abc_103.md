# A - Task Scheduling Problem
 [問題リンク](https://atcoder.jp/contests/abc103/tasks/abc103_a)  
**実行時間制限：** 2 sec  
**メモリ制限：** 1024 MiB  
**配点：** 100点

---

## 問題文

3個のタスクがあり、あなたは全てのタスクを完了させなければなりません。

はじめ、任意の1個のタスクをコスト0で完了できます。

また、  
i番目のタスクを完了した直後に  
j番目のタスクを完了するには、コスト **A<sub>ij</sub>** がかかります。
各タスク間のコスト **A<sub>ij</sub>**（ただし i ≠ j）が与えられます。

---

## 解法
最もコストが低くなるタスクのこなし方が、中間値-最小値と最大値-中間値のコストの和であることに気づく。

---

## 自己分析

- max min の使い方を覚える
- 変数は左側に入力

---

## 入力例

A,B,C = map(int,input().split())

D = max(A,B,C)
E = min(A,B,C)
F = A + B + C - D - E

G = F - E
H = D - F

print(G + H)

