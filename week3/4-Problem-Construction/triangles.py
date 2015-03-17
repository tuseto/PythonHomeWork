def is_triangle(a, b, c):
    return a < b + c and b < a + c and c < b + a

from math import sqrt


def area(a, b, c):
    p = (a + b + c) / 2
    return sqrt((p*(p-a)*(p-b)*(p-c)))


def is_pythagorean(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


def max_area(triangles):
    max_area = 0
    
    for triangle in triangles:
        areas = area(triangle[0],triangle[1],triangle[2])
        if areas > max_area:
            max_area = areas
            biggest_triangle = [triangle[0],triangle[1],triangle[2]]
    return biggest_triangle


print(max_area([[5,5,5],[1,1,1],[11,11,11]]))




