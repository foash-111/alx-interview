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
    remain_bytes = 0
    # num_bytes = 0

    # if it list we will itarate over it
    # if it string we will itarate over it's characters

    for i in data:
        # Convert the integer to a binary string of 8 bits
        binary_representation = format(i, '08b')

        if remain_bytes == 0:
            if binary_representation[0] == '0':
                continue  # 1 byte character
            elif binary_representation[:3] == '110':
                # num_bytes = 2
                remain_bytes = 1
            elif binary_representation[:4] == '1110':
                # num_bytes = 3
                # the next 2 numbers (bytes) Expected to start with 10xx xxxx
                # if number[0] == '1110 XXXX' so it's 3 bytes number and,
                # it's expected the number in [1], [2] to consider as:
                # continution bytes and start with '10xxx xxxx'

                remain_bytes = 2
            elif binary_representation[:5] == '11110':
                # num_bytes = 4
                remain_bytes = 3
            else:
                # Invalid UTF-8 start byte
                return False
        else:
            #  Continuation byte must start with '10'
            if binary_representation[:2] != '10':  # continue byte
                return False
            remain_bytes -= 1
    # If we're expecting continuation bytes but didn't get them
    return remain_bytes == 0
