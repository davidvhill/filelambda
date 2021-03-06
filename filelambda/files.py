"""Functions for working with files in python"""

import logging
import os

logger = logging.getLogger(__name__)

def read(path):
    """Read a text file.

    Args:
        path (str): Full path to file

    Returns:
        str: File text
    """

    logger.debug("Read file: {}".format(path))
    
    with open(path, 'r') as handle:
        return handle.read()


def readb(path):
    """Read a binary file.

    Args:
        path (str): Full path to file

    Returns:
        File bytes
    """

    logger.debug("Read binary file:{}".format(path))
    
    with open(path, 'rb') as handle:
        return handle.read()


def readlines(path):
    """Read lines from a text file.

    Args:
        path (str): Full path to file

    Returns:
        list: File text
    """

    logger.debug("Read lines:{}".format(path))
    
    with open(path, 'r') as handle:
        return handle.readlines()


def readlinesb(path):
    """Read lines from a binary file.

    Args:
        path (str): Full path to file

    Returns:
        list: File bytes
    """

    logger.debug("Read binary lines:{}".format(path))
    
    with open(path, 'rb') as handle:
        return handle.readlines()


def write(path, data):
    """Write data to a text file.

    Args:
        path (str): Full path to file
        data (str): File text

    Returns:
        int: Number of characters written
    """

    logger.debug("Write file:{}".format(path))
    
    with open(path, 'w') as handle:
        return handle.write(data)


def writeb(path, data):
    """Write data to a binary file.

    Args:
        path (str): Full path to file
        data (str): File bytes

    Returns:
        int: Number of bytes written
    """

    logger.debug("Write binary file:{}".format(path))
    
    with open(path, 'wb') as handle:
        return handle.write(data)


def append(path, data):
    """Append data to a text file.

    Args:
        path (str): Full path to file
        data (str): File text

    Returns:
        int: Number of characters appended
    """

    logger.debug("Append file:{}".format(path))
    
    with open(path, 'a') as handle:
        return handle.write(data)


def appendb(path, data):
    """Write data to a binary file.

    Args:
        path (str): Full path to file
        data (str): File bytes

    Returns:
        int: Number of bytes appended
    """

    logger.debug("Append binary file:{}".format(path))
    
    with open(path, 'ab') as handle:
        return handle.write(data)


def delete(path):
    """Delete a file.

    Args:
        path (str): Full path to file

    Returns:
        bool: True if the file was deleted, False if not (with message logged)
    """

    logger.debug("Delete file:{}".format(path))
    
    try:
        os.remove(path)
    except FileNotFoundError:
        pass
    except Exception as e:
        logger.error("Exception deleting file:{}".format(path))
        logger.error(e)
        return False
    return True


def exists(path):
    """Determine if a file exists.

    Args:
        path (str): Full path to file

    Returns:
        bool: True if the file exists, False if not
    """
    
    return os.path.exists(path) and os.path.isfile(path)


def mkdirs(filename):
    """Ensures the set of directories exist for the supplied filename.

    Args:
        filename (str): Full path to where the file should exist

    Returns:
       Full file path if the directories were created or None
    """

    logger.debug("mkdir:{}".format(filename))
    
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        return filename
    except:
        return None
