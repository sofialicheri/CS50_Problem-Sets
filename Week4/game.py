import random


def main():
    n = 0
    guess = ""

    while int(n) < 1:
        try:
            n = int(input("Level: "))
        except ValueError:
            continue

    computer = random.randrange(1, n+1)

    if guess == "":
        while guess == "" or computer != guess:
            try:
                guess = int(input("Guess: "))
                if guess < 1:
                    raise ValueError
                if computer > guess:
                    print("Too small!")
                elif computer < guess:
                    print("Too large!")
            except ValueError:
                continue

    if computer == guess:
        print("Just right!")

if __name__ == "__main__":
    main()
