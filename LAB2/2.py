x = []



def count_char_in_string(x,c):
    d = []
    temp = 0
    for i in range(0,len(x)):
        d.append(x[i].count(c))
    return d
x = [str(x) for x in input("").split()]
c = input()
print(count_char_in_string(x,c))

