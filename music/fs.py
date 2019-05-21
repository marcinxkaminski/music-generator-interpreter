from music.log import get_logger

logger = get_logger(__name__)


def read(file_path):
    with open(file_path, 'r') as f:
        logger.info('Reading %s', file_path)
        return f.read()


async def write(file_path, data):
    with open(file_path, 'w') as f:
        f.write(data)
        logger.info('Wrote %s', file_path)


async def append(file_path, data):
    with open(file_path, 'a') as f:
        f.write(data)
        logger.info('Appended %s', file_path)
