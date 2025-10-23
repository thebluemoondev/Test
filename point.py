import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def di_chuyen(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def tinh_khoang_cach(self, point):
        print(math.sqrt(pow((self.x - point.x), 2) + pow((self.y - point.y), 2)))

p1 = Point(1, 1)
p2 = Point(4, 5)

p1.di_chuyen(2, 1)

khoang_cach = p1.tinh_khoang_cach(p2)