#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from ink.sys.config import ConfigManager


conf = ConfigManager()
conf.read()
print(conf.get_db_connect_config())
