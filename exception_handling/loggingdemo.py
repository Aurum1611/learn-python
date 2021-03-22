import logging

logging.basicConfig(filename="niFile.log",level=logging.INFO)
logging.critical("Critical")
logging.error("Error")
logging.warning("Warning")
logging.info("Information")
logging.debug("Debug")

""" Warning is the default log level.
Whatever lever comes above this level is printed onto the log.
Whatever level comes below this level isn't. """