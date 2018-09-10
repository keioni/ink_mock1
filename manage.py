#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from ink.sys.config import gconf


filename = os.path.dirname(__file__) + '/var/settings.cfg'
gconf.read(filename)
print(gconf.get_db_connect_config())
