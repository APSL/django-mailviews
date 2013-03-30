#!/usr/bin/env python
# encoding: utf-8
# ----------------------------------------------------------------------------

__version__ = (0, 5, 1)

def get_version():
    bits = [str(bit) for bit in __version__]
    version = bits[0]
    for bit in bits[1:]:
        version += (bit.isdigit() and '.' or '') + bit
    return version


