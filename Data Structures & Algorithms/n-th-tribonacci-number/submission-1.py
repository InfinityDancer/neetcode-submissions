class Solution:
    def __init__(self):
        self.fib_list = [0] * 38

        self.fib_list[0] = 0
        self.fib_list[1] = 1
        self.fib_list[2] = 1

        print(self.fib_list)

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return self.fib_list[0]

        if self.fib_list[n] != 0:
            return self.fib_list[n]
        
        fib_prev = self.tribonacci(n - 1)
        fib_prev_2 = self.tribonacci(n - 2)
        fib_prev_3 = self.tribonacci(n - 3)

        self.fib_list[n] = fib_prev + fib_prev_2 + fib_prev_3

        return self.fib_list[n]
        