#!/usr/bin/env python3

"""validate utf-8"""


def validUTF8(data):
    """Encoding (s.encode('utf-8')):
    This part of the expression takes the string s
    and converts it into a sequence of bytes
    using UTF-8 encoding.
    Decoding (decode('utf-8')):
    After encoding the string into bytes,
    the .decode('utf-8') method
    is called on the resulting bytes object.
    """
    if isinstance(data, str):
        try:
            data.encode('utf-8').decode('utf-8')
            return True
        except UnicodeDecodeError:
            return False
    else:
        if isinstance(data, list):
            for i in data:
                if isinstance(i, int):
                    result = i & 255
                    if result == i:
                        pass
                    else:
                        return False
    return True
