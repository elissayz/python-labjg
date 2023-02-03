#!/usr/bin/python3

import Fixme
import pytest
  
  
def evens(n):
    arr = range(n+1)
    arr = filter(lambda x: (x % 2 == 0), arr)
    return list(arr)
