class ThreeVector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def addition(self):
        a = self.x + 4
        b = self.y + 5
        c = self.z + 6
        print((self.x, self.y, self.z), '+', (4, 5, 6), '=', (a, b, c))

    def subtraction(self):
        a = self.x - 4
        b = self.y - 5
        c = self.z - 5
        print((self.x, self.y, self.z), '-', (4, 5, 6), '=', (a, b, c))

    @staticmethod
    def inner_product(x, y, z):
        a = x * 4
        b = y * 5
        c = z * 6
        return a + b + c


ThreeVector(1, 2, 3).addition()
ThreeVector(1, 2, 3).subtraction()
print((1, 2, 3), '·', (4, 5, 6), '=', ThreeVector(1, 2, 3).inner_product(1, 2, 3))
