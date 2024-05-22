month = int(input('Введите номер месяца:'))
def month_to_season(month):
 
 seasons = {
        1: "Зима",
        2: "Зима",
        3: "Весна",
        4: "Весна",
        5: "Весна",
        6: "Лето",
        7: "Лето",
        8: "Лето",
        9: "Осень",
        10: "Осень",
        11: "Осень",
        12: "Зима"
    }
 if month < 1 or month > 12:
        return "Некорректный месяц"
 else:
        return seasons[month]
    
season = month_to_season(month)
print(season)