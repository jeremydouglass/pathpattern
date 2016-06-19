# -*- coding: utf-8 -*-

from .context import pathpattern

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        sample.hmm()


if __name__ == '__main__':
    unittest.main()
