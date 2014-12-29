# Copyright (c) 2014, Matt Layman

import os

from tap.main import main
from tap.tests import TestCase


class TestMain(TestCase):
    """Tests for tap.main.main"""

    def test_exits_with_error(self):
        """The main function returns an error status if there were failures."""
        argv = ['/bin/fake', 'fake.tap']
        stream = open(os.devnull, 'wb')

        status = main(argv, stream=stream)

        self.assertEqual(1, status)