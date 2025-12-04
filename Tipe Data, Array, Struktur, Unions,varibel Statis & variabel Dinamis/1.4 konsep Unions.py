class MyUnion:
    def __init__(self):
        self.value = None

    def set_integer(self, x):
        self.value = x

    def set_float(self, x):
        self.value = x

    def set_string(self, x):
        self.value = x

# Penggunaan
u = MyUnion()
u.set_integer(10)
print("Union berisi integer:", u.value)

u.set_float(3.14)
print("Union berisi float:", u.value)

u.set_string("Hello")
print("Union berisi string:", u.value)

