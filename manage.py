#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from attrdict import AttrDict

import ink.sys.config


filename = os.path.dirname(__file__) + '/var/settings.json'
gconf = ink.sys.config.load(filename)
print(dict(gconf.configurations.database))
