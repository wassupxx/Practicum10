def make_payment(P):
    """
    Проверяет корректность платежа по кредитной карте и выводит результат.

    Args:
        P: сумма платежа (должна быть числом)

    Условия:
        - минимальный платёж: $20;
        - кредитный лимит: $1000.
    """

    min_payment = 20
    credit_limit = 1000

    try:
        payment = float(P)

        if payment >= min_payment and payment <= credit_limit:
            print("Успех!")
        else:
            if payment < min_payment:
                print(f"Повторите попытку. Сумма ({payment}) меньше минимального платежа ({min_payment}).")
            else:
                print(f"Повторите попытку. Сумма ({payment}) превышает кредитный лимит ({credit_limit}).")

    except (ValueError, TypeError):
        print("Повторите попытку. Введите корректное числовое значение.")


make_payment(10)
