class vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return f"({self.x}, {self.y})"


class vector3d(vector2d):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def show(self):
        return f"({self.x}, {self.y}, {self.z})"

o = vector2d(1, 2)
print(o.show())
p = vector3d(3,4, 5)
print(p.show())