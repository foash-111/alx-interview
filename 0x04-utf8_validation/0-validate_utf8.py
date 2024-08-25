#!/usr/bin/python3

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
    bytes_remaining = 0

    for num in data:
        # Convert the integer to a binary string of 8 bits
        bin_rep = format(num, '#010b')[-8:]

        if bytes_remaining == 0:
            # Determine the number of bytes in the UTF-8 character
            if bin_rep[0] == '0':
                continue  # 1-byte character
            elif bin_rep[:3] == '110':
                bytes_remaining = 1  # 2-byte character
            elif bin_rep[:4] == '1110':
                bytes_remaining = 2  # 3-byte character
            elif bin_rep[:5] == '11110':
                bytes_remaining = 3  # 4-byte character
            else:
                return False  # Invalid UTF-8 start byte
        else:
            # Continuation byte must start with '10'
            if bin_rep[:2] != '10':
                return False
            bytes_remaining -= 1

    # If we're expecting continuation bytes but didn't get them
    return bytes_remaining == 0
