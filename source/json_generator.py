#!/usr/bin/env python3

import os
import fnmatch
from json import dumps

def write_json(data, filename):
  try:
    jsondata = dumps(data, indent=2, skipkeys=True, sort_keys=True)
    fd = open(filename, 'w')
    fd.write(jsondata)
    fd.close()
  except:
    print 'ERROR writing', filename
    pass

def get_dir(path, ext):
  matches = []
  for root, dirnames, filenames in os.walk(path):
    for filename in fnmatch.filter(filenames, ext):
      matches.append(os.path.join(root, filename))
  return matches

def get_json():
  result = []
  for count, file in enumerate(get_dir('../snippets/', '*.sublime-snippet'), start=1):
    line        = open(file)
    content     = line.read()
    trigger     = content.split('<tabTrigger>')[1].split('</tabTrigger>')[0]
    description = content.split('<description>')[1].split('</description>')[0]

    result.append({'id':count, 'trigger':trigger, 'description':description})

  return result


write_json(get_json(), "../snippets.json")

