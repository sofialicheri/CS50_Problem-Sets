def main():
    fuel = percentage()
    print(fuel)


def percentage():
    while True:
        try:
            fraction = input("Fraction: ").split("/")
            decimal = float(int(fraction[0])/int(fraction[1]))
            if 0<=decimal and decimal<=0.1:
                percentage = "E"
            elif decimal == 0.25:
                percentage = "25%"
            elif decimal == 0.5:
                percentage = "50%"
            elif decimal == 0.75:
                percentage = "75%"
            elif 0.9<=decimal and decimal<=1:
                percentage = "F"
            elif decimal>1:
                raise ValueError
            else:
                percentage = (f"{round(decimal*100)}%")
            return percentage
        except (ValueError, ZeroDivisionError):
            pass

main()
