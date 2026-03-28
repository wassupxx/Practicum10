import turtle


def draw_triangle(x1, y1, x2, y2, x3, y3, color):
    """
    Рисует треугольник по координатам вершин с заданным цветом заливки.
    """
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()

    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)

    turtle.end_fill()


def draw_square(x, y, side, color1, color2):
    """
    Рисует квадрат из двух треугольников.
    """
    x1, y1 = x, y
    x2, y2 = x + side, y
    x3, y3 = x + side, y + side
    x4, y4 = x, y + side

    draw_triangle(x1, y1, x2, y2, x3, y3, color1)

    draw_triangle(x1, y1, x3, y3, x4, y4, color2)


def draw_pattern(rows, cols, tile_size, color1, color2):
    """
    Рисует узор кафельной плитки.
    """
    for row in range(rows):
        for col in range(cols):
            x = col * tile_size
            y = row * tile_size

            if (row + col) % 2 == 0:
                draw_square(x, y, tile_size, color1, color2)
            else:
                draw_square(x, y, tile_size, color2, color1)


def main():
    """
    Главная функция программы
    """
    print("=== Программа для рисования кафельной плитки ===")
    print()

    try:
        rows = int(input("Введите количество рядов плитки: "))
        cols = int(input("Введите количество столбцов плитки: "))
        tile_size = int(input("Введите размер плитки: "))
        color1 = input("Введите первый цвет: ")
        color2 = input("Введите второй цвет: ")

        if rows <= 0 or cols <= 0 or tile_size <= 0:
            print("Ошибка: количество рядов, столбцов и размер должны быть положительными числами!")
            return

        turtle.delay(0)
        turtle.bgcolor("white")

        draw_pattern(rows, cols, tile_size, color1, color2)

        turtle.hideturtle()
        turtle.done()

    except ValueError:
        print("Ошибка: пожалуйста, введите корректные числа!")


main()
