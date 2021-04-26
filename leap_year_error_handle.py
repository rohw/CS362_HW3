while(True):
    user_input = input("Enter a year: ")
    try:
        year = int(user_input)
    except:
        print('It is not a valid input')
        continue
    if year >= 0:
        break
    else:
        print("It is not a valid input")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        print("It is a leap year")
else:
    print("It is not a leap year")
