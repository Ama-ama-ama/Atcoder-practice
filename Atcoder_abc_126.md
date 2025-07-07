# ABC126 A - Changing a Character

[問題リンク](https://atcoder.jp/contests/abc126/tasks/abc126_a)  
配点：100点  
実行時間制限：2 sec / メモリ制限：1024 MiB

---

## 問題文

長さ `N` の文字列 `S` が与えられる。  
整数 `K`（1 ≤ K ≤ N）も与えられる。  

このとき、文字列 `S` の **K文字目**（1-indexed）を **小文字に変える**。  
変換後の文字列を出力せよ。

---

## 解法

- Pythonの文字列は 0-indexed なので、`K-1` 番目の文字を変更する必要がある。
- Pythonの文字列は immutable（変更不可）なので、スライスを使って変換を行う。
- `S[:K-1]` + `S[K-1].lower()` + `S[K:]` という形で文字列を組み立て直せばよい。

---

## 自己分析

- 1-indexed と 0-indexed の違いに注意が必要だった。
- Pythonの文字列は直接変更できないので、スライスと `lower()` を組み合わせる発想が重要。
- シンプルだが、基礎的な文字列操作の理解度が問われる問題。

---

## コード例

```python
N, K = map(int, input().split())
S = input()
print(S[:K-1] + S[K-1].lower() + S[K:])
