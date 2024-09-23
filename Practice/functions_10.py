
def is_leap_year(year):
    if(year%4==0 or year%100==0 and year%400==0):
        print(f"{year} is a leap year")
    else: 
        print(f"{year} is not a leap year")

is_leap_year(1989)