# -*- coding: utf-8 -*-

# Copyright 2014-2015 by Christopher C. Little.
# This file is part of Abydos.
#
# Abydos is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Abydos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Abydos. If not, see <http://www.gnu.org/licenses/>.

"""abydos.tests.test_ngram

This module contains unit tests for abydos.ngram
"""

from __future__ import unicode_literals
import unittest
from abydos.corpus import Corpus
from abydos.ngram import NGramCorpus


class NGramCorpusTestCases(unittest.TestCase):
    """test cases for abydos.ngram.NGramCorpus
    """
    def test_init(self):
        """test abydos.ngram.__init__
        """
        self.assertIsInstance(NGramCorpus(), NGramCorpus)
        # TODO: Add constructor from Corpus test
        self.assertRaises(TypeError, NGramCorpus, ["a", "b", "c"])

    def test_corpus_importer(self):
        """test abydos.ngram.corpus_importer
        """
        pass

    def test_gng_importer(self):
        """test abydos.ngram.gng_importer
        """
        pass

    def test_get_count(self):
        """test abydos.ngram.get_count
        """
        pass


if __name__ == '__main__':
    unittest.main()
