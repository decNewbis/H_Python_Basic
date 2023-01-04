from __future__ import annotations


class VectorXYZ:
    def __init__(self, x: int | float, y: int | float, z: int | float):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: VectorXYZ | int | float):
        if isinstance(other, VectorXYZ):
            return VectorXYZ(self.x + other.x, self.y + other.y, self.z + other.z)
        if isinstance(other, int | float):
            return VectorXYZ(self.x + other, self.y + other, self.z + other)
        return NotImplemented

    def __radd__(self, other: VectorXYZ | int | float | tuple):
        return self.__add__(other)

    def __mul__(self, other: VectorXYZ | int | float):
        if isinstance(other, VectorXYZ):
            return self.x * other.x + self.y * other.y + self.z * other.z
        if isinstance(other, int | float):
            return VectorXYZ(self.x * other, self.y * other, self.z * other)
        return NotImplemented

    def __rmul__(self, other: VectorXYZ | int | float | tuple):
        return self.__mul__(other)

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'


if __name__ == '__main__':
    vector_1 = VectorXYZ(1, 1, 1)
    vector_2 = VectorXYZ(2, 2, 2)

    assert str(vector_1 + vector_2) == '(3, 3, 3)', 'vector_1 + vector_2'
    assert isinstance(vector_1 + vector_2, VectorXYZ), 'isinstance(vector_1 + vector_2, VectorXYZ)'

    assert str(vector_1 + 3) == '(4, 4, 4)', 'vector_1 + 3'
    assert isinstance(vector_1 + 3, VectorXYZ), 'isinstance(vector_1 + 3, VectorXYZ)'

    assert str(3 + 3 + vector_1) == '(7, 7, 7)', '3 + 3 + vector_1'
    assert isinstance(3 + 3 + vector_1, VectorXYZ), 'isinstance(3 + 3 + vector_1, VectorXYZ)'

    assert str(vector_1 * vector_2) == '6', 'vector_1 * vector_2'
    assert isinstance(vector_1 * vector_2, int), 'isinstance(vector_1 * vector_2, VectorXYZ)'

    assert str(vector_1 * 3) == '(3, 3, 3)', 'vector_1 * 3'
    assert isinstance(vector_1 * 3, VectorXYZ), 'isinstance(vector_1 * 3, VectorXYZ)'

    assert str(3 * 3 * vector_1) == '(9, 9, 9)', '3 * 3 * vector_1'
    assert isinstance(3 * 3 * vector_1, VectorXYZ), '3 * 3 * vector_1, VectorXYZ)'
