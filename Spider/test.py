
from multiprocessing import Pool
def main(num):
    print("hello"+str(num))
if __name__ == '__main__':
    pool = Pool()
    groups = ([x for x in range(10)])
    pool.map(main, groups)
    pool.close()
    pool.join()