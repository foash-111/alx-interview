#!/usr/bin/env python3

def validUTF8(data):
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
