#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.dos.anjos@gmail.com>
# Thu 12 May 14:02:28 2011 

"""Dumps lists of files.
"""

import os
import sys

# Driver API
# ==========
help_message = 'Dumps lists of files based on your criteria'

def dumplist(args):
  from .query import Database
  db = Database()

  r = db.files(
      directory=args.directory, 
      extension=args.extension,
      device=args.device, 
      support=args.support, 
      groups=args.group, 
      cls=args.cls
      )

  output = sys.stdout
  if args.selftest:
    from ..utils import null
    output = null()

  for id, f in r.items():
    output.write('%s\n' % (f,))

def add_commands(parser):
  """Add specific subcommands that the action "dumplist" can use"""

  parser.add_argument('-d', '--directory', dest="directory", default='', help="if given, this path will be prepended to every entry returned (defaults to '%(default)s')")
  parser.add_argument('-e', '--extension', dest="extension", default='', help="if given, this extension will be appended to every entry returned (defaults to '%(default)s')")
  parser.add_argument('-c', '--class', dest="cls", default='', help="if given, limits the dump to a particular subset of the data that corresponds to the given class (defaults to '%(default)s')", choices=('real', 'attack', ''))
  parser.add_argument('-g', '--group', dest="group", default='', help="if given, this value will limit the output files to those belonging to a particular protocolar group. (defaults to '%(default)s')", choices=('train', 'devel', 'test', ''))
  parser.add_argument('-s', '--support', dest="support", default='', help="if given, this value will limit the output files to those using this type of attack support. (defaults to '%(default)s')", choices=('fixed', 'hand', ''))
  parser.add_argument('-x', '--device', dest="device", default='', help="if given, this value will limit the output files to those using this type of device for attacks. (defaults to '%(default)s')", choices=('print', 'mobile', 'highdef', ''))
  parser.add_argument('--self-test', dest="selftest", default=False,
      action='store_true')
  parser.set_defaults(func=dumplist)
