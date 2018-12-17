def is_leap(year):
    leap = False
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                leap=True
                return leap
            else:
                return leap
        else:
            leap=True
            return leap
    else:
        return leap

year= int(input("Enter a year:"))
if (year<=1900 or year>=(10**5)):
    print("Invalid Input")
else:
    print(is_leap(year))
