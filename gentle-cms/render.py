#!/usr/bin/env python

import sys
import yaml

##########
#  HELPERS
##################

def input_checking(inputArgs):
    if verify_length(inputArgs, 2) is False or \
    verify_extension(inputArgs, ".md") is False:
        print "usage: render.py index.md"
        sys.exit()
    else:
            return inputArgs[1]

def check_length(inputArgs, length):
    if len(inputArgs) != length:
        return False
    else:
        return True

def check_extension(fileToCheck, extension):
    extensionLength = len(extension)
    if fileToCheck[-extensionLength:] == extension:
        return True
    else:
        return False

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)

def load_configuration():
    CONFIG_FILE = "config.yaml"
    stream      = open(CONFIG_FILE, 'r')
    config_link = yaml.load(stream)
    for key, value in doc.items():
        print key, '->', value
        print '\n'

#################

FORMAT_TYPE = enum(HEADER = 0, SUB_HEADER = 1, PARAGRAPH = 2, IMAGE = 3,
                   YOUTUBE_VIDEO = 4, LINK = 5)

MARKDOWN_SOURCE = input_checking(sys.argv)
