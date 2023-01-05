class FibonacciIterator:
    def __init__(self, n: int):
        if n > 0:
            self.end = n
        else:
            self.end = 0
        self.prev = -1
        self.next = 1
        self.iterator = -1

    def __iter__(self):
        return self

    def __next__(self):
        current = self.prev + self.next
        if current <= self.end:
            self.prev, self.next = self.next, self.prev + self.next
            self.iterator += 1
            return current
        else:
            raise StopIteration

    def check_iteration_parity(self):
        if self.iterator % 2 == 0:
            return True
        return False


if __name__ == '__main__':
    fb = FibonacciIterator(13)
    for it_num, el in enumerate(fb):
        print(f'Fibonacci num: {el}. Iterator num: {it_num}. Even iteration: {fb.check_iteration_parity()}')
