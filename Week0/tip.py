def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent_dec = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent_dec
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollars = float(d.replace("$",""))
    return dollars

def percent_to_float(p):
    percent = float(p.strip().replace("%",""))
    percent_dec = float(percent/100)
    return percent_dec

main()
