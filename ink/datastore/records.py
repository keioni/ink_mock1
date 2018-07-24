#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector


class Records:
    db_conn_elem: dict

    def __init__(self):
        self.conn: mysql.connector.MySQLConnection

    def connect(self):
        self.conn = mysql.connector.connect(self.db_conn_elem)

    def get_boxes(self, user_id: str) -> list:
        sql_stmt = '''
            select * from boxes where user_id = '?'
        '''
        cur = self.conn.cursor()
        sql_args = list(user_id)
        cur.execute(sql_stmt, sql_args)

    def get_cards(self, user_num: int, box_num: int) -> list:
        sql_stmt = '''
            select * from cards where user_num = ? and box_num = ?
        '''
        cur = self.conn.cursor()
        sql_args = list(user_num, box_num)
        cur.execute(sql_stmt, sql_args)

    def get_records(self, card_num: int) -> list:
        sql_stmt = '''
            select record from records where card_num = ?
        '''
        cur = self.conn.cursor()
        sql_args = list(card_num)
        cur.execute(sql_stmt, sql_args)


def get_all():
    pass
