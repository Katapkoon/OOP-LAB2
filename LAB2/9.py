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
    kom = [1,3,5,7,8,10,12]
    yon = [4,6,9,11]
    feb = 2
    d1 = list(map(int,date1.split("-")))
    d2 = list(map(int,date2.split("-")))
    if not(d1[1] > 0 and d1[1] <= 12) or not(d2[1] > 0 and d2[1] <= 12):
        return -1
    if (d1[1] == feb and d1[0] == 29 and not is_leap(d1[2])) or (d2[1] == feb and d2[0] == 29 and not is_leap(d2[2])):
        return -1 
    elif (d1[1] == feb and d1[0] > 29) or (d2[1] == feb and d2[0] > 29):
        return -1
    for i in range(0,len(kom)):
        if (d1[1] == i and d1[0] > 31) or (d2[1] == i and d2[0] > 31):
            return -1
    for i in range(0,len(yon)):
        if (d1[1] == i and d1[0] > 30) or (d2[1] == i and d2[0] > 30):
            return -1
    first_date = day_of_year(d1[0],d1[1],d1[2])
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

print(date_diff("29-3-1999","30-3-2000"))