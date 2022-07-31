import random
import time

from threading import Thread

class TicToc:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2 - self.t1

class FindPi:
    def __init__(self):
        self.i = 0
        self.n = 0

    def throw_points(self, nn):
        for i in range(nn):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            r = x**2 + y**2
            self.n += 1
            if r <=  1:
                self.i += 1

    def value_of_pi(self):
        return 4 * self.i / self.n


if __name__ == "__main__":
    tt = TicToc()
    tt.tic()
    finding_pi = FindPi()
    n = 10000000
    #finding_pi.throw_points(10000000)
    Thread(target=finding_pi.throw_points, args=(n, )).start()
    for _ in range(25):
        pi = finding_pi.value_of_pi()
        print("pi=%.5f | i=%d | n=%d | time=%.5f seconds" % (pi, finding_pi.i, finding_pi.n, tt.toc()))
        time.sleep(1)