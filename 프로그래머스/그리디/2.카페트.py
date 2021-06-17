import sys

brown,yellow=map(int,sys.stdin.readline().split())
row=col=0
def solution(brown, yellow):
    total=brown+yellow
    for i in range(1,total):
        if total%i==0:
            if (i-2)*(total//i-2)==yellow:
                row,col=i,total//i
                break
    if(row<=col):
        row,col=col,row

    return [row,col]

print(solution(brown,yellow))

    # total=brown+yellow
    # for i in range(1,total):
    #     for j in range((total-1)//i,1,-1):
    #         if (i-2)*(j-2)==yellow and (i*j==yellow+brown):
    #             row,col=i,j
    #             break