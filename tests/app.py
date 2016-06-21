# -*- coding: utf-8 -*-

from .context import pathpattern
from pathpattern import *

import unittest

class TestAppSuite(unittest.TestCase):
    """Rendering test cases."""

    def test_app(self):
        print '   TEST APP!'
        print '   '
        print '   generate abstract diagram'
        print '   '
        print '   import work data'
        print '   generate report'
        print '   generate report diagram'
        print '   '
        print '   import corpus data'
        print '   generate report'
        print '   generate report diagram'
        print '   '
        print '   compare work to corpus'
        print '   search for feature in corpus'
        print '   '

if __name__ == '__main__':
    unittest.main()
