month_num = 15

if 1 <= month_num <= 12:  # if the month_num is valid

    if month_num == 2:  # if the month is Feb
        print('28 days')
    elif month_num == 4 or month_num == 6 or month_num == 9 or month_num == 11:  # if the month is Apr, Jun, Sep, or Nov
        print('30 days')
    else:
        print('31 days')

else:
    print('Invalid Month')


"""
Write a program that can print the number of days in a month
	            Ex:
	                number = 1;
                    output:
                        31 Days
	            Hints:
	                Months that has 31 days: 1, 3, 5, 7, 8, 10, 12
	                Months that has 30 days: 4, 6, 9, 11
	                Month that has 28 days: 2
"""
