def is_prime(num):
    """
    Логическая функция, определяющая, является ли число простым.
    Возвращает True, если число простое, и False в противном случае.
    """
    if num < 2:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2

    return True


def main():
    """
    Основная функция программы.
    Вводит число N и выводит все простые числа от 1 до N.
    """
    try:

        N = int(input("Введите натуральное число N: "))

        if N <= 0:
            print("Ошибка: N должно быть натуральным числом ( >0)")
            return

        prime_numbers = []
        for i in range(1, N + 1):
            if is_prime(i):
                prime_numbers.append(i)

        if prime_numbers:
            print(*prime_numbers)
        else:
            print(f"\nНет простых чисел в диапазоне от 1 до {N}")

    except ValueError:
        print("Ошибка: пожалуйста, введите целое число")


main()