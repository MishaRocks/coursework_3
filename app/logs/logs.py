import logging
formatter = logging.Formatter("%(asctime)s :: [%(levelname)s] :: %(message)s :: %(pathname)s")


def my_logger(name, file, level=logging.INFO):
    file_handler = logging.FileHandler(file)
    file_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)

    return logger
