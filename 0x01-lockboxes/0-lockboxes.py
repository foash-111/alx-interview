#!/usr/bin/python3
"""0-lockboxes.py"""


def open_box(boxes, cur_box=[], visted_boxes = [], cur_key=0, index=0):
    # 1 4 6
    if cur_key not in visted_boxes: # 1 
        visted_boxes.append(cur_key) #
        if index < (len(cur_box) - 1):
            next_key= cur_box[index + 1] # 4
            if next_key < (len(boxes)):
                next_box = boxes[next_key]
                open_box(boxes, next_box, visted_boxes, next_key,index + 1)

    if (len(boxes) - 1) == len(visted_boxes):
        return True
    return False

def canUnlockAll(boxes):
    """check for if the boxes contain keys for all other boxes or not"""
    cur_box = boxes[0] # start_box
    cur_key = cur_box[0]
    visted_boxes = []
    index = 0

    result = open_box(boxes, cur_box, visted_boxes, cur_key, index)

    return result
