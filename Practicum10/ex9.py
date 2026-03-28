from datetime import datetime


def seconds_since_year(datetime_str):
    """
        Принимает строку с датой и временем в формате "MM/DD/YYYY HR:MIN:SEC"
        и возвращает количество секунд, прошедших с "01/01/YYYY 00:00:00".

        Args:
            dateime_str (str): дата и время в формате "MM/DD/YYYY HR:MIN:SEC"

        Returns:
            int: количество секунд с начала года
        """
    datetime_datetime = datetime.strptime(datetime_str, "%m/%d/%Y %H:%M:%S")
    year = datetime_datetime.year
    start_year = datetime(year, 1, 1, 0, 0, 0)
    time_difference = datetime_datetime - start_year
    return time_difference.total_seconds()


print(seconds_since_year())
