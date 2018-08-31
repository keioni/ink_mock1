# -*- coding: utf-8 -*-

import configparser
import os

class Configure(configparser.ConfigParser):
    '''
    Configure class.
    '''

    # def __init__(self, *args, **kwargs):
    #     super(Configure, self).__init__(*args, **kwargs)

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


def load(conf_filename: str = '') -> configparser.ConfigParser:
    conf = Configure()
    conf.BOOLEAN_STATES = {'enable': True, 'disable': False}
    if not conf_filename:
        conf_filename = os.path.dirname(__file__) + '/settings.cfg'
    if os.path.exists(conf_filename):
        conf.read(conf_filename)

    return conf
