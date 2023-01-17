x = [int(x) for x in input("").split()]
def count_minus(str):
    ans_list = [num for num in str if num < 0]
    return len(ans_list)

print(count_minus(x))
