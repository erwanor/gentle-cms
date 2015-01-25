#!/usr/bin/env python

from sys import argv
from yaml import load
from re import match, findall

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)

ENTRY_TYPE = enum(HEADER = 0, SUB_HEADER = 1, PARAGRAPH = 2, UNKNOWN = 3)
LINK_TYPE   = enum(IMAGE  = 0, YOUTUBE    = 1, LINK = 2, UNKNOWN = 3)

class Utils:
    def __init__(self):
        pass

    @staticmethod
    def input_checking(inputArgs):
        if check_length(inputArgs, 2) is False or \
           check_extension(inputArgs, ".md") is False:
            print "usage: render.py index.md"
            sys.exit()
        else:
                return inputArgs[1]

    @staticmethod
    def check_length(inputArgs, length):
        if len(inputArgs) == length:
            return True
        else:
            return False

    @staticmethod
    def check_extension(inputArgs, extension):
        extensionLength = len(extension)
        fileToCheck = inputArgs[1]
        if fileToCheck[-extensionLength:] == extension:
            return True
        else:
            return False


    class Identify:
        def __init__(self):
            pass

        @staticmethod
        def is_header(entry):
            matched = match('^[\#]{1}([a-z-A-Z-0-9- ._:)($\[\]!~@,-]{1,})$', entry)
            return matched is not None

        @staticmethod
        def is_sub_header(entry):
            matched = match('^[\#]{2}([a-z-A-Z-0-9- ._:)($\[\]!~@,-]{1,})$', entry)
            return matched is not None

        @staticmethod
        def is_paragraph(entry):
            matched = match('^[\-]{3}([a-z-A-Z-0-9- ._:)($\[\]!~@,-]{1,})[\-]{3}$', entry)
            return matched is not None

        @staticmethod
        def match_links(raw_entry):
            matched = findall('\[([a-zA-Z0-9\ \!\?\,\:\*\'\;\/\/\.\&\=\?\%]*)\]\((https?\:\/\/[a-zA-Z-0-9\/\.\&\=\?\%]*)\)', raw_entry)
            return matched

        @staticmethod
        def check_entry_type(entry):
            if self.is_header(entry) is True:
                return ENTRY_TYPE.HEADER
            elif self.is_sub_header(entry) is True:
                return ENTRY_TYPE.SUB_HEADER
            elif self.is_paragraph(entry) is True:
                return ENTRY_TYPE.PARAGRAPH
            else:
                return ENTRY_TYPE.UNKNOWN

        @staticmethod
        def check_match_type(match):
            if self.is_image(match.group(2)) is True:
                return LINK_TYPE.IMAGE
            elif self.is_youtube(match.group(2)) is True:
                return LINK_TYPE.YOUTUBE
            else:
                return LINK_TYPE.LINK

class Configuration:
    def __init__(self, config="config.yaml"):
        self.CONFIG_FILE = config

    @staticmethod
    def load_configuration():
        config_data  = {}
        stream       = open(self.CONFIG_FILE, 'r')
        config_steam = load(stream)
        for key, value in config_steam.items():
            config_data.update({key : value})
        return config_data


class PreProcessing:
    def __init__(self, markdown_source):
        self.markdown_source = markdown_source

    def scan_source(self, source):
        markdown_data = []
        with open(source) as stream:
            for line in stream:
                markdown_data.append((Utils.Identify.check_entry_type(line), line))
                print line
        print markdown_data

    def scan_entry(self, raw_entry):
        match = Utils.Identify.match_links(raw_entry)
        if match is not None:
            match_type = Utils.Identify.check_match_type(match)

        return None

class Processing:
    def __init__(self):
        pass

    def link_to_html(self, match):
        pass

        #self.configuration = Configuration.load_configuration()
