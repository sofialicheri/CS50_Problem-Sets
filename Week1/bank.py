def moneyback():
    user = input("Greeting: ").strip().casefold()
    if user.startswith("hello"):
        return "$0"
    elif user.startswith("h"):
        return "$20"
    else:
        return "$100"

def main():
    print(moneyback())

main()
