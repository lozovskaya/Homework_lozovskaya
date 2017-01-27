array = input().split()
n, elem = map(int, input().split())
print(*array[:n], elem, *array[n:])
