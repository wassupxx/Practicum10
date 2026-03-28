def card():
    """
    Рассчитывает денежный эквивалент телефонной карты с учётом бонусов.

    Args:
        payment (int): стоимость карты в долларах

    Returns:
        equivalent: общий денежный эквивалент карты (номинал + бонус)
    """
    payment = int(input("Enter a payment: "))
    while payment not in (5, 10, 25, 50, 100):
        payment = int(input("Enter a payment: "))
    if payment == 5 or 10:
        equivalent = payment
    if payment == 25:
        equivalent = payment + 3
    if payment == 50:
        equivalent = payment + 8
    if payment == 100:
        equivalent = payment + 20
    return equivalent


print(card())
