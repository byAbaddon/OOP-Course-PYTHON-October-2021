class Stack:
    data = []

    def push(self, el):
        if isinstance(el, str):
            self.data.append(el)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return False if self.data else True

    def __repr__(self):
        return f"[{', '.join(self.data[::-1])}]"


