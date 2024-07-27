class Cube:
    def __init__(self, N):
        self.N = N

    def getVolume(self):
        Volume = self.N ** 3
        return Volume

    def getSurfaceArea(self):
        SurfaceArea = self.N * self.N * 6
        return SurfaceArea

x = int(input())

c = Cube(x)

v = c.getVolume()
print(v)

s = c.getSurfaceArea()

print(s)