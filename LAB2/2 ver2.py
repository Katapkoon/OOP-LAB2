x = [str(x) for x in input("").split()]
c = input()


def count_char_in_string(x,c):
    d = [len([letter for letter in string if letter == c]) for string in x]
    return d

print(count_char_in_string(x,c))

