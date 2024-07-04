#!/usr/bin/python3
"""
This module contains the function canUnlockAll that determines if
all boxes can be opened
"""

from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determines if all boxes can be opened.

    Args:
        boxes: A lsit of lists

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    unlocked = set([0])
    keys = [0]

    while keys:
        key = keys.pop()
        for new_key in boxes[key]:
            if new_key not in unlocked and new_key < len(boxes):
                unlocked.add(new_key)
                keys.append(new_key)

    return len(unlocked) == len(boxes)
