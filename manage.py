#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json

from ink.sys.config import load_conf


conf_file = os.path.dirname(__file__) + '/var/settings.json'
load_conf(conf_file)

from ink.sys.config import conf
print(conf.database)
