#!/usr/bin/env python3

import sys
sys.path.append('../source/')
from json_generator import getJson
import json
import re
import unittest

def list_duplicates(seq):
  seen = set()
  seen_add = seen.add
  # adds all elements it doesn't know yet to seen and all other to seen_twice
  seen_twice = set( x for x in seq if x in seen or seen_add(x) )
  # turn the set into a list (as requested)
  return list( seen_twice )

class TestDuplicatesMethods(unittest.TestCase):

  def test_duplicates(self):
    json = getJson()
    triggers = []

    for snippet in json:
      trigger = snippet['trigger']
      if re.match(r'^z', trigger) is None:
        triggers.append(trigger)

    self.assertEqual(list_duplicates(triggers), [])

if __name__ == '__main__':
  unittest.main()
