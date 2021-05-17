class IMath:
    def add(self, x, y):
        pass

    def sub(self, x, y):
        pass

    def mul(self, x, y):
       pass

    def div(self, x, y):
        pass

class Math(IMath):
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y

class Proxy(IMath):
    def __init__(self):
        self.math = None

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y
    def mul(self, x, y):
        if not self.math:
            self.math = Math()
        return self.math.mul(x, y)

    def div(self, x, y):
        if y == 0:
            return float('inf')
        if not self.math:
            self.math = Math()
        return self.math.div(x, y)

p = Proxy()
x, y = 4, 2
print('4 + 2 = ' + str(p.add(x, y)))
print('4 - 2 = ' + str(p.sub(x, y)))
print('4 * 2 = ' + str(p.mul(x, y)))
print('4 / 2 = ' + str(p.div(x, y)))