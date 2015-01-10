#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
    print "usage: render.py index.md"
    sys.exit()

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)

FORMAT_TYPE = enum(HEADER = 0, SUB_HEADER = 1, PARAGRAPH = 2, IMAGE = 3,
                   YOUTUBE_VIDEO = 4, LINK = 5)
