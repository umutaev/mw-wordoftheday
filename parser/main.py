import logging

import request

logger = logging.getLogger("parser")
logger.setLevel("DEBUG")
fh = logging.FileHandler("./test.log", "a", "utf-8")
formatter = logging.Formatter(
    "%(asctime)s - %(name)s [%(levelname)s]: %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

if __name__ == "__main__":
    logger.info("Initializing Request().")
    r = request.Request()
    print(r.__repr__())
    print(str(r))
