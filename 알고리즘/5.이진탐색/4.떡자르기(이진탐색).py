import sys
n,m = map(int,sys.stdin.readline().split())

data= list(map(int,input().split()))    #int
sum=2000000000
while sum>m:
    mid=max(data)//2
    if (sum(data)-mid*n)>=
        return mid 

# def bi_sear(array,target,start,end):
#     while start<=end:
#         mid = (start+end)//2
#         if array[mid]==target:
#             return mid
#         elif array[mid]>target:
#             end=mid-1
#         else:
#             start=mid+1
#     return None

result=bi_sear(array,target,0,n-1)

if result==None:
    print("없음")
else: print(result+1)



# print(max(array))