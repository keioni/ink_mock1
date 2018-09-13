# -*- coding: utf-8 -*-

import os
import json

from attrdict import AttrDict


class Configure:

    def __init__(self):
        self.__conf = {}

    def load(self, conf_file: str, force_load: bool=False):
        if self.__conf:
            if not force_load:
                msg = 'Still loaded.'
                raise ValueError(msg)
        with open(conf_file, 'r') as f:
            raw_conf = json.load(f)
        if not raw_conf:
            msg = 'Cannot load system settings from the file.'
            raise ValueError(msg)
        if raw_conf.get('version') != '1.0':
            msg = 'Version number does not exist or not match this system.'
            raise ValueError(msg)
        self.__conf = raw_conf.get('configurations')

    def __getattr__(self, name):
        if not self.__conf:
            msg = 'Configuration file does not loaded.'
            raise AttributeError(msg)
        values = self.__conf.get(name)
        if values:
            return AttrDict(values)
        msg = 'No configuration values of name: {}'.format(name)
        raise AttributeError(msg)

conf = Configure()

# conf = AttrDict()

# conf_file = os.environ.get('INK_CONF_FILE')
# if not conf_file:
#     conf_file = './var/settings.json'

# with open(conf_file, 'r') as f:
#     raw_conf = json.load(f)
# if not raw_conf:
#     msg = 'Cannot load system settings from the file.'
#     raise ValueError(msg)
# if raw_conf.get('version') != '1.0':
#     msg = 'Version number does not exist or not match this system.'
#     raise ValueError(msg)
# conf = AttrDict(raw_conf.get('configurations'))
