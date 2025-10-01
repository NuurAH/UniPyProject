import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import os
#present and parent directory set up, most important
pw_directory = str(Path(__file__).resolve().parent)
parent_directory = Path(pw_directory).parent
#create logger
logger = logging.getlogger("UniProjectToolkit_logger")
logger.setlevel(logging.DEBUG) #This can be changed 

#making a stream handler, adapted from tutorial

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_formatter = logging.Formatter("%(levelname)s [%(asctime)s] %(message)s" )
stream_handler.setFormatter(stream_formatter)

#working on rotating file handler
