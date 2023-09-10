year1 = int(input("Enter year 1 to be checked: "))
 
if year1 % 4 == 0:
    if year1 % 100 == 0:
        if year1 % 400 == 0:
            print("The year 1 is a leap year!")
        else:
            print("The year 1 is not a leap year!")
    else:
        print("The year 1 is a leap year!")
else:
    print("The year is not a leap year!")
year2 = int(input("Enter year 2 to be checked: "))
 
if year2 % 4 == 0:
    if year2 % 100 == 0:
        if year2 % 400 == 0:
            print("The year 2 is a leap year!")
        else:
            print("The year 2 is not a leap year!")
    else:
        print("The year 2 is a leap year!")
else:
    print("The year 2 is not a leap year!")