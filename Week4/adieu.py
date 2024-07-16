import inflect

p = inflect.engine()

global namelist
namelist = []


def main():
    while True:
        try:
            namelist.append(input("Name: "))

        except EOFError:
            break

    namelist_comma = p.join(namelist)

    print("Adieu, adieu, to " + namelist_comma)


if __name__ == "__main__":
    main()
