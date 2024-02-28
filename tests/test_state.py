#!/usr/bin/python3

import os
import unittest

from models import storage
from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        storage.__objects = {}

    def test_name(self):
        myModel = State()
        myModel.name = "Baku"
        self.assertEqual(myModel.name, "Baku")
