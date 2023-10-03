import threading

from functools import lru_cache


class Facto:

    def __init__(self):
        self.result = 1
        self.lock = threading.Lock()

    def factorial(self, start, end):
        for i in range(start, end + 1):
            self.lock.acquire()
            self.result *= i
            self.lock.release()

    @lru_cache()
    def calculate_factorial(self, n):
        self.result = 1
        thread1 = threading.Thread(target=self.factorial, args=(1, n // 2))
        thread2 = threading.Thread(target=self.factorial, args=(n // 2 + 1, n))
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
        return self.result


if __name__ == '__main__':
    number = 10

    facto = Facto()
    print(facto.calculate_factorial(12342))