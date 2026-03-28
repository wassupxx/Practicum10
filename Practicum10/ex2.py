def fibonacci():
    """
        Печатает первые n чисел последовательности Фибоначчи.

        Args:
            N (int): количество чисел Фибоначчи для вывода
    """
    N = int(input())
    a, b = 1, 1
    for num in range(N):
        print(a, end=' ')
        a, b = b, a + b


fibonacci()
