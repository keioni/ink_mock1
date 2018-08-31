#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import ink.sys.config


conf = ink.sys.config.load()
print(conf.db_connect_config())
