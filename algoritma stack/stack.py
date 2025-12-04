# ====================================
# IMPLEMENTASI STACK
# ====================================

class Stack:
    def __init__(self):
        self.data = []  # array sebagai stack

    # PUSH
    def push(self, item):
        self.data.append(item)
        print(f"{item} ditambahkan ke stack.")

    # POP
    def pop(self):
        if self.is_empty():
            print("Stack kosong, tidak bisa POP.")
            return None
        return self.data.pop()

    # PEEK
    def peek(self):
        if self.is_empty():
            print("Stack kosong.")
            return None
        return self.data[-1]

    # CEK KOSONG
    def is_empty(self):
        return len(self.data) == 0

    # SIZE
    def size(self):
        return len(self.data)


# ====================================
# CONTOH PENGGUNAAN
# ====================================

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("\nElemen teratas:", stack.peek())
print("Ukuran stack:", stack.size())

print("\nPOP:", stack.pop())
print("POP:", stack.pop())

print("Stack kosong?", stack.is_empty())
