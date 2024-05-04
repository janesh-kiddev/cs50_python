def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    trip=dollars[1:]
    return float(trip)


def percent_to_float(percent):
    tt=float(percent[:len(percent)-1])
    return tt/100


main()
