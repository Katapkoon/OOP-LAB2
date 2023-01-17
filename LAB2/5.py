x = input()

def only_english(string1):
    ans= [ letter for letter  in string1 if letter.isalpha() or not ' ']
    return "".join(ans)

print(only_english(x))

