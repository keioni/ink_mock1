# -*- coding: utf-8 -*-

import configparser

class ConfigParser(configparser.ConfigParser):
    salt = 'oajokkN6AkwZB4wA0XpFtzlJpYYTVB7a9JkjV56PMAs'
    debug_sql_print = True
    db_name = 'ink'
    db_host = 'localhost'
    db_port = 3306
    db_user = ''
    db_password = ''


conf = ConfigParser()
conf.BOOLEAN_STATES = {'enable': True, 'disable': False}
conf.db_connect_config = {
    'database': conf.db_name,
    'host': conf.db_host,
    'port': conf.db_port,
    'user': conf.db_user,
    'passwod': conf.db_password,
}
conf.read('./sys/settings.cfg', 'utf-8')
