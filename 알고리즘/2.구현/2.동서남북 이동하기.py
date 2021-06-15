import sys
x,y = map(int,sys.stdin.readline().split())

dx=[0,0,1,-1]
dy=[1,-1,0,0]

for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    print('(',nx,',',ny,')')