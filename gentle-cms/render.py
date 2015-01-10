#!/usr/bin/env python

import sys
import yaml

##########
#  HELPERS
##################

def input_checking(inputArgs):
    if check_length(inputArgs, 2) is False or \
       check_extension(inputArgs, ".md") is False:
        print "usage: render.py index.md"
        sys.exit()
    else:
            return inputArgs[1]

def check_length(inputArgs, length):
    if len(inputArgs) == length:
        return True
    else:
        return False

def check_extension(inputArgs, extension):
    extensionLength = len(extension)
    fileToCheck = inputArgs[1]
    if fileToCheck[-extensionLength:] == extension:
        return True
    else:
        return False

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)

class Utils:
    def __init__(self):
        pass

    @staticmethod
    def load_configuration():
        CONFIG_FILE  = "config.yaml"
        config_data  = {}
        stream       = open(CONFIG_FILE, 'r')
        config_steam = yaml.load(stream)
        for key, value in config_steam.items():
            config_data.update({key : value})
        return config_data

    @staticmethod
    def is_header(entry):
        return True

    @staticmethod
    def is_sub_header(entry):
        return True

    @staticmethod
    def is_paragraph(entry):
        return True
#################

FORMAT_TYPE = enum(HEADER = 0, SUB_HEADER = 1, PARAGRAPH = 2, IMAGE = 3,
                   YOUTUBE_VIDEO = 4, LINK = 5)


class Render:
    def __init__(self, markdown_source):
        self.markdown_source = markdown_source
        self.configuration = Utils.load_configuration()

    def scan_source(self, source):
        markdown_data = []
        with open(source) as stream:
            for line in stream:
                markdown_data.append((Render.check_entry_type(line), line))
                print line
        print markdown_data

    def scan_entry(self, entry):
        # Find images
        # Find youtube videos
        # Find links
        return None

    @staticmethod
    def check_entry_type(entry):
        if Utils.is_header(entry) is True:
            return FORMAT_TYPE.HEADER
        elif Utils.is_sub_header(entry) is True:
            return FORMAT_TYPE.SUB_HEADER
        elif Utils.is_paragraph(entry) is True:
            return FORMAT_TYPE.PARAGRAPH

