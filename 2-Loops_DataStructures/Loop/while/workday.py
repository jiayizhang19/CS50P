def main():
    weekday = int(input("Input the number of weekday (1 for Monday and so on and so forth): "))

    while 0 < weekday < 6:
        days = 6 - weekday
        print(f"{days} days to work ...")
        weekday += 1
    
    print("Enjoy your weekends! ^_^")

main()