import logging
import os
from pathlib import Path


def file_upload():
    path_to_file = os.path.dirname(__file__) + '/file.txt'
    file_path = Path(path_to_file)
    size = os.stat(file_path).st_size

    if size is 0:
        logging.error('The file is empty!')
        return False
    else:
        logging.debug('Opening file:    {}'.format(file_path))
        logging.debug('File size:       {} bytes.'.format(size))
        file = open(Path(path_to_file))
        content = file.read()
        file.close()
        return content.lower()
