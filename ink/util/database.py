# -*- coding: utf-8 -*-

import mysql.connector

from ink.sys.config import CONF


class DBMaintainer:
    '''
    INK System Database Maintainer
    '''

    # select * from boxes where user_id=$UID
    # select * from cards where user_id=$UID
    # select * from cards where user_id=$UID and box_id=$BID
    # select record from records where card_id=$CID

    TABLE_DEFS = {
    'tokens': '''
        create table tokens (
            rowid integer auto_increment,
            token bigint,
            user_id integer,
            ctime datetime not null,
            primary key (token),
        )
    ''',
    'users': '''
        create table users (
            rowid integer auto_increment,
            token bigint,
            user_id integer,
            ctime datetime not null,
            primary key (token),
        )
    ''',
    'boxes': '''
        create table boxes (
            box_id integer auto_increment,
            user_id integer,
            box_title varchar(32) not null,
            ctime datetime,
            mtime datetime,
            primary key (box_id),
            index index_user (user_id),
        )
    ''',
    'cards': '''
        create table cards (
            card_id integer auto_increment,
            box_id integer,
            user_id integer,
            card_title varchar(32) not null,
            ctime datetime,
            mtime datetime,
            recent_records char(340),
            primary key (card_id),
            index index_user_box (user_id, box_id),
        )
    ''',
    'records': '''
        create table records (
            rowid integer auto_increment,
            card_id integer,
            record char(16),
            primary key (rowid),
            index index_card (card_id),
        )
    '''
    }

    def __init__(self):
        self.conn = mysql.connector.connect(**CONF.db_connect_config)
        self.conn.autocommit(False)

    def __get_defined_tables(self) -> list:
        tables = list()
        for table_name in self.TABLE_DEFS.keys():
            tables.append(table_name)
        return tables

    def execute(self, statements: list) -> bool:
        result = False
        cursor = self.conn.cursor()
        if cursor:
            try:
                for statement in statements:
                    cursor.execute(statement)
                self.conn.commit()
                result = True
            except mysql.connector.Error:
                self.conn.rollback()
            finally:
                cursor.close()
        return result

    def __select(self, statement: str, fetch_type: str = 'all') -> tuple:
        result = tuple()
        cursor = self.conn.cursor()
        if cursor:
            cursor.execute(statement)
            if fetch_type == 'all':
                result = tuple(cursor.fetchall())
            elif fetch_type == 'one':
                result = tuple(cursor.fetchone())
            cursor.close()
        return result

    def fetchone(self, statement) -> tuple:
        return self.__select(statement, 'one')

    def fetchall(self, statement) -> tuple:
        return self.__select(statement, 'all')

    def create_tables(self, tables: list=None) -> bool:
        if not tables:
            tables = self.__get_defined_tables()
        statements = list()
        for table in tables:
            statements.append(self.TABLE_DEFS[table])
        return self.execute(statements)

    def destroy_tables(self, tables: list=None) -> bool:
        if not tables:
            tables = self.__get_defined_tables()
        statements = list()
        for table in tables:
            statements.append('drop table {}'.format(table))
        return self.execute(statements)
