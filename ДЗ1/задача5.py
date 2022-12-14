# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt

xA = float(input('Введите координату точки А по оси Х: '))
yA = float(input('Введите координату точки А по оси Y: '))
xB = float(input('Введите координату точки B по оси Х: '))
yB = float(input('Введите координату точки B по оси Y: '))
distance = round(sqrt((xB - xA)**2 + (yB - yA)**2), 2)
print(distance)