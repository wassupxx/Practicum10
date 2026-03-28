def print_common_multiples(A, B, N):
    """
    Выводит на экран в порядке возрастания все общие кратные для двух натуральных чисел A и B,
    не превосходящие N.

    Args:
        A (int): первое натуральное число
        B (int): второе натуральное число
        N (int): верхняя граница (кратные не должны превышать N)
    """

    if not all(isinstance(x, int) and x > 0 for x in [A, B, N]):
        print("Ошибка: все аргументы должны быть натуральными числами (целыми положительными)")
        return

    def gcd(a, b):
        """Находит наибольший общий делитель (НОД) чисел a и b"""
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        """Находит наименьшее общее кратное (НОК) чисел a и b"""
        return a * b // gcd(a, b)

    lcm_AB = lcm(A, B)

    if lcm_AB > N:
        print(f"Нет общих кратных для {A} и {B}, не превосходящих {N}")
        return

    current_multiple = lcm_AB
    while current_multiple <= N:
        print(current_multiple)
        current_multiple += lcm_AB


print_common_multiples(5, 9, 90)
