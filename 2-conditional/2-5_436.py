a=[1,2,3,4,5,5,5]
remove_set={3,5}
# result=[i for i in a if i not in remove_set]
result=[]
for i in a:
    if i not in remove_set:
        result.append(i)
        
print(result)