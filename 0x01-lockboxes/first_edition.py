
2	
3	def open_box(boxes, keys=[], visted_boxes = []):
4	    for i in keys:
5	        if i not in visted_boxes:
6	            visted_boxes.append(i)
7	            open_box(boxes, boxes[i], visted_boxes)
8	    if (len(boxes) - 1) == len(visted_boxes):
9	        return True
10	    return False
11	
12	def canUnlockAll(boxes):
13	    """check for if the boxes contain keys for all other boxes or not"""
14	    start_box = boxes[0]
15	    visted_boxes = []
16	    result = open_box(boxes, start_box, visted_boxes)
17	
18	    return result
19	
20	
21	
22	boxes = [[1], [2], [3], [4], []]
23	print(canUnlockAll(boxes))
24	
25	boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
26	print(canUnlockAll(boxes))
27	
28	boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
29	print(canUnlockAll(boxes))
