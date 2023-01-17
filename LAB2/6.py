x = input().split()
y = input().split()

def add2list(lst1,lst2):
    newlst = [int(lst1[i]) + int(lst2[i]) for i in range(0,len(lst1))]
    return newlst

print(add2list(x,y))