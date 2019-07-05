class Friend:
    def __init__(self, age, address, color, is_bobo):
        self.age = age
        self.address = address
        self.color = color
        self.is_bobo = is_bobo

    def is_matanda(self):
        if self.age > 18:
            return True
        else:
            return False

    def ambobo(self):
        print("Ambobo mo!")

