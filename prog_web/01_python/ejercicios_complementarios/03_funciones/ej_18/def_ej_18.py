def month_days(month: int, year: int):
    '''
    Returns the amount of days in a month given its year.
    '''
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        if leap_year(year):
            return 29
        else:
            return 28
    else: 
        print("Mes incorrecto (Mes debe valer entre 1 y 12)")
        pass

def leap_year(year: int) -> bool:
    ''' 
    Returns True if the year is a leap year
    ex: 2004 returns True, 2003 returns False
    '''
    if year%4 == 0:
        return True
    else: 
        return False