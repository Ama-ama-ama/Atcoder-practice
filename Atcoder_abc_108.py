K = int(input())

A = K // 2
B = K % 2
if K % 2 == 0:
    print(A**2)
else:
    print(A**2 + A*B)
    
