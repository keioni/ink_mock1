#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json

from ink.sys import conf

conf.load(os.environ.get('INK_CONF_FILE'))
# conf.load(os.environ.get('./var/settings.json'))
print(conf.database)
print(conf.database.host)
