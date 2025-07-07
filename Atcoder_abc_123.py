nums = [int(input()) for _ in range(5)]
k = int(input())

if max(nums) - min(nums) <= k:
    print("Yay!")
else:
    print(":(")
