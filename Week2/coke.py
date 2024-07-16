def main():
    global to_pay
    to_pay = 50
    print("Amount Due: 50")
    while True:
        insert_coin = int(input("Insert Coin: "))
        remaining_amount = amount_due(insert_coin)
        if remaining_amount is None or remaining_amount <=0:
            break
        print("Amount Due:", remaining_amount)

def amount_due(money):
    global to_pay
    if to_pay == 0:
        return None
    if money in [25, 10, 5]:
        to_pay = to_pay - money
        if to_pay <= 0:
            print("Change Owed:", abs(to_pay))
        return to_pay
    elif money >= 50 or money not in [25, 10, 5]:
        return to_pay
main()
