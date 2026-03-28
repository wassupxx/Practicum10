from datetime import datetime


def convert_datetime(datetime_str):
    """
        Преобразует строку с датой и временем из формата "MM/DD/YYYY HR:MIN:SEC"
        в формат "DD.MM.YY HR:MIN:SEC AM/PM" (12‑часовой формат).

        Args:
            datetime_str (str): дата и время в формате "MM/DD/YYYY HR:MIN:SEC"
    """
    try:

        input_datetime = datetime.strptime(datetime_str, "%m/%d/%Y %H:%M:%S")

        day = input_datetime.day
        month = input_datetime.month
        year = input_datetime.year
        hour_24 = input_datetime.hour
        minute = input_datetime.minute
        second = input_datetime.second

        year_short = year % 100

        if hour_24 == 0:
            hour_12 = 12
            period = "AM"
        elif hour_24 < 12:
            hour_12 = hour_24
            period = "AM"
        elif hour_24 == 12:
            hour_12 = 12
            period = "PM"
        else:
            hour_12 = hour_24 - 12
            period = "PM"

        result = f"{day:02d}.{month:02d}.{year_short:02d} {hour_12:02d}:{minute:02d}:{second:02d} {period}"
        print(result)

    except ValueError:
        print("Ошибка: некорректный формат даты или неверные данные.")


convert_datetime()
