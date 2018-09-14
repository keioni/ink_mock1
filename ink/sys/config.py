# -*- coding: utf-8 -*-

import os
import json

from attrdict import AttrDict


class Configure:

    def __init__(self, conf_dict: dict=None):
        self.__conf = {}
        if conf_dict:
            self.__conf = conf_dict

    def __getattr__(self, name):
        if not self.__conf:
            msg = 'Setting file does not loaded.'
            raise AttributeError(msg)
        values = self.__conf['configurations'].get(name)
        if values:
            return AttrDict(values)
        msg = 'No configuration values of name: {}'.format(name)
        raise AttributeError(msg)

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.__conf)

    # def __str__(self):
    #     return json.dumps(self.__conf, indent=4)

    def load(self, conf_file: str, force_load: bool=False):
        if self.__conf:
            if not force_load:
                msg = 'Still loaded.'
                raise ValueError(msg)
        with open(conf_file, 'r') as f:
            self.__conf = json.load(f)
        if not self.__conf:
            msg = 'Cannot load system settings from the file.'
            raise ValueError(msg)
        if self.__conf.get('version') != '1.0':
            msg = 'Version number does not exist or not match this system.'
            raise ValueError(msg)
        if not self.__conf.get('configurations'):
            msg = "Setting file's format is invalid."
            raise ValueError(msg)


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
