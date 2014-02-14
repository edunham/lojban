#! /usr/bin/env python2.7

import sqlite3

class Vocab(Object):
    """
    The Vocabulary wraps the db holding word lists

    Probably also an English thesaurus for trying to map words or phrases to
    their closest Lojban equivalent when they occur nowhere in the Lojban
    language materials.
    """
    self.db = ''
    self.listpath = ['','']

    def __init__(self):
        # Check whether the database exists and stuff
        pass

    def read_lists(self):
        # nuke the db if it exists, and read in all the words from the lists
        pass

    def get_translation(self, w):
        # Query DB for all lojban words for whom w appears in their definition
        pass

    def is_lojban(self, w):
        # True if w appears anywhere in lojban corpus; else false
        pass

class LojbanWord(Object):
    def __init__(self):
        pass

    def pronounce(self):
        # phonetic pronunciation from spelling
        pass

class Gismu(LojbanWord):
    def __init__(self):
        pass

class Cmavo(LojbanWord):
    def __init__(self):
        pass

class Translation(Object):
    """
    a Translation tries to represent meaning. Holds original sentence and blob
    of possible phrasings in the other language.
    """
    def __init__(self, sentence):
        #
        pass
    def pprint(self):
        # pretty-print
        pass


