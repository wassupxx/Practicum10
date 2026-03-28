def row(A, B):
    """
        Печатает в порядке возрастания все числа в диапазоне от A до B (включительно),
        которые содержат только цифры из множества {1, 3, 4, 8, 9}.

        Если A > B, значения меняются местами перед обработкой.

        Args:
            A (int): начало диапазона
            B (int): конец диапазона
    """
    if A > B:
        A, B = B, A
    numbers = {1, 3, 4, 8, 9}
    for num in range(A, B + 1):
        for digit in str(num):
            if int(digit) in numbers:
                print(num)
                break


row()
