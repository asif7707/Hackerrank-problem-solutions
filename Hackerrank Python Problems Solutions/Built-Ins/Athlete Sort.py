#!/bin/python3

import math
import os
import random
import re
import sys


def sub_list(lis, sort_k):
    lis.sort(key=lambda x: x[sort_k])
    return lis


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    for arg in sub_list(arr, k):
        print(*arg)
