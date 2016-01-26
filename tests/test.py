#!/usr/bin/env python3

import sys
sys.path.append('../source/')
from json_generator import get_json
from duplicates import list_duplicates
import json
import re
import unittest

class TestDuplicatesMethods(unittest.TestCase):

  def test_duplicates(self):
    json = get_json()
    triggers = []

    for snippet in json:
      trigger = snippet['trigger']
      if re.match(r'^z', trigger) is None:
        triggers.append(trigger)

    self.assertEqual(list_duplicates(triggers), [])

if __name__ == '__main__':
  unittest.main()
