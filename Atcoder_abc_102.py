A,B,C = map(int,input().split())

D = max(A,B,C) E = min(A,B,C) F = A + B + C - D - E

G = F - E H = D - F

print(G + H)
