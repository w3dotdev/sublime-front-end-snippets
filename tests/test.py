#!/usr/bin/env python3

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from source.json_generator import get_json
from source.duplicates import list_duplicates
import json
import re
import unittest

class TestDuplicatesMethods(unittest.TestCase):

  def test_duplicates(self):
    json = get_json('snippets/')
    triggers = []
    for snippet in json:
      trigger = snippet['trigger']
      if re.search(r'z.', trigger) is None:
        triggers.append(trigger)

    self.assertEqual(list_duplicates(triggers), [])

if __name__ == '__main__':
  unittest.main()
