# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of():
    month = int((input('Введите номер месяца: ')))

    if month == 1:
        print('Месяц 1 (Январь). является частью первого квартала')
    elif month == 2:
        print('Месяц 2 (Февраль). является частью первого квартала')
    elif month == 3:
        print('Месяц 3 (Март). является частью первого квартала')
    elif month == 4:
        print('Месяц 4 Апрель. является частью второго квартала')
    elif month == 5:
        print('Месяц 5 (май). является частью второго квартала')
    elif month == 6:
        print('Месяц 6 (Июнь). является частью второго квартала')
    elif month == 7:
        print('Месяц 7 (Июль). является частью третьего квартала')
    elif month == 8:
        print('Месяц 8 (Август). является частью третьего квартала')
    elif month == 9:
        print('Месяц 9 (Сентябрь). является частью третьего квартала')
    elif month == 10:
        print('Месяц 10 (Октябрь). является частью четвортого квартала')
    elif month == 11:
        print('Месяц 11 (Ноябрь). является частью четвортого квартала')
    elif month == 12:
        print('Месяц 12 (Декабрь). является частью четвортого квартала')
    elif month > 12:
        print('Такого месяца не существует')
quarter_of()