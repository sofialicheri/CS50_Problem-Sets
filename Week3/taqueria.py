def calculator(order):
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    menu_lower = {k.lower(): v for k, v in menu.items()}
    price = 0

    try:
        while True:
            item = input("Item: ")
            if not item: #if item is empty
                break
            elif item.lower() in menu_lower:
                order.append(item)
                cost = menu_lower[item.lower()]
                price+=cost
                print(f"Total: ${price:.2f}")
            elif item.lower() not in menu_lower:
                pass
            else:
                continue
            # the order will also be a list, so each item is added in order list

    except EOFError:
        print("\n")
        pass

    return price

order = []
calculator(order)
