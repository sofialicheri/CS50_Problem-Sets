def my_list():
    sorted_groceries = {}
    while True:
        try:
            item = input().lower()

            if item in groceries:
                groceries[item] += 1  # item count goes up 1
            else:
                groceries[item] = 1

            sorted_groceries = dict(sorted(groceries.items()))

        except EOFError:
            return sorted_groceries


def main():
    sorted_groceries = my_list()
    for item in sorted_groceries:
        print(sorted_groceries[item], item.upper())


groceries = {}
item_count = 1

main()
