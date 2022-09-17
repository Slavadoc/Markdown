# Kegel
# n,k = [int(i) for i in input().split()]
# list = ['I'] * n
# print(list)
# for n in range(k):
#     l,r = [int(s) for s in input().split()]
#     for j in range(l-1,r):
#         list[j] = '.'
# print(' '.join(a))
# Fibonici
array = [0,0]
array[0] = 0
array[1] = 1
N = int(input())

for i in range(N):
    array.append(array[i] + array[i+1])
print("fibonati = ", array)
