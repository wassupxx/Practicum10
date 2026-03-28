def discounts(purchase, card, holiday):
    """
        Рассчитывает окончательную стоимость покупки с учётом всех скидок.

        Args:
            purchase (float): стоимость покупки (неотрицательное число с 
            не более чем 2 знаками после запятой)
            card (bool): True, если есть дисконтная карта
            holiday (bool): True, если день праздничный
    """
    if not holiday and not card:
        if purchase > 30000:
            good = purchase * 0.9
        if 20000 < purchase <= 30000:
            good = purchase * 0.93
        if 15000 < purchase <= 20000:
            good = purchase * 0.95
        if 5000 < purchase <= 15000:
            good = purchase * 0.97
        if purchase <= 5000:
            good = purchase
    if card and not holiday:
        if purchase > 30000:
            good = purchase * 0.85
        if 20000 < purchase <= 30000:
            good = purchase * 0.88
        if 15000 < purchase <= 20000:
            good = purchase * 0.9
        if 5000 < purchase <= 15000:
            good = purchase * 0.92
        if purchase <= 5000:
            good = purchase * 0.95
    if not card and holiday:
        if purchase > 30000:
            good = purchase * 0.87
        if 20000 < purchase <= 30000:
            good = purchase * 0.9
        if 15000 < purchase <= 20000:
            good = purchase * 0.92
        if 5000 < purchase <= 15000:
            good = purchase * 0.94
        if purchase <= 5000:
            good = purchase * 0.97
    if card and holiday:
        if purchase > 30000:
            good = purchase * 0.85
        if 20000 < purchase <= 30000:
            good = purchase * 0.85
        if 15000 < purchase <= 20000:
            good = purchase * 0.87
        if 5000 < purchase <= 15000:
            good = purchase * 0.89
        if purchase <= 5000:
            good = purchase * 0.92
    print(good)


discounts(30000, False, True)
