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

print(day_of_year(30,12,2000))