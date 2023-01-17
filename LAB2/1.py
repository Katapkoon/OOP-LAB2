x = [str(x) for x in input("").split()]
temp = 0
have_zero = False
for i in range(0,len(x)):
    if x[i] == '0':
        have_zero = True
        temp = i
        x.pop(i)
        break

x.sort(reverse=False)
if have_zero == True:
    x.insert(temp,'0')
print(x)
print("".join(x))