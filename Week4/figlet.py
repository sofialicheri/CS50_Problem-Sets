import sys
import random
from pyfiglet import Figlet

figlet = Figlet()


def output(text):
    output = figlet.renderText(text)
    return output


def main():
    if len(sys.argv) == 3:
        if sys.argv[1] == "--font" or sys.argv[1] == "-f":
            if sys.argv[2] in figlet.getFonts():
                figlet.setFont(font=sys.argv[2])
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")


    elif len(sys.argv) == 2:
        if sys.argv[1] not in figlet.getFonts():
            sys.exit("Invalid usage")

    elif len(sys.argv) == 1:
        figlet.setFont(font=random.choice(figlet.getFonts()))

    user = input("Input: ")
    print(output(user))


if __name__ == "__main__":
	main()
