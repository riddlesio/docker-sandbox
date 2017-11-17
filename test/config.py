'''
This module contains all the configuration necessary
to run the basic test suite for all compiler and 
runtime images.

In order to add a test for a programming language,
just add a tuple to the list of PROGRAMMING_LANGUAGES
containing the lowercase slug of the programming language
and the runtime which should execute the binary.
'''

PROGRAMMING_LANGUAGES = [
    ('c', None),
    ('cpp', None),
    ('cs', 'mono'),
    ('go', None),
    ('haskell', None),
    ('java', 'java -jar'),
    ('javascript', 'node'),
    ('kotlin', 'java -jar'),
    ('lua', 'lua'),
    ('pascal', None),
    ('php', 'php'),
    ('python3', 'python3'),
    ('scala', 'scala'),
]
