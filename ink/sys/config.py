# -*- coding: utf-8 -*-

import configparser

class ConfigParser(configparser.ConfigParser):
    salt = 'oajokkN6AkwZB4wA0XpFtzlJpYYTVB7a9JkjV56PMAs'
    validation_timeout_in_sec = 3600
    db_connect_string = 'sqlite:///cyreco/db/userlist.sqlite3'
    debug_sql_print = True
    db_database = ''
    db_host = 'localhost'
    db_port = 3306
    db_user = ''
    db_password = ''

CONF = ConfigParser()
CONF.db_connect_config = {
    'database': CONF.db_database,
    'host': CONF.db_host,
    'port': CONF.db_port,
    'user': CONF.db_user,
    'passwod': CONF.db_password,
}
CONF.read('./sys/settings.cfg', 'utf-8')
