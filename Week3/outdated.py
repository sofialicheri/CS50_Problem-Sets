import re

user_date = ""


def main():
    print(conversion(user_date))


def conversion(user_date):

    month = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12,
    }

    while True:
        user_date = input("Date: ").strip()

        user_date_split = re.split(
            " |, ", user_date
        )  # split first by comma and space and just space

        if len(user_date_split) == 3:

            if "," not in user_date:
                continue

            if user_date_split[0] in month and int(user_date_split[1]) in range(1, 32):
                user_date_split[0] = month[
                    user_date_split[0]
                ]  # valid month, returns its corresponding number
                if int(user_date_split[1]) in range(1, 10):
                    user_date_split[1] = "0" + str(
                        user_date_split[1]
                    )  # adds 0 to day numbers 1-9
                if int(user_date_split[0]) in range(1, 10):
                    user_date_split[0] = "0" + str(
                        user_date_split[0]
                    )  # adds 0 to month numbers 1-9
                break
            else:
                continue

        if len(user_date_split) != 3:
            try:
                user_date_split = re.split("/", user_date)  # split by slashes/
                if int(user_date_split[0]) not in range(1, 13) or int(
                    user_date_split[1]
                ) not in range(1, 32):
                    continue  # invalid month or day
                if int(user_date_split[0]) in range(1, 10):
                    user_date_split[0] = "0" + str(
                        user_date_split[0]
                    )  # adds 0 to month numbers 1-9
                if int(user_date_split[1]) in range(1, 10):
                    user_date_split[1] = "0" + str(
                        user_date_split[1]
                    )  # adds 0 to day numbers 1-9
                break
            except ValueError:
                continue

    iso_month = str(user_date_split[0])
    iso_day = str(user_date_split[1])
    iso_year = str(user_date_split[2])

    converted_date = iso_year + "-" + iso_month + "-" + iso_day

    return converted_date


main()
