from enum import Enum


class AttackType(Enum):
    HASH = 1
    FILE = 2

class HashType(Enum):
    SHA1 = 1
    SHA256 = 2


MIN_NODES = 2

NODES = {
    '\x00': (0, 0),
    '\x01': (0, 1),
    '\x02': (0, 2),
    '\x03': (1, 0),
    '\x04': (1, 1),
    '\x05': (1, 2),
    '\x06': (2, 0),
    '\x07': (2, 1),
    '\x08': (2, 2)
}


def open_key_file(file_path: str):
    """
    Open the key file (like gesture.key) and return the hash value, in hex
    """

    with open(file_path, 'rb') as file:
        data = file.read()

    return data.hex()