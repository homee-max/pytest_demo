

class Calculator:
    def add(self, x, y) -> int:
        return x + y

    def subtract(self, x, y) -> int:
        return x - y

    def multiply(self, x, y) -> int:
        if x > 10:
            print('x>10')
        return x * y 
