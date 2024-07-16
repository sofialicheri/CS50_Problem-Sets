def main():
    time = input("What time is it? ").strip()
    finaltime = convert(time)
    if finaltime <= 8 and finaltime >= 7:
        return "breakfast time"
    elif finaltime <= 13 and finaltime >= 12:
        return "lunch time"
    elif finaltime <= 19 and finaltime >= 18:
        return "dinner time"

def convert(time):
    exact = time.rsplit(":")
    minutes = int(exact[1])
    return float(((int(exact[0])*60) + minutes)/60)

if __name__ == "__main__":
    print(main())
