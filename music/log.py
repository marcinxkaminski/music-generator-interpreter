import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(name)s | %(message)s')
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')
handler = logging.FileHandler('music.log')
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)

def get_logger(name):
  logger = logging.getLogger(name)
  logger.addHandler(handler)
  return logger