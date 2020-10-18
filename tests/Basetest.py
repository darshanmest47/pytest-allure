import inspect
import logging

import pytest


@pytest.mark.usefixtures("setup")
class Basetest:

    def logger_finc(self):
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        filehandler = logging.FileHandler('files.log')
        formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)')
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)

        logger.setLevel('DEBUG')

        return logger



