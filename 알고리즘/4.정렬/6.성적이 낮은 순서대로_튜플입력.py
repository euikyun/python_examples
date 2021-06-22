import sys

n=int(sys.stdin.readline().strip())

array=[]
for _ in range(n):
    data=input().split()
    array.append((data[0], int(data[1])))

array=sorted(array,key=lambda i:i[1])
print(array)
for i in array:
    print(i[0],end=" ")
