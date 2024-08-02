#!/usr/bin/python3
"""0-lockboxes.py"""


def canUnlockAll(boxes):
    """check for if the boxes contain keys for all other boxes or not"""
    my_list = []
    for i in boxes:
        for j in i:
            my_list.append(j)
    for k in range(1, len(boxes)):
        if k in my_list:
            pass
        else:
            return False
    return True
