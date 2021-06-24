import sys
data = list(map(int,input().split()))    #int
k=int(sys.stdin.readline().strip())

def solution(data, k):
    for i in range(1,k+1):
        if data[i%len(data)-1]!=0:
            data[i%len(data)-1]-=1
        

    answer = k%len(data)-1
    return answer

res=solution(data,k)
print(res)
print(data)