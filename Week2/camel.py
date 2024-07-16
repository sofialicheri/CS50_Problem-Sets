def main():
    camelCase = input("camelCase: ")
    print("snake_case:", snake_case(camelCase))

def snake_case(word):
    letter = ""
    for c in word:
        if c.isupper():
            letter = letter + ("_" + c.lower())
        elif c.islower():
            letter += c
        elif c == "":
            break
    return letter

main()
