# -*- coding: utf-8 -*-

import configparser
import os

class ConfigManager(configparser.ConfigParser):
    '''
    INK System configuration manager.

    Used for customizing system behaviors by config file.
    '''

    def __init__(self, *args, **kwargs):
        super(ConfigManager, self).__init__(*args, **kwargs)
        self.BOOLEAN_STATES = {'enable': True, 'disable': False}

    def read(self, filename: str = '', encoding = None):
        if not filename:
            filename = os.path.dirname(__file__) + '/settings.cfg'
        super(ConfigManager, self).read(filename, encoding)

    # def __getattr__(self, name):
    #     if name == 'db_connect_config':
    #         db_conf = dict()
    #         if section_name in self:
    #             for key in self[section_name]:
    #                 value = self[section_name][key]
    #                 if key == 'port':
    #                     value = int(value)
    #                 db_conf[key] = value
    #         return db_conf
    #     msg = '{} object has no attribute {}'.format(type(self), name)
    #     raise AttributeError(msg)

    # def __setattr__(self, name, value):
    #     msg = ''
    #     if name == 'db_connect_config':
    #         msg = 'readonly attribute {}'.format(type(self))
    #     if msg:
    #         raise AttributeError(msg)
    #     super().__setattr__(name, value)

    def get_db_connect_config(self, section_name: str = 'database'):
        '''
        db_connect_config return a string used for mysql.connect() method.
        '''
        db_conf = dict()
        if section_name in self:
            for key in self[section_name]:
                value = self[section_name][key]
                if key == 'port':
                    value = int(value)
                db_conf[key] = value
        return db_conf
