#!/usr/bin/python3

import os
import unittest

from models import storage
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        storage.__objects = {}

    def test_name(self):
        myModel = Amenity()
        myModel.name = "Test"
        self.assertEqual(myModel.name, "Test")