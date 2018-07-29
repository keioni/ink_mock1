#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

from ink.util.security import secure_hashing
from ink.sys.config import CONF


class Users:

    def __init__(self):
        self.conn = mysql.connector.connect(**CONF.db_connect_config)
        self.salt = 'hoge' # XXX

    def get_uid(self, username: str) -> int:
        sql_stmt = '''
            select user_id from users where username = '?'
        '''
        user_id = 0
        cur = self.conn.cursor()
        sql_args = list(username)
        cur.execute(sql_stmt, sql_args)
        row = cur.fetchone()
        if row:
            user_id = int(row[0])
        cur.close()
        return user_id

    def get_username(self, user_id: int) -> str:
        sql_stmt = '''
            select username from users where user_id = ?
        '''
        username = ''
        cur = self.conn.cursor()
        sql_args = list(user_id)
        cur.execute(sql_stmt, sql_args)
        row = cur.fetchone()
        if row:
            username = str(row[0])
        cur.close()
        return username

    def add_user(self, username: str, password: str) -> int:
        # XXX
        return self.get_uid(username)

    def delete_user(self, user_id: int) -> bool:
        pass

    def auth_user(self, username: str, password: str) -> bool:
        sql_stmt = '''
            select password from users where username = '?'
        '''
        stored_password = ''
        input_password = secure_hashing(username, self.salt)
        cur = self.conn.cursor()
        sql_args = list(username)
        cur.execute(sql_stmt, sql_args)
        row = cur.fetchone()
        if row:
            stored_password = str(row[0])
        cur.close()
        return stored_password == input_password
