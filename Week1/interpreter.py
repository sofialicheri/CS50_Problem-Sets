def main():
    user = input("Expression: ")
    part = user.rsplit(" ")
    x = int(part[0])
    y = part[1]
    z = int(part[2])
    if y == "+":
        print(float(x + z))
    elif y == "-":
        print(float(x - z))
    elif y == "*":
        print(float(x * z))
    elif y == "/":
        print(float(x / z))


main()
