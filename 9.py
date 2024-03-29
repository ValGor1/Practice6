import turtle

# Функция для рисования окружности
def draw_circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.circle(radius)


# Функция для вычисления расстояния между центрами окружностей
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


# Заданные координаты центров и радиусы окружностей
center1 = [int(x) for x in input('Введите координаты центра первой окружности через пробел: ').split()]
radius1 = int(input('Введите радиус первой окружности: '))
center2 = [int(x) for x in input('Введите координаты центра второй окружности через пробел: ').split()]
radius2 = int(input('Введите радиус второй окружности: '))

# Нарисовать первую окружность
draw_circle(center1[0], center1[1], radius1, 'blue')

# Нарисовать вторую окружность
draw_circle(center2[0], center2[1], radius2, 'green')

# Определить расстояние между центрами окружностей
dist = distance(center1[0], center1[1], center2[0], center2[1])

# Определить относительное положение окружностей
if dist > radius1 + radius2:
    print('Окружности лежат одна вне другой, не касаясь')
elif dist == radius1 + radius2:
    print('Окружности имеют внешнее касание')
elif dist < radius1 + radius2 and dist > abs(radius1 - radius2):
    print('Окружности пересекаются')
elif dist == abs(radius1 - radius2):
    print('Окружности имеют внутреннее касание')
elif dist < abs(radius1 - radius2):
    print('Одна окружность лежит внутри другой, не касаясь')

turtle.done()