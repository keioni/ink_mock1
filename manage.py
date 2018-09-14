#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json

from ink.sys.config import conf

conf_file = os.environ.get('INK_CONF_FILE')
if not conf_file:
    conf_file = './var/settings.json'
conf.load(conf_file, True)
print(conf)
print(conf.database)
print(conf.database.host)
