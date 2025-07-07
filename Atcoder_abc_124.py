A, B = map(int, input().split())
total = max(A, B) + max(min(A, B), max(A, B) - 1)
print(total)
