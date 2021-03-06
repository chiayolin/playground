# this program will display the day of the week that the 
# following holidays fall on for a year entered by the user:
#
# New Year’s eve   -  12/31
# St. Patrick Day  -  03/17
# April Fool’s Day -  04/01
# Fourth of July   -  07/04
# Labor Day        -  first Monday of September
# Halloween        -  10/31
# user’s birthday  -  mm/dd
#

## init 
# constants for finding DoW
t = (0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4); c = 0

# some commonsense that computers don't know
monday = 1; labor_day_day = 1 # initialize Labor's Day day first
holiday = \
    [("New Year's Eve", 12, 31), ("St. Patrick Day", 3, 17),
    ("April Fool’s Day", 4, 1), ("Fourth of July", 7, 4),
    ["Labor Day", 9, 1], ("Halloween", 10, 31)]
month_name = \
    ('January', 'February', 'March', 'April', 'May', 'June', 'July', 
    'August', 'September', 'October', 'November', 'December')
day_name = \
    ('Sunday', 'Monday','Tuesday','Wednesday','Thursday',
    'Friday', 'Saturday')

## main
terminate = 0
while not terminate: 
    # get user's birthday into a list
    user_birthday = \
        input("what's your birthday? (mm/dd/yyyy): ").split("/")

    # convert user's birthday into a list of intergers
    # by using list comprehension
    user_birthday = [int(i) for i in user_birthday]

    # get a year number in interger 
    the_year = int(input("which year are you looking for? "))

    # define numeric symbols
    MONTH = 0; DAY = 1; YEAR = 2;

    # find the DoW of user's birthday
    m = user_birthday[MONTH]; y = user_birthday[YEAR]; d = user_birthday[DAY]
    y -= m < 3 # leap year check
    dow_user_birthday = \
        int((y + y / 4 - y / 100 + y / 400 + t[m - 1] + d + c) % 7)
    y = the_year;
    y -= m < 3
    dow_user_birthday_the_year = \
        int((y + y / 4 - y / 100 + y / 400 + t[m - 1] + d + c) % 7)
    
    # re-define the numeric symbols
    NAME = 0; MONTH = 1; DAY = 2; YEAR = the_year
    labor_day = 4 # labor day is the forth tuple of the list

    # print a newline so it looks better
    print(end = '\n')

    # print user's birthday
    print("your birthday was on", day_name[int(dow_user_birthday)], 
        "and it's on", day_name[int(dow_user_birthday_the_year)],
        "in", the_year)

    # find and print every holiday's date and DoW with this iteration 
    counter = 0
    while counter != len(holiday):
        # find the date for labor's day
        if counter == labor_day:
            _y = the_year; _y -= m < 3
            while int((_y + _y / 4 - _y / 100 + _y / 400 \
                + t[9 - 1] + labor_day_day + c) % 7) != 1:
                    labor_day_day += 1
            # put the correct day into the tuple
            holiday[labor_day][DAY] = labor_day_day
        
        # get day of the week
        m = holiday[counter][MONTH]; d = holiday[counter][DAY]; y = YEAR
        y -= m < 3
        dow = int((y + y / 4 - y / 100 + y / 400 + t[m - 1] + d + c) % 7)
        
        # since every piece of info we need is in the list; 
        # therefore, just iterate through every tuple 
        print(holiday[counter][NAME], "is on",
            month_name[holiday[counter][MONTH] - 1],
            str(holiday[counter][DAY]) + ",",
            day_name[dow])
        counter += 1
    
    ## terminating
    terminate = 1 if input("try again? ")[0][0].lower() != 'y' else None 
