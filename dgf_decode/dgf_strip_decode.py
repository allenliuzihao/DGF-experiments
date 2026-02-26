from enum import Enum
import sys

'''
    This code is a Python implementation of the triangle strip decoding algorithm described in the paper 
        DGF: A Dense, Hardware-Friendly Geometry Format for Lossily Compressing Meshlets with Arbitrary Topologies (HPG 2024)
'''

class ControlBit(Enum):
    RESTART = 1
    EDGE1 = 2
    EDGE2 = 3
    BACKTRACK = 4

def count_first_index(firstIndex: list[bool], index: int):
    count = 0
    for i in range(index):
        if firstIndex[i]:
            count = count + 1
    return count

def decode_strip_data(triangleIndex: int, controls: list[ControlBit], firstIndex : list[bool], reuseIndex: list[int]):
    r = 1
    indexAddress = [0, 1, 2]
    bt = None
    prevControl = None
    prev = None
    for k in range(1, triangleIndex + 1):
        control = controls[k]
        prev = indexAddress.copy()
        if control == ControlBit.RESTART:
            r = r + 1
            indexAddress = [ 2 * r + triangleIndex - 2, 2 * r + triangleIndex - 1, 2 * r + triangleIndex ]
        elif control == ControlBit.EDGE1:
            indexAddress = [prev[2], prev[1], 2 * r + k]
            bt = prev[0]
        elif control == ControlBit.EDGE2:
            indexAddress = [prev[0], prev[2], 2 * r + k]
            bt = prev[1]
        elif control == ControlBit.BACKTRACK:
            if prevControl == ControlBit.EDGE1:
                indexAddress = [bt, prev[0], 2 * r + k]
            else:
                indexAddress = [prev[1], bt, 2 * r + k]
        prevControl = control
    for k in range(3):
        vid = count_first_index(firstIndex, indexAddress[k])
        if indexAddress[k] >= 1 and firstIndex[indexAddress[k] - 1] == False:
            vid = reuseIndex[indexAddress[k] - vid - 1]        
        print(f"triangle {triangleIndex} -> vertex id: {vid}")

if __name__ == "__main__":
    controls = [
        ControlBit.RESTART, 
        ControlBit.EDGE1, 
        ControlBit.EDGE2, 
        ControlBit.EDGE1, 
        ControlBit.EDGE1,
        ControlBit.EDGE2,
        ControlBit.EDGE2,
        ControlBit.EDGE2,
        ControlBit.EDGE1,
        ControlBit.EDGE1,
        ControlBit.EDGE2
    ]
    firstIndex = [
        True, True, True, True, True, False, True, True, False, True, True, False
    ]
    reuseIndex = [1, 4, 4]
    triangleIndex = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    
    # see https://www.youtube.com/watch?v=FG1F_qPUX0s&t=5m58s for the example of triangle strip and the control bits
    decode_strip_data(triangleIndex, controls, firstIndex, reuseIndex)