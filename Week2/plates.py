def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    numbers = "1234567890"
    punctuation = ",./;'[]<>?:{}+_=-()*&^%$#@!"
    n = 0
    first_digit_encountered = False
    while n<len(s):
        if s[n] in punctuation:
            return False
        if s[n].isdigit():
            if first_digit_encountered== False:
                first_digit_encountered=True
                if s[n] == "0":
                    return False
            if n+1<len(s) and s[n+1].isalpha():
                    return False
        n += 1
    if 2 <= len(s) <= 6:
        if s[0:1].isalpha():
            return True
    else:
        return False

main()
