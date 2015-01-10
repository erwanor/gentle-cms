#!/usr/bin/env python

import sys

##########
#  HELPERS
##################

def check_extension(fileToCheck, extension):
    extensionLength = len(extension)
    if fileToCheck[-extensionLength:] == extension:
        return True
    else:
        return False

def verify_input(inputArgs):
    if len(inputArgs) != 2:
        print "usage: render.py index.md"
        sys.exit()
    else:
        MARKDOWN_FILE = inputArgs[1]
        check = check_extension(MARKDOWN_FILE, ".md")
        if check is False:
            print "The input extension is not .md"
            sys.exit()
        else:
            return MARKDOWN_FILE

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)

#################

FORMAT_TYPE = enum(HEADER = 0, SUB_HEADER = 1, PARAGRAPH = 2, IMAGE = 3,
                   YOUTUBE_VIDEO = 4, LINK = 5)

SOURCE = verify_input(sys.argv)
