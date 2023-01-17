def day_of_year(day,month,year):
    dem = [31,28,31,30,31,30,31,31,30,31,30,31] #dey stands for days each month
    day_of_years = 0

    if is_leap(year):
        dem[2-1] += 1 
    
    day_of_years += day
    for i in range(1, month):
        day_of_years += dem[i - 1]
        
    return day_of_years
    
def is_leap(year):
    if year % 4 == 0:
        if year % 400 == 0 or year % 100 != 0:
            return True
        else:
            return False
    else:
        return False

def date_diff(date1,date2):
    d1 = list(map(int,date1.split("-")))
    print(d1)
    d2 = list(map(int,date2.split("-")))
    first_date = day_of_year(d1[0],d1[1],d1[2])
    print(first_date)
    days1 = day_in_year(d1[2]) #check numbers of days in year of first date.
    second_date = day_of_year(d2[0],d2[1],d2[2])
    days2 = day_in_year(d2[2]) #check numbers of days in year of second date.
    days_year_gap = 0
    for i in range(d1[2]+1,d2[2]):
        if is_leap(i):
            days_year_gap += 366
        else:
            days_year_gap += 365

    diff = second_date + days_year_gap + ((days1 - first_date) + 1) 
    return diff

def day_in_year(year):
    if is_leap(year):
        return 366
    else:
        return 365
    
print(date_diff("25-12-1999","9-3-2000"))
