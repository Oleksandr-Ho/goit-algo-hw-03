import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  # Найвища швидкість
    t.penup()
    t.goto(-size / 2, size / 2 / 3**0.5)  # Початкова позиція для сніжинки Коха
    t.pendown()

    for _ in range(3):  # Створення трьох сторін сніжинки
        koch_curve(t, order, size)
        t.right(120)  # Поворот для створення наступної сторони

    window.mainloop()  # Залишає вікно відкритим після завершення малювання

# Виклик функції
order = int(input("Введіть рівень рекурсії: "))  # Дозволяє користувачу вказати рівень рекурсії
draw_koch_snowflake(order)
