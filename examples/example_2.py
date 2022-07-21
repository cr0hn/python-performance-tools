import os
import time

from performance_tools import *


def main():
    environment = os.environ.get("ENVIRONMENT", None)

    with catch_time("Example message 2", lambda: environment in ("DEVELOPMENT", "STAGING")):
        for i in range(10):
            time.sleep(0.1)


if __name__ == '__main__':
    main()
