#######################################################
# my_date
#
# Name: Erick Anangwe
# Section: 03
#
# Fall 2023
#########################################################


def is_leap_year(year: int) -> bool:
    """Return True if year is a leap year, False otherwise"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
 

def ordinal_date(year: int, month: int, day: int) -> int:
    """ Return the number of days elapsed since the beginning of the year, including any partial days.
        For example, the ordinal date for 1 January is 1.
        Hint: pre-compute the ordinal date for the first of each month."""
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Days in each month
    
    # zk I like this approach
    if is_leap_year(year):
        days_in_month[2] = 29
    day_of_the_year = sum(days_in_month[:month]) + day
    return day_of_the_year


def days_elapsed(year1: int, month1: int, day1: int, year2: int, month2: int, day2: int) -> int:
    """ Return the number of days that have elapsed between year1-month1-day1 and year2-month2-day2.
        You may assume that year1-month1-day1 falls on or before year2-month2-day2. (In other words,
        your answer will always be >= 0.) """
    if year1 == year2:
        if month1 == month2:
            return day2 - day1
        else:
            ordinal_date1 = ordinal_date(year1, month1, day1)
            ordinal_date2 = ordinal_date(year2, month2, day2)
            return ordinal_date2 - ordinal_date1
    else:
        days_in_year1 = ordinal_date(year1, 12, 31) - ordinal_date(year1, month1, day1)
        days_in_year2 = ordinal_date(year2, month2, day2)

        # zk Clever short-cut.  Make sure you understand how it works (and that  you didn't just
        # copy it)
        years_in_between = sum(366 if is_leap_year(year) else 365 for year in range(year1 + 1, year2))
        total_days = days_in_year1 + days_in_year2 + years_in_between
        return total_days

#print(days_elapsed(1941, 12, 7, 2023, 11, 1))


# This is a tuple. It is immutable so that users can't accidentally modify it.


DAYS_OF_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')


def day_of_week(year: int, month: int, day: int) -> str:
    """ Return the day of the week (Sunday, Monday, Tuesday, etc.) for the given day
        Hint 1: 1 January 1753 was a Monday.
        Hint 2: Use the methods you've already written."""
    total_days = days_elapsed(1753, 1, 1, year, month, day)
    day_index = total_days % 7

    return DAYS_OF_WEEK[day_index]
    

def to_str(year: int, month: int, day: int) -> str:
    """ Return this date as a string of the form "Thursday, 07 March 1833"."""
    week_day = day_of_week(year, month, day)
    month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]
    date_str = f"{week_day}, {day:02d} {month_list[month - 1]} {year}"

    return date_str


print(to_str(2023, 10, 4))
              
    