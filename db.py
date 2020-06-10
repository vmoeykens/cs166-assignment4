"""
This file includes a simple database class, which provides methods:

    execute_query:  Takes a query as a string and executes it with a current
                    database connection. Doing things this way is not advised,
                    since it introduces vulnerability to injection attack.
                    We do it this way for instructional purposes only!

    setup:          A utility to create a fresh instance of the database,
                    and to populate it with some records for testing.

Here we use SQLite directly rather than an ORM (object relational mapper, e.g.,
SQLAlchemy) because it's easier for students to see what's going on in SQL
queries.
"""

import os
import json
from typing import Union
import sqlite3
import config


class Db:
    """Database class for bank environment. """

    # SQL query to create `account` table
    CREATE_TABLE_ACCOUNT = """CREATE TABLE IF NOT EXISTS account (
        id integer PRIMARY KEY,
        uname text NOT NULL,
        pw_hash text NOT NULL,
        created_at datetime NOT NULL,
        last_login datetime NOT NULL
    );"""

    # Note: Spelling "trnsaction" is intentional
    CREATE_TABLE_TRANSACTION = """CREATE TABLE IF NOT EXISTS trnsaction (
        id integer PRIMARY KEY,
        account_id integer NOT NULL,
        debit float,
        credit float,
        dt datetime NOT NULL,
        memo text,
        FOREIGN KEY(account_id) REFERENCES account(id)
    );
    """

    INSERT_ACCOUNT = """INSERT INTO account
        (id, uname, pw_hash, created_at, last_login)
        VALUES("{id}", "{uname}", "{pw_hash}", "{created_at}", 
        "{last_login}");"""

    INSERT_TRANSACTION = """INSERT INTO trnsaction
        (id, account_id, debit, credit, dt, memo)
        VALUES("{id}", "{account_id}", "{debit}", "{credit}", "{dt}", 
        "{memo}");"""

    @staticmethod
    def get_connection():
        """
        Get a connection to the database
        :return: sqlite3.Connection
        """
        return sqlite3.connect(config.DB_FILE)

    @staticmethod
    def execute_query(cnx: sqlite3.Connection, query: str):
        """
        Execute a SQL query. This method takes a connection to the database
        and executes a query passed in as a string.
        :param cnx: sqlite3.Connection
        :param query: str
        """
        c = cnx.cursor()
        if config.SC in query:
            c.executescript(query)
        else:
            c.execute(query)
        cnx.commit()
        return c

    @classmethod
    def setup(cls) -> Union[sqlite3.Connection, None]:
        """
        Setup the database tables
        """
        try:
            os.remove(config.DB_FILE)
        except FileNotFoundError:
            pass
        try:
            cnx = cls.get_connection()
            cls.execute_query(cnx, cls.CREATE_TABLE_ACCOUNT)
            cls._populate_accounts(cnx)
            cls.execute_query(cnx, cls.CREATE_TABLE_TRANSACTION)
            cls._populate_transactions(cnx)
            c = cls.list_tables(cnx)
            rows = c.fetchall()
            assert ('account',) in rows
            assert ('trnsaction',) in rows
            return cnx  # Because maybe you want to reuse it
        except sqlite3.Error as e:
            print("An error has occurred. Please report this incident.")
            print(e)
            return None

    @classmethod
    def list_tables(cls, cnx: sqlite3.Connection):
        """
        List tables
        :param cnx:
        :return:
        """
        q = "SELECT name FROM sqlite_master WHERE type ='table' " \
            "AND name NOT LIKE 'sqlite_%'"
        c = cls.execute_query(cnx, q)
        return c

    @classmethod
    def _populate_accounts(cls, cnx: sqlite3.Connection):
        """
        Populate account table with records from JSON file. Yes, we could do
        this more efficiently. Suffices for our purposes.
        :param cnx: sqlite3.Connection
        """
        with open('./data/accounts.json', 'r') as f:
            data = json.load(f)
        for record in data['RECORDS']:
            query = cls.INSERT_ACCOUNT.format(
                id=record['id'],
                uname=record['uname'],
                pw_hash=record['pw_hash'],
                created_at=record['created_at'],
                last_login=record['last_login']
            )
            # print(query)
            c = cls.execute_query(cnx, query)
        return c

    @classmethod
    def _populate_transactions(cls, cnx: sqlite3.Connection):
        """
        Populate transaction table with records from JSON file. Yes, we could
        do  this more efficiently. Suffices for our purposes.
        :param cnx: sqlite3.Connection
        """
        with open('./data/transactions.json', 'r') as f:
            data = json.load(f)
        for record in data['RECORDS']:
            query = cls.INSERT_TRANSACTION.format(
                id=record['id'],
                account_id=record['account_id'],
                debit=record['debit'],
                credit=record['credit'],
                dt=record['dt'],
                memo=record['memo']
            )
            # print(query)
            c = cls.execute_query(cnx, query)
        return c
