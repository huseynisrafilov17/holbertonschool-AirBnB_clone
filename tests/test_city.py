#!/usr/bin/python3

import os
import unittest

from models import storage
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        storage.__objects = {}

    def test_name(self):
        myModel = City()
        myModel.name = "Baku"
        self.assertEqual(myModel.name, "Baku")

    def test_state_id(self):
        myModel = City()
        myModel.state_id = "164"
        self.assertEqual(myModel.state_id, "164")
