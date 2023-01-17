x = [ [1, -3, 2], [-8, 5], [-1, -4, -3]]
blank = []
def delete_minus(x):
    ans = [[i for i in sub_list if i >= 0] for sub_list in x]
    return ans

print(delete_minus(x))