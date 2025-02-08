import turtle

def draw_koch_snowflake(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_snowflake(t, length, level - 1)
        t.left(60)
        draw_koch_snowflake(t, length, level - 1)
        t.right(120)
        draw_koch_snowflake(t, length, level - 1)
        t.left(60)
        draw_koch_snowflake(t, length, level - 1)

def main():
    try:
        level = int(input("Введіть рівень рекурсії (наприклад, 3): "))
        if level < 0:
            raise ValueError("Рівень рекурсії має бути невід'ємним цілим числом.")
    except ValueError as e:
        print(f"Помилка: {e}")
        return

    # Налаштування екрану Turtle
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.title("Сніжинка Коха")

    # Налаштування Turtle
    t = turtle.Turtle()
    t.speed(1000)
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    # Малювання сніжинки Коха
    for _ in range(3):
        draw_koch_snowflake(t, 400, level)
        t.right(120)

    # Завершення роботи
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
