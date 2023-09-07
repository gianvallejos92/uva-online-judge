import sys

FEB_MONTH = 2
FEB_LEAPS_DAYS = 29
LAST_MONTH = 12
YEAR_DAYS = 365
daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

def leaps_between_years(initYear, endYear):
    cnt = 0
    for x in range(initYear, endYear):
        if is_leap(x):
            cnt += 1
    return cnt

def add_n_days(n, day, month, year):    
    for x in range(n):
        if (day + 1 <= daysPerMonth[month-1]) or (is_leap(year) and month == FEB_MONTH and day + 1 <= FEB_LEAPS_DAYS):
            day+=1            
        else:
            day = 1
            if month == LAST_MONTH:
                month = 1
                year+=1
            else:
                month+=1                    
    return [day, month, year]

def rest_n_days(n, day, month, year):
    for x in range(n):
        if day - 1 == 0:
            if month - 1 == 0:
                year-=1
                month = LAST_MONTH
            else:
                month-=1
            
            if month == FEB_MONTH and is_leap(year):
                day = FEB_LEAPS_DAYS
            else: 
                day = daysPerMonth[month-1]
        else:
            day-=1
    return [day, month, year]

if __name__ == '__main__':
    
    for line in sys.stdin:
        N, day, month, year = list(map(int, line.rstrip().split()))[:4]
        if N == 0 and day == 0 and month == 0 and year == 0:
            break
        
        if N > YEAR_DAYS:
            addYears = int(N/YEAR_DAYS)
            restOfDays = N%YEAR_DAYS
            numberOfLeaps = leaps_between_years(year, year + addYears)            
            year += addYears
            debtDays = restOfDays - numberOfLeaps
            if debtDays > 0:
                result = add_n_days(debtDays, day, month, year)
            else:
                result = rest_n_days(debtDays*-1, day, month, year)
        else:
            result = add_n_days(N, day, month, year)

        day, month, year = result[:3]

        print(day, month, year)

    exit(0)
