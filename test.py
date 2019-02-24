import time
from multiprocessing import Pool


def run(fn):
    time.sleep(1)
    return fn*fn


if __name__ == '__main__':
    test = [1, 2, 3, 4, 5, 6, 7, 8]
    s = time.time()
    for fn in test:
        run(fn)
    e = time.time()
    print('执行时间:', e - s)
    pool = Pool(processes=8)
    r = pool.map(run, test)
    pool.close()
    pool.join()
    e1 = time.time()
    print('执行时间:', e1 - e)