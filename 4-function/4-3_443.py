array=[('a',50),('b',32),('c',74)]

def my_key(x):
    return x[1]

print(sorted(array,key=my_key))


# array=[(8,6),(1,8),(5,3),(6,8),(8,2)]
# print(sorted(array,key=lambda x:x[1]))