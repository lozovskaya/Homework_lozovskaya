arr = input().split()
n = int(input())
print(*arr[:n], *arr[n + 1:])
