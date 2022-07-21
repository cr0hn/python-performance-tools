import time

from performance_tools import *


def main():
    with catch_time("Example message"):
        for i in range(10):
            time.sleep(0.1)


if __name__ == '__main__':
    main()
