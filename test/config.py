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
    ('cs', ''),
    ('javascript', 'node'),
    ('php', 'php')
]