#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector


class Users:
    db_conn_elem: dict

    def __init__(self):
        self.conn = mysql.connector.connect(self.db_conn_elem)

    def get_uid(self, username: str) -> int:
        sql_stmt = '''
            select user_id from users where username = '?'
        '''
        cur = self.conn.cursor()
        sql_args = list(username)
        cur.execute(sql_stmt, sql_args)
        row = cur.fetchone()
        if row:
            return int(row[0])
        else:
            return 0

    def get_username(self, user_id: int) -> str:
        sql_stmt = '''
            select username from users where user_id = ?
        '''
        cur = self.conn.cursor()
        sql_args = list(user_id)
        cur.execute(sql_stmt, sql_args)
        row = cur.fetchone()
        if row:
            return str(row[0])
        else:
            return ''

    def add_user(self, username: str, password: str) -> int:
        # XXX
        return self.get_uid(username)

    def delete_user(self, user_id: int) -> bool:
        pass

    def auth_user(self, user_id: int, password: str) -> bool:
        pass
