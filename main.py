from multiprocessing import Pool
from time import time


def factorize(*number):
    res = []
    for ix, n in enumerate(number):
        res.append([])
        for i in range(n+1):
            if n % (i+1) == 0:
                res[ix] += [i+1]
    if len(number) == 1:
        res = res[0]
    return res


if __name__ == '__main__':
    factorize(55555)
    # synchronous
    start_time = time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    print("Execution time for synchronous is %s seconds" % (time() - start_time))
    # Execution time for synchronous is 0.7808823585510254 seconds

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]
    start_time = time()
    with Pool(processes=4) as pool:
        a, b, c, d = pool.map(factorize, (128, 255, 99999, 10651060,))
    print("Execution time for asynchronous is %s seconds" % (time() - start_time))
    # Execution time for asynchronous is 0.9753804206848145 seconds

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]